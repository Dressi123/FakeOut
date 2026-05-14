"""Analyze hand labels: model precision/recall, per-LF precision."""
import pandas as pd
import numpy as np

df = pd.read_csv('/Users/dressi/Desktop/github/FakeOut/labeling_sample.csv')

def to_bin(s, unsure_as):
    if s == 'scam': return 1
    if s == 'not_scam': return 0
    return unsure_as

df['y_drop']    = df['true_label'].apply(lambda s: to_bin(s, np.nan))
df['y_as_scam'] = df['true_label'].apply(lambda s: to_bin(s, 1))
df['y_as_safe'] = df['true_label'].apply(lambda s: to_bin(s, 0))
df['y_pred']    = (df['snorkel_proba_scam'] > 0.5).astype(int)

print("=" * 72)
print("LABEL DISTRIBUTION")
print("=" * 72)
print(df['true_label'].value_counts().to_string())

print()
print("=" * 72)
print("STRATUM x TRUE LABEL")
print("=" * 72)
print(pd.crosstab(df['stratum'], df['true_label']).to_string())

print()
print("=" * 72)
print("MODEL PREDICTION (proba > 0.5) vs TRUE LABEL")
print("=" * 72)
for name, y_col in [("drop unsure", "y_drop"), ("unsure=scam", "y_as_scam"), ("unsure=safe", "y_as_safe")]:
    mask = df[y_col].notna()
    y_true = df.loc[mask, y_col].astype(int)
    y_pred = df.loc[mask, 'y_pred']
    n = len(y_true)
    tp = int(((y_true==1) & (y_pred==1)).sum())
    fp = int(((y_true==0) & (y_pred==1)).sum())
    tn = int(((y_true==0) & (y_pred==0)).sum())
    fn = int(((y_true==1) & (y_pred==0)).sum())
    print(f"\n[{name}]  n={n}")
    print("                pred=NOT_SCAM   pred=SCAM")
    print(f"  true=NOT_SCAM   {tn:>5d}            {fp:>5d}")
    print(f"  true=SCAM       {fn:>5d}            {tp:>5d}")
    if tp + fp > 0:
        print(f"  Precision (model says SCAM): {tp/(tp+fp):.3f}  ({tp}/{tp+fp})")
    if tp + fn > 0:
        print(f"  Recall    (true scams caught): {tp/(tp+fn):.3f}")
    acc = (tp + tn) / n
    print(f"  Accuracy: {acc:.3f}")

print()
print("=" * 72)
print("PRECISION BY STRATUM")
print("=" * 72)
for s in ['top50', 'high', 'mid', 'low']:
    sub = df[df['stratum']==s]
    n = len(sub)
    n_scam = (sub['true_label']=='scam').sum()
    n_unsure = (sub['true_label']=='unsure').sum()
    n_not = (sub['true_label']=='not_scam').sum()
    print(f"  {s:6s}  n={n}  scam={n_scam}  unsure={n_unsure}  not_scam={n_not}  "
          f"→ scam-rate (incl. unsure): {(n_scam+n_unsure)/n:.2%}")

print()
print("=" * 72)
print("PER-LF PRECISION (when this LF fired, what was the true label?)")
print("=" * 72)
print("'mean_true' uses scam=1, unsure=0.5, not_scam=0; lower=better for NOT_SCAM LFs.")

def lf_fires(name, lfs_str):
    if not isinstance(lfs_str, str): return False
    return f'{name}(' in lfs_str

def label_score(s):
    return 1.0 if s=='scam' else 0.5 if s=='unsure' else 0.0

df['true_score'] = df['true_label'].apply(label_score)

scam_lfs = ['zori_low','price_anomaly','low_price_floor','too_good_amenities',
            'contact_in_body','urgency_keywords']
notscam_lfs = ['zori_high','section8_income','student_housing','template_body',
               'long_detailed_body','weekly_rental','auto_template_body']

print("\nSCAM-leaning LFs (high mean_true = LF was correct):")
print(f"  {'LF':25s}  {'fired':>6s}  {'mean':>6s}  {'composition':<32s}")
for lf in scam_lfs:
    fires = df[df['lfs_fired'].apply(lambda s: lf_fires(lf, s))]
    if len(fires) == 0:
        print(f"  {lf:25s}  {0:>6d}  {'---':>6s}  (never fired in sample)")
        continue
    n = len(fires)
    mean_t = fires['true_score'].mean()
    nc = (fires['true_label']=='scam').sum()
    nu = (fires['true_label']=='unsure').sum()
    nn = (fires['true_label']=='not_scam').sum()
    print(f"  {lf:25s}  {n:>6d}  {mean_t:>6.3f}  scam={nc} unsure={nu} not_scam={nn}")

print("\nNOT_SCAM-leaning LFs (low mean_true = LF was correct):")
print(f"  {'LF':25s}  {'fired':>6s}  {'mean':>6s}  {'composition':<32s}")
for lf in notscam_lfs:
    fires = df[df['lfs_fired'].apply(lambda s: lf_fires(lf, s))]
    if len(fires) == 0:
        print(f"  {lf:25s}  {0:>6d}  {'---':>6s}  (never fired in sample)")
        continue
    n = len(fires)
    mean_t = fires['true_score'].mean()
    nc = (fires['true_label']=='scam').sum()
    nu = (fires['true_label']=='unsure').sum()
    nn = (fires['true_label']=='not_scam').sum()
    print(f"  {lf:25s}  {n:>6d}  {mean_t:>6.3f}  scam={nc} unsure={nu} not_scam={nn}")

print()
print("=" * 72)
print("CALIBRATION: model proba bin vs true scam rate")
print("=" * 72)
df['proba_bin'] = pd.cut(df['snorkel_proba_scam'], bins=[0, 0.2, 0.4, 0.6, 0.8, 1.0])
cal = df.groupby('proba_bin', observed=True).agg(
    n=('true_score','size'),
    mean_true=('true_score','mean'),
    n_scam=('true_label', lambda s: (s=='scam').sum()),
    n_unsure=('true_label', lambda s: (s=='unsure').sum()),
    n_not_scam=('true_label', lambda s: (s=='not_scam').sum()),
).round(3)
print(cal.to_string())
