"""Render a labeling batch as markdown for human review — with full ZORI + city context."""
import sys
from pathlib import Path
import pandas as pd
import numpy as np

if len(sys.argv) < 2:
    print("usage: render_batch.py <batch_num>  (1=rows 1-10, 2=rows 11-20, ...)")
    sys.exit(1)

batch = int(sys.argv[1])
start = (batch - 1) * 10 + 1
end = batch * 10

ROOT = Path('/Users/dressi/Desktop/github/FakeOut')
sample = pd.read_csv(ROOT / 'labeling_sample.csv')
batch_df = sample[(sample['sample_id'] >= start) & (sample['sample_id'] <= end)]

# Load full df once for ZORI fields + city context
full = pd.read_parquet(ROOT / 'df_with_snorkel.parquet')

# Per-city stats (median listing price, count of listings, median price/sqft)
city_stats = full.groupby('cityname').agg(
    n_listings=('price', 'size'),
    median_price=('price', 'median'),
    median_psf=('price_per_sqft', 'median'),
).round(2)

out_path = ROOT / f'labeling/batch_{batch:02d}.md'
out_path.parent.mkdir(exist_ok=True)

lines = [f"# Labeling batch {batch} — rows {start}-{end}\n\n"]
lines.append("Open this file, read each listing, then come back to chat with overrides.\n")
lines.append("Format: `1=scam, 4=unsure, 7=scam` (silence on a row = accept proposed label)\n\n---\n\n")

for _, r in batch_df.iterrows():
    fr = full.loc[r['orig_idx']]
    body = r['body'] if isinstance(r['body'], str) else '(no body)'
    title = r['title'] if isinstance(r['title'], str) else '(no title)'

    # ZORI baseline + provenance
    zori_b = fr.get('zori_baseline')
    zori_b_str = f"\\${zori_b:.0f}/mo" if pd.notna(zori_b) else "N/A"
    zori_gran = fr.get('zori_granularity')
    zori_n = fr.get('zori_n_neighbors_used')
    zori_dist = fr.get('zori_neighbor_median_distance_km')
    zori_month = fr.get('zori_month')
    zori_zip = fr.get('assigned_zip')

    if zori_gran == 'zip':
        zori_src = f"direct ZIP match ({zori_zip})"
    elif zori_gran == 'spatial':
        zori_src = (f"spatial k-NN, {int(zori_n) if pd.notna(zori_n) else '?'} neighbors at "
                    f"~{zori_dist:.1f}km from ZIP {zori_zip}")
    else:
        zori_src = "no baseline (AK/HI/PR or rural)"

    ratio = r['price_vs_zori_ratio']
    ratio_str = f"{ratio:.3f}" if pd.notna(ratio) else "N/A"
    zscore = fr.get('price_zori_zscore')
    zscore_str = f"{zscore:.2f}" if pd.notna(zscore) else "N/A (group too small)"

    # City context
    city = r['cityname']
    if city in city_stats.index:
        cs = city_stats.loc[city]
        city_str = (f"**City context** ({city}, {r['state']}): {int(cs['n_listings']):,} listings  "
                    f"|  city median price: \\${cs['median_price']:.0f}/mo  "
                    f"|  city median \\$/sqft: \\${cs['median_psf']:.2f}")
    else:
        city_str = f"**City context** ({city}, {r['state']}): not in summary stats"

    # Per-bedroom + price/sqft
    pb = r['price'] / r['bedrooms'] if pd.notna(r['bedrooms']) and r['bedrooms'] > 0 else None
    psf = fr.get('price_per_sqft')
    pb_str = f"\\${pb:.0f}/BR" if pb else "(studio or N/A)"
    psf_str = f"\\${psf:.2f}/sqft" if pd.notna(psf) else "N/A"

    lines.append(f"## Row {r['sample_id']}  —  stratum: `{r['stratum']}`\n\n")
    lines.append(f"### Listing\n")
    lines.append(f"- **Location**: {city}, {r['state']}  (ZIP {zori_zip})\n")
    lines.append(f"- **Listed price**: \\${r['price']:.0f}/mo\n")
    lines.append(f"- **Size / layout**: {r['square_feet']} sqft  |  {r['bedrooms']} BR  |  {r['bathrooms']} BA\n")
    lines.append(f"- **Per-bedroom**: {pb_str}  |  **Per-sqft**: {psf_str}\n")
    lines.append(f"- **Amenities count**: {r['amenity_count']}\n")
    lines.append(f"- **Listing date**: {fr.get('listing_dt')}\n\n")

    lines.append(f"### Market context\n")
    lines.append(f"- **ZORI baseline for this ZIP+month** ({zori_month}): {zori_b_str}\n")
    lines.append(f"- **ZORI source**: {zori_src}\n")
    lines.append(f"- **price / ZORI baseline**: {ratio_str}  ⇒  listing is at {ratio*100:.0f}% of market\n" if pd.notna(ratio) else f"- **price / ZORI baseline**: N/A\n")
    lines.append(f"- **z-score within ZIP+month**: {zscore_str}\n")
    lines.append(f"- {city_str}\n\n")

    lines.append(f"### Model verdict\n")
    lines.append(f"- **Snorkel P(SCAM)**: {r['snorkel_proba_scam']:.4f}  "
                 f"({'SCAM' if r['snorkel_label']==1 else 'NOT_SCAM' if r['snorkel_label']==0 else 'ABSTAIN'})\n")
    lines.append(f"- **LFs that fired**: {r['lfs_fired']}\n\n")

    lines.append(f"### Title\n> {title}\n\n")
    lines.append(f"### Body (full)\n```\n{body}\n```\n\n")
    lines.append("---\n\n")

out_path.write_text(''.join(lines))
print(f"Wrote {out_path}")
