"""Round 2 labeling sample: targeted at finding actual scams in atypical patterns."""
import re
import numpy as np
import pandas as pd

df = pd.read_parquet('df_with_snorkel.parquet')
SEED = 1337  # different seed from round 1
rng = np.random.default_rng(SEED)

# --- Recompute which LFs fired (subset) -----------------------------------
PHONE_RE = re.compile(r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b")
EMAIL_RE = re.compile(r"\b\S+@\S+\.\S+\b")
URGENCY = ['act fast','wire transfer','western union','moneygram','moving abroad','out of country','missionary','god bless','send deposit',"cashier's check"]

def has_contact(b):
    if not isinstance(b, str): return False
    return bool(PHONE_RE.search(b) or EMAIL_RE.search(b))

def has_urgency(t, b):
    text = (t if isinstance(t, str) else '') + ' ' + (b if isinstance(b, str) else '')
    return any(kw in text.lower() for kw in URGENCY)

df['_contact_in_body'] = df['body'].apply(has_contact)
df['_urgency'] = df.apply(lambda r: has_urgency(r['title'], r['body']), axis=1)

# --- Pools ----------------------------------------------------------------
# Exclude rows already labeled in round 1
labeled_r1 = pd.read_csv('labeling_sample.csv')
already_labeled = set(labeled_r1['orig_idx'].tolist())

available = df[~df.index.isin(already_labeled)].copy()
print(f"Pool after excluding round 1: {len(available):,}")

# Stratum 1: top-50 from NEW model (after range fix)
top_pool = available.nlargest(50, 'snorkel_proba_scam')

# Stratum 2: contact_in_body fires
contact_pool = available[available['_contact_in_body']]

# Stratum 3: urgency keywords fires
urgency_pool = available[available['_urgency']]

# Stratum 4: has_photo == 'No' AND high proba (>0.6)
nophoto_pool = available[(available['has_photo'] == 'No') & (available['snorkel_proba_scam'] > 0.6)]

# Stratum 5: RentLingo (model says ~0% scam — sanity check)
rentlingo_pool = available[available['source'] == 'RentLingo']

# Stratum 6: rare / long-tail sources (not the top 2)
rare_pool = available[~available['source'].isin(['RentDigs.com', 'RentLingo'])]

# Stratum 7: Mid-uncertainty (proba 0.45-0.55) — calibration check
midcal_pool = available[(available['snorkel_proba_scam'] >= 0.45) & (available['snorkel_proba_scam'] <= 0.55)]

picks = {
    'top_new':    rng.choice(top_pool.index, size=10, replace=False).tolist(),
    'contact':    rng.choice(contact_pool.index, size=min(5, len(contact_pool)), replace=False).tolist(),
    'urgency':    rng.choice(urgency_pool.index, size=min(5, len(urgency_pool)), replace=False).tolist(),
    'no_photo':   rng.choice(nophoto_pool.index, size=min(5, len(nophoto_pool)), replace=False).tolist(),
    'rentlingo':  rng.choice(rentlingo_pool.index, size=5, replace=False).tolist(),
    'rare_src':   rng.choice(rare_pool.index, size=5, replace=False).tolist(),
    'mid_cal':    rng.choice(midcal_pool.index, size=5, replace=False).tolist(),
}

print("Stratum sizes:")
for k,v in picks.items():
    print(f"  {k:12s}: {len(v)}")

# Build CSV (continue sample_id from round 1)
start_id = labeled_r1['sample_id'].max() + 1
rows = []
sid = start_id
for stratum, idxs in picks.items():
    for idx in idxs:
        r = df.loc[idx]
        rows.append({
            'sample_id': sid,
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
            'source': r['source'],
            'has_photo': r['has_photo'],
            'lfs_fired': '(computed in renderer)',
            'title': r['title'],
            'body': r['body'],
            'true_label': '',
            'note': '',
        })
        sid += 1

out = pd.DataFrame(rows)
out.to_csv('labeling_sample_r2.csv', index=False)
print(f"\nBuilt {len(out)} rows -> labeling_sample_r2.csv (sample_id {start_id} to {sid-1})")
