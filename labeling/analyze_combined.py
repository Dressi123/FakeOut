"""Analyze combined hand labels from rounds 1, 2, and 3 (105 listings total)."""
import pandas as pd
import numpy as np

ROOT = '/Users/dressi/Desktop/github/FakeOut/'
r1 = pd.read_csv(ROOT + 'labeling_sample.csv')
r2 = pd.read_csv(ROOT + 'labeling_sample_r2.csv')
r3 = pd.read_csv(ROOT + 'labeling_sample_r3.csv')
r4 = pd.read_csv(ROOT + 'labeling_sample_r4.csv')
r5 = pd.read_csv(ROOT + 'labeling_sample_r5.csv')
r6 = pd.read_csv(ROOT + 'labeling_sample_r6.csv')

# Recompute proba against current parquet (latest model)
full = pd.read_parquet(ROOT + 'df_with_snorkel.parquet')
for sub in (r1, r2, r3, r4, r5, r6):
    sub['snorkel_proba_scam'] = sub['orig_idx'].map(full['snorkel_proba_scam'])
    sub['snorkel_label']      = sub['orig_idx'].map(full['snorkel_label'])

r1['round'] = 1; r2['round'] = 2; r3['round'] = 3; r4['round'] = 4; r5['round'] = 5; r6['round'] = 6
cols = ['round','sample_id','stratum','orig_idx','snorkel_proba_scam','snorkel_label','true_label']
df = pd.concat([r1[cols], r2[cols], r3[cols], r4[cols], r5[cols], r6[cols]], ignore_index=True)

print("=" * 72)
print(f"COMBINED LABEL DISTRIBUTION ({len(df)} listings)")
print("=" * 72)
print(df['true_label'].value_counts().to_string())

print()
print("=" * 72)
print("BY ROUND x STRATUM")
print("=" * 72)
print(pd.crosstab([df['round'], df['stratum']], df['true_label'], margins=True).fillna(0).astype(int).to_string())

def score(s): return 1.0 if s=='scam' else 0.5 if s=='unsure' else 0.0
df['true_score'] = df['true_label'].apply(score)
df['y_pred'] = (df['snorkel_proba_scam'] > 0.5).astype(int)

print()
print("=" * 72)
print("MODEL CONFUSION MATRIX")
print("=" * 72)
for label, transform in [
    ("strict (drop unsure)", lambda s: 0 if s=='not_scam' else 1 if s=='scam' else None),
    ("unsure=scam", lambda s: 0 if s=='not_scam' else 1),
]:
    df['y'] = df['true_label'].apply(transform)
    sub = df.dropna(subset=['y'])
    y_true = sub['y'].astype(int); y_pred = sub['y_pred']
    tp = int(((y_true==1)&(y_pred==1)).sum()); fp = int(((y_true==0)&(y_pred==1)).sum())
    tn = int(((y_true==0)&(y_pred==0)).sum()); fn = int(((y_true==1)&(y_pred==0)).sum())
    print(f"\n[{label}]  n={len(sub)}")
    print("                pred=NOT_SCAM   pred=SCAM")
    print(f"  true=NOT_SCAM   {tn:>5d}            {fp:>5d}")
    print(f"  true=SCAM       {fn:>5d}            {tp:>5d}")
    if tp+fp>0: print(f"  Precision: {tp/(tp+fp):.3f} ({tp}/{tp+fp})")
    if tp+fn>0: print(f"  Recall:    {tp/(tp+fn):.3f} ({tp}/{tp+fn})")
    print(f"  Accuracy:  {(tp+tn)/len(sub):.3f}")
    print(f"  Class balance: {y_true.mean():.2%} positive")

print()
print("=" * 72)
print("CALIBRATION")
print("=" * 72)
df['proba_bin'] = pd.cut(df['snorkel_proba_scam'], bins=[-0.001, 0.2, 0.4, 0.6, 0.8, 1.0])
cal = df.groupby('proba_bin', observed=True).agg(
    n=('true_score','size'),
    mean_true=('true_score','mean'),
    n_scam=('true_label', lambda s: (s=='scam').sum()),
    n_unsure=('true_label', lambda s: (s=='unsure').sum()),
    n_not_scam=('true_label', lambda s: (s=='not_scam').sum()),
).round(3)
print(cal.to_string())

print()
print("=" * 72)
print("WHERE THE SCAMS AND UNSURES LANDED")
print("=" * 72)
flagged = df[df['true_label'].isin(['scam','unsure'])].sort_values('snorkel_proba_scam', ascending=False)
for _, r in flagged.iterrows():
    print(f"  sample_id={r['sample_id']:>3d}  label={r['true_label']:8s}  stratum={r['stratum']:20s}  proba={r['snorkel_proba_scam']:.4f}")

print()
print("=" * 72)
print("HUNTER 1 PRECISION (free-form low-price stratum)")
print("=" * 72)
hunter = df[df['stratum']=='hunter_freeform_low']
print(f"  n = {len(hunter)}")
print(f"  scam: {(hunter['true_label']=='scam').sum()}")
print(f"  unsure: {(hunter['true_label']=='unsure').sum()}")
print(f"  not_scam: {(hunter['true_label']=='not_scam').sum()}")
print(f"  Stratum scam-rate (excl unsure): {(hunter['true_label']=='scam').sum()/len(hunter):.1%}")
print(f"  Stratum scam-rate (incl unsure): {(hunter['true_label'].isin(['scam','unsure'])).sum()/len(hunter):.1%}")

print()
print("=" * 72)
print("ESTIMATED TRUE SCAM RATE (Wilson CI)")
print("=" * 72)
def wilson(k, n, z=1.96):
    p = k/n
    denom = 1 + z**2/n
    center = (p + z**2/(2*n)) / denom
    half = z * np.sqrt(p*(1-p)/n + z**2/(4*n**2)) / denom
    return p, center-half, center+half

n_total = len(df)
n_scam = (df['true_label']=='scam').sum()
n_unsure = (df['true_label']=='unsure').sum()
p, lo, hi = wilson(n_scam, n_total)
print(f"  Strict (scam=2/{n_total}): {p:.2%}  95% CI [{lo*100:.2f}%, {hi*100:.2f}%]")
p, lo, hi = wilson(n_scam + n_unsure, n_total)
print(f"  Charitable (scam+unsure=5/{n_total}): {p:.2%}  95% CI [{lo*100:.2f}%, {hi*100:.2f}%]")

# Note: stratified samples don't give a population-level estimate directly
# Only the random/calibration strata are population-representative
print()
print("  Caveat: this CI assumes the labeled sample is representative.")
print("  Our sample is stratified — over-sampled in suspicious zones.")
print("  Population scam rate is likely LOWER than the sample rate.")

print()
print("=" * 72)
print("TOP-K PRECISION (model-ranked)")
print("=" * 72)
sorted_df = df.sort_values('snorkel_proba_scam', ascending=False)
for k in [10, 25, 50, 105]:
    if k > len(sorted_df): continue
    topk = sorted_df.head(k)
    n_scam = (topk['true_label']=='scam').sum()
    n_unsure = (topk['true_label']=='unsure').sum()
    print(f"  top-{k:3d}: scam={n_scam}  unsure={n_unsure}  not_scam={(topk['true_label']=='not_scam').sum()}  "
          f"→ precision (scam only): {n_scam/k:.1%}  (incl unsure: {(n_scam+n_unsure)/k:.1%})")
