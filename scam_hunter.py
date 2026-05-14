"""Targeted scam hunters: surface candidates more likely to be actual scams."""
import re
from collections import Counter
import pandas as pd
import numpy as np

df = pd.read_parquet('df_with_snorkel.parquet')
print(f"Loaded {len(df):,} rows, sources: {df['source'].nunique()}")

# Pre-load already-labeled
r1 = pd.read_csv('labeling_sample.csv')
r2 = pd.read_csv('labeling_sample_r2.csv')
already = set(r1['orig_idx']) | set(r2['orig_idx'])
print(f"Already labeled: {len(already)}\n")

# Auto-template detection (re-derive)
df['_is_auto_template'] = df['body'].str.lower().fillna('').str.contains(
    'this unit is located at', regex=False) & df['body'].str.lower().fillna('').str.contains(
    'monthly rental rates range from', regex=False)

df['_body_len'] = df['body'].fillna('').str.len()

# ============================================================
# HUNTER 1: Free-form low-price
# ============================================================
print("=" * 70)
print("HUNTER 1: Free-form low-price (user-written bait pattern)")
print("=" * 70)
h1 = df[
    ~df['_is_auto_template'] &
    df['range_lo'].isna() &
    (df['_body_len'].between(20, 250)) &
    df['price_vs_zori_ratio'].notna() &
    (df['price_vs_zori_ratio'] < 0.5) &
    df['zori_granularity'].ne('none') &
    ~df.index.isin(already)
]
print(f"Candidates: {len(h1):,}")
print(f"Sources: {h1['source'].value_counts().to_dict()}")
if len(h1) > 0:
    print("\nSample (5 random):")
    for _, r in h1.sample(min(5, len(h1)), random_state=42).iterrows():
        body = (r['body'] or '')[:200].replace('\n',' ')
        print(f"  [{r['cityname']:20s}] ${r['price']:.0f}/{r['square_feet']:.0f}sqft  ratio={r['price_vs_zori_ratio']:.3f}")
        print(f"    TITLE: {r['title']}")
        print(f"    BODY:  {body}")

# ============================================================
# HUNTER 2: Cross-city body reuse (stolen description)
# ============================================================
print("\n" + "=" * 70)
print("HUNTER 2: Same body text in DIFFERENT cities (stolen description)")
print("=" * 70)
# Group by body, count distinct cities
body_city = df.dropna(subset=['body']).groupby('body').agg(
    n_listings=('cityname','size'),
    n_cities=('cityname','nunique'),
    cities=('cityname', lambda s: list(s.unique())[:5]),
).reset_index()

# Sweet spot: appears in 2-5 different cities (not aggregator-spam, but reused)
suspicious_bodies = body_city[
    (body_city['n_cities'].between(2, 5)) &
    (body_city['n_listings'].between(2, 10))  # not 50x
]
print(f"Bodies appearing in 2-5 different cities (2-10 listings): {len(suspicious_bodies):,}")

if len(suspicious_bodies) > 0:
    # Map back to listings
    h2_idx = df[df['body'].isin(suspicious_bodies['body'])].index
    h2 = df.loc[h2_idx]
    h2 = h2[~h2.index.isin(already)]
    print(f"Candidate listings: {len(h2):,}")
    if len(h2) > 0:
        print("\nSample (3 unique bodies, showing all city instances):")
        for body_text in suspicious_bodies.sample(min(3, len(suspicious_bodies)), random_state=42)['body']:
            instances = h2[h2['body']==body_text].head(3)
            print(f"\n  Body (truncated): {(body_text or '')[:150]}...")
            for _, r in instances.iterrows():
                print(f"    [{r['cityname']}, {r['state']}] ${r['price']:.0f} src={r['source']}")

# ============================================================
# HUNTER 3: Phone numbers across cities
# ============================================================
print("\n" + "=" * 70)
print("HUNTER 3: Phone numbers appearing in multiple cities (scaled scammer)")
print("=" * 70)
PHONE_RE = re.compile(r'\b(\d{3}[-.\s]?\d{3}[-.\s]?\d{4})\b')

def extract_phones(body):
    if not isinstance(body, str): return []
    return [m.replace('-','').replace('.','').replace(' ','') for m in PHONE_RE.findall(body)]

df['_phones'] = df['body'].apply(extract_phones)
phone_to_rows = {}
for idx, phones in df['_phones'].items():
    for p in phones:
        phone_to_rows.setdefault(p, []).append(idx)

# Phones appearing in >= 3 listings across >= 2 cities
suspicious_phones = []
for phone, rows in phone_to_rows.items():
    if len(rows) >= 3:
        cities = df.loc[rows, 'cityname'].nunique()
        if cities >= 2:
            suspicious_phones.append((phone, len(rows), cities, rows))

print(f"Phones in >=3 listings across >=2 cities: {len(suspicious_phones)}")
if suspicious_phones:
    print("\nTop 10 by listing count:")
    for phone, n, cities, rows in sorted(suspicious_phones, key=lambda x: -x[1])[:10]:
        sample = df.loc[rows[:3]]
        city_list = sample[['cityname','state','price']].to_dict('records')
        print(f"  {phone}: {n} listings across {cities} cities")
        for r in city_list:
            print(f"    {r['cityname']}, {r['state']}  ${r['price']:.0f}")

    # Get listing indices not yet labeled
    h3_idx = []
    for _, _, _, rows in suspicious_phones:
        h3_idx.extend(rows)
    h3 = df.loc[list(set(h3_idx))]
    h3 = h3[~h3.index.isin(already)]
    print(f"\nUnique candidate listings: {len(h3):,}")
