"""Build a stratified hand-labeling sample for FakeOut.

Output: labeling_sample.csv with all fields needed for review + which LFs fired.
"""
import re
import numpy as np
import pandas as pd

df = pd.read_parquet('df_with_snorkel.parquet')
SEED = 42
rng = np.random.default_rng(SEED)

# --- Recompute which LFs fired (boolean per row, per LF) -------------------
def lf_zori_low(r):       return r['zori_granularity'] != 'none' and bool(r['zori_anomaly_low'])
def lf_zori_high(r):      return r['zori_granularity'] != 'none' and bool(r['zori_anomaly_high'])
def lf_price_anomaly(r):
    if not r['is_price_anomaly']: return False
    rt = r['price_vs_zori_ratio']
    return (pd.notna(rt) and rt < 1) or pd.isna(rt)
def lf_low_price_floor(r):
    return pd.notna(r['price']) and pd.notna(r['square_feet']) and r['price'] < 300 and r['square_feet'] > 200
def lf_too_good_amenities(r):
    if pd.isna(r['amenity_count']) or r['amenity_count'] < 8: return False
    rt = r['price_vs_zori_ratio']
    return bool(r['zori_anomaly_low']) or (pd.notna(rt) and rt < 0.7)
PHONE_RE = re.compile(r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b")
EMAIL_RE = re.compile(r"\b\S+@\S+\.\S+\b")
def lf_contact_in_body(r):
    b = r['body'] if isinstance(r['body'], str) else ''
    return bool(PHONE_RE.search(b) or EMAIL_RE.search(b))
URGENCY = ['act fast','wire transfer','western union','moneygram','moving abroad','out of country','missionary','god bless','send deposit',"cashier's check"]
def lf_urgency_keywords(r):
    t = (r['title'] if isinstance(r['title'], str) else '').lower()
    b = (r['body']  if isinstance(r['body'],  str) else '').lower()
    return any(kw in t+' '+b for kw in URGENCY)
SECTION8 = ['section 8','section8','gosection8','income restriction','income restricted','income-based','income based','hud','income limit','income-restricted']
def lf_section8_income(r):
    b = (r['body'] if isinstance(r['body'], str) else '').lower()
    return any(t in b for t in SECTION8)
STUDENT = ['student housing','student community','near campus','off-campus','off campus','near university','university of','student living','student apartment','student apartments','college students']
def lf_student_housing(r):
    t = (r['title'] if isinstance(r['title'], str) else '').lower()
    b = (r['body']  if isinstance(r['body'],  str) else '').lower()
    return any(term in t+' '+b for term in STUDENT)
# Body template: precompute counts
body_counts = df['body'].value_counts(dropna=True)
body_count_map = df['body'].map(body_counts).fillna(0).astype(int)
def lf_template_body(r): return body_count_map.loc[r.name] >= 5
def lf_long_detailed_body(r):
    bl = len(r['body']) if isinstance(r['body'], str) else 0
    return bl > 500 and pd.notna(r['amenity_count']) and r['amenity_count'] >= 3
WEEKLY = ['extended stay','extended-stay','weekly &','weekly and monthly','monthly &','per week','weekly rent','weekly rate','corporate housing']
def lf_weekly_rental(r):
    t = (r['title'] if isinstance(r['title'], str) else '').lower()
    b = (r['body']  if isinstance(r['body'],  str) else '').lower()
    return any(kw in t+' '+b for kw in WEEKLY)
def lf_auto_template_body(r):
    b = (r['body'] if isinstance(r['body'], str) else '').lower()
    return 'this unit is located at' in b and 'monthly rental rates range from' in b

LFS = {
    'zori_low': (lf_zori_low, 'SCAM'),
    'zori_high': (lf_zori_high, 'NOT_SCAM'),
    'price_anomaly': (lf_price_anomaly, 'SCAM'),
    'low_price_floor': (lf_low_price_floor, 'SCAM'),
    'too_good_amenities': (lf_too_good_amenities, 'SCAM'),
    'contact_in_body': (lf_contact_in_body, 'SCAM'),
    'urgency_keywords': (lf_urgency_keywords, 'SCAM'),
    'section8_income': (lf_section8_income, 'NOT_SCAM'),
    'student_housing': (lf_student_housing, 'NOT_SCAM'),
    'template_body': (lf_template_body, 'NOT_SCAM'),
    'long_detailed_body': (lf_long_detailed_body, 'NOT_SCAM'),
    'weekly_rental': (lf_weekly_rental, 'NOT_SCAM'),
    'auto_template_body': (lf_auto_template_body, 'NOT_SCAM'),
}

def fired_lfs(r):
    out = []
    for name, (fn, vote) in LFS.items():
        try:
            if fn(r): out.append(f"{name}({vote})")
        except Exception:
            pass
    return '; '.join(out) if out else '(none)'

# --- Stratified sample -----------------------------------------------------
top50_idx = df.nlargest(50, 'snorkel_proba_scam').index.tolist()
high_pool = df[(df['snorkel_proba_scam'] > 0.7) & ~df.index.isin(top50_idx)]
mid_pool  = df[(df['snorkel_proba_scam'] >= 0.3) & (df['snorkel_proba_scam'] <= 0.7)]
low_pool  = df[df['snorkel_proba_scam'] < 0.3]

picks = {
    'top50':  rng.choice(top50_idx, size=15, replace=False).tolist(),
    'high':   rng.choice(high_pool.index, size=10, replace=False).tolist(),
    'mid':    rng.choice(mid_pool.index,  size=15, replace=False).tolist(),
    'low':    rng.choice(low_pool.index,  size=10, replace=False).tolist(),
}

rows = []
for stratum, idxs in picks.items():
    for idx in idxs:
        r = df.loc[idx]
        rows.append({
            'sample_id': len(rows) + 1,
            'stratum': stratum,
            'orig_idx': idx,
            'cityname': r['cityname'],
            'state': r['state'],
            'price': r['price'],
            'square_feet': r['square_feet'],
            'bedrooms': r['bedrooms'],
            'bathrooms': r['bathrooms'],
            'amenity_count': r['amenity_count'],
            'price_vs_zori_ratio': r['price_vs_zori_ratio'],
            'snorkel_proba_scam': r['snorkel_proba_scam'],
            'snorkel_label': r['snorkel_label'],
            'lfs_fired': fired_lfs(r),
            'title': r['title'],
            'body': r['body'],
            'true_label': '',
            'note': '',
        })

out = pd.DataFrame(rows)
out.to_csv('labeling_sample.csv', index=False)
print(f"Built {len(out)} labeling rows -> labeling_sample.csv")
print(f"Stratum sizes: " + ", ".join(f"{k}={len(v)}" for k,v in picks.items()))
