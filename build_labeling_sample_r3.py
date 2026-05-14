"""Round 3 sample: Hunter 1 candidates (free-form low-price, possibly real scams)."""
import re
import numpy as np
import pandas as pd

df = pd.read_parquet('df_with_snorkel.parquet')
SEED = 7777

# Already labeled
r1 = pd.read_csv('labeling_sample.csv')
r2 = pd.read_csv('labeling_sample_r2.csv')
already = set(r1['orig_idx']) | set(r2['orig_idx'])

df['_is_auto_template'] = df['body'].str.lower().fillna('').str.contains(
    'this unit is located at', regex=False) & df['body'].str.lower().fillna('').str.contains(
    'monthly rental rates range from', regex=False)
df['_body_len'] = df['body'].fillna('').str.len()

# Hunter 1: Free-form low-price
h1 = df[
    ~df['_is_auto_template'] &
    df['range_lo'].isna() &
    df['_body_len'].between(20, 250) &
    df['price_vs_zori_ratio'].notna() &
    (df['price_vs_zori_ratio'] < 0.5) &
    df['zori_granularity'].ne('none') &
    ~df.index.isin(already)
]
print(f"Hunter 1 candidates: {len(h1)}")

rng = np.random.default_rng(SEED)
picks = rng.choice(h1.index, size=min(15, len(h1)), replace=False).tolist()

start_id = max(r1['sample_id'].max(), r2['sample_id'].max()) + 1
rows = []
for i, idx in enumerate(picks):
    r = df.loc[idx]
    rows.append({
        'sample_id': start_id + i,
        'stratum': 'hunter_freeform_low',
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

out = pd.DataFrame(rows)
out.to_csv('labeling_sample_r3.csv', index=False)
print(f"Built {len(out)} rows -> labeling_sample_r3.csv (sample_id {start_id} to {start_id + len(picks) - 1})")
