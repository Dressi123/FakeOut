"""Render labeling batch from round 2 sample with updated LFs."""
import sys
import re
from pathlib import Path
import pandas as pd
import numpy as np

if len(sys.argv) < 2:
    print("usage: render_batch_r2.py <batch_num>  (1=rows 51-60, 2=rows 61-70, ...)")
    sys.exit(1)

batch = int(sys.argv[1])
start = 50 + (batch - 1) * 10 + 1
end = 50 + batch * 10

ROOT = Path('/Users/dressi/Desktop/github/FakeOut')
sample = pd.read_csv(ROOT / 'labeling_sample_r2.csv')
batch_df = sample[(sample['sample_id'] >= start) & (sample['sample_id'] <= end)]
full = pd.read_parquet(ROOT / 'df_with_snorkel.parquet')

# Per-city stats
city_stats = full.groupby('cityname').agg(
    n_listings=('price', 'size'),
    median_price=('price', 'median'),
    median_psf=('price_per_sqft', 'median'),
).round(2)

# --- Updated LF firing detection (matches the new notebook LFs) ---
PHONE_RE = re.compile(r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b")
EMAIL_RE = re.compile(r"\b\S+@\S+\.\S+\b")
URGENCY = ['act fast','wire transfer','western union','moneygram','moving abroad','out of country','missionary','god bless','send deposit',"cashier's check"]
SECTION8 = ['section 8','section8','gosection8','income restriction','income restricted','income-based','income based','hud','income limit','income-restricted']
STUDENT = ['student housing','student community','near campus','off-campus','off campus','near university','university of','student living','student apartment','student apartments','college students']
WEEKLY = ['extended stay','extended-stay','weekly &','weekly and monthly','monthly &','per week','weekly rent','weekly rate','corporate housing']

body_counts = full['body'].value_counts(dropna=True)

def fired(r, fr):
    out = []
    body = (fr['body'] if isinstance(fr['body'], str) else '')
    title = (fr['title'] if isinstance(fr['title'], str) else '')
    has_unbounded = bool(fr.get('has_unbounded_range', False))

    # SCAM-leaning (with abstain on unbounded range)
    if fr['zori_granularity'] != 'none' and not has_unbounded and bool(fr.get('zori_anomaly_low')):
        out.append('zori_low(SCAM)')
    if bool(fr.get('is_price_anomaly')) and not has_unbounded:
        rt = fr.get('price_vs_zori_ratio')
        if (pd.notna(rt) and rt < 1) or pd.isna(rt):
            out.append('price_anomaly(SCAM)')
    if not has_unbounded:
        if pd.notna(fr.get('price')) and pd.notna(fr.get('square_feet')):
            if fr['price'] < 300 and fr['square_feet'] > 200:
                out.append('low_price_floor(SCAM)')
    if pd.notna(fr.get('amenity_count')) and fr['amenity_count'] >= 8 and not has_unbounded:
        rt = fr.get('price_vs_zori_ratio')
        if bool(fr.get('zori_anomaly_low')) or (pd.notna(rt) and rt < 0.7):
            out.append('too_good_amenities(SCAM)')
    if PHONE_RE.search(body) or EMAIL_RE.search(body):
        out.append('contact_in_body(SCAM)')
    if any(kw in (title+' '+body).lower() for kw in URGENCY):
        out.append('urgency_keywords(SCAM)')

    # NOT_SCAM-leaning
    if fr['zori_granularity'] != 'none' and bool(fr.get('zori_anomaly_high')):
        out.append('zori_high(NOT_SCAM)')
    if any(t in body.lower() for t in SECTION8):
        out.append('section8_income(NOT_SCAM)')
    if any(t in (title+' '+body).lower() for t in STUDENT):
        out.append('student_housing(NOT_SCAM)')
    if body_counts.get(fr['body'], 0) >= 5:
        out.append('template_body(NOT_SCAM)')
    if len(body) > 500 and pd.notna(fr.get('amenity_count')) and fr['amenity_count'] >= 3:
        out.append('long_detailed_body(NOT_SCAM)')
    if any(t in (title+' '+body).lower() for t in WEEKLY):
        out.append('weekly_rental(NOT_SCAM)')
    if 'this unit is located at' in body.lower() and 'monthly rental rates range from' in body.lower():
        out.append('auto_template_body(NOT_SCAM)')
    if pd.notna(fr.get('range_lo')):
        out.append('explicit_price_range(NOT_SCAM)')
    return '; '.join(out) if out else '(none)'

out_path = ROOT / f'labeling/batch_r2_{batch:02d}.md'
out_path.parent.mkdir(exist_ok=True)

lines = [f"# Labeling batch (round 2) {batch} — rows {start}-{end}\n\n"]
lines.append("Reply format: `52=scam, 55=unsure` (silence on a row = accept proposed label)\n\n---\n\n")

for _, r in batch_df.iterrows():
    fr = full.loc[r['orig_idx']]
    body = r['body'] if isinstance(r['body'], str) else '(no body)'
    title = r['title'] if isinstance(r['title'], str) else '(no title)'

    zori_b = fr.get('zori_baseline')
    zori_b_str = f"\\${zori_b:.0f}/mo" if pd.notna(zori_b) else "N/A"
    zori_gran = fr.get('zori_granularity')
    if zori_gran == 'zip':
        zori_src = f"direct ZIP match ({fr.get('assigned_zip')})"
    elif zori_gran == 'spatial':
        zori_src = f"spatial k-NN, {int(fr.get('zori_n_neighbors_used'))} neighbors at ~{fr.get('zori_neighbor_median_distance_km'):.1f}km"
    else:
        zori_src = "no baseline"

    ratio = r['price_vs_zori_ratio']
    ratio_str = f"{ratio:.3f}" if pd.notna(ratio) else "N/A"

    range_lo = fr.get('range_lo')
    range_hi = fr.get('range_hi')
    has_unbounded = bool(fr.get('has_unbounded_range', False))
    eff_price = fr.get('effective_price')
    if pd.notna(range_hi):
        range_str = f"explicit \\${range_lo:.0f}-\\${range_hi:.0f} → effective price = \\${eff_price:.0f}"
    elif has_unbounded:
        range_str = f"floor-only `range from \\${range_lo:.0f}` → SCAM LFs ABSTAIN"
    else:
        range_str = "no range pattern detected"

    city = r['cityname']
    if city in city_stats.index:
        cs = city_stats.loc[city]
        city_str = (f"{int(cs['n_listings']):,} listings  |  median \\${cs['median_price']:.0f}/mo  "
                    f"|  median \\${cs['median_psf']:.2f}/sqft")
    else:
        city_str = "no stats"

    pb = r['price'] / r['bedrooms'] if pd.notna(r['bedrooms']) and r['bedrooms'] > 0 else None
    psf = fr.get('price_per_sqft')

    lines.append(f"## Row {r['sample_id']}  —  stratum: `{r['stratum']}`\n\n")
    lines.append(f"### Listing\n")
    lines.append(f"- **Location**: {city}, {r['state']}  (ZIP {fr.get('assigned_zip')})\n")
    lines.append(f"- **Listed price**: \\${r['price']:.0f}/mo  |  **Effective price**: \\${eff_price:.0f}/mo\n")
    lines.append(f"- **Range pattern**: {range_str}\n")
    lines.append(f"- **Size / layout**: {r['square_feet']} sqft  |  {r['bedrooms']} BR  |  {r['bathrooms']} BA\n")
    lines.append(f"- **Per-bedroom**: " + (f"\\${pb:.0f}/BR" if pb else "(studio/N/A)") + f"  |  **Per-sqft**: " + (f"\\${psf:.2f}" if pd.notna(psf) else "N/A") + "\n")
    lines.append(f"- **Amenities count**: {r['amenity_count']}  |  **Has photo**: {r['has_photo']}  |  **Source**: {r['source']}\n")
    lines.append(f"- **Listing date**: {fr.get('listing_dt')}\n\n")

    lines.append(f"### Market context\n")
    lines.append(f"- **ZORI baseline** ({fr.get('zori_month')}): {zori_b_str}  ({zori_src})\n")
    lines.append(f"- **Effective / ZORI ratio**: {ratio_str}\n")
    lines.append(f"- **City** ({city}, {r['state']}): {city_str}\n\n")

    lines.append(f"### Model verdict\n")
    lines.append(f"- **Snorkel P(SCAM)**: {r['snorkel_proba_scam']:.4f}  ({['NOT_SCAM','SCAM','ABSTAIN'][int(r['snorkel_label']) if r['snorkel_label'] in (0,1) else 2]})\n")
    lines.append(f"- **LFs that fired**: {fired(r, fr)}\n\n")

    lines.append(f"### Title\n> {title}\n\n")
    lines.append(f"### Body (full)\n```\n{body}\n```\n\n")
    lines.append("---\n\n")

out_path.write_text(''.join(lines))
print(f"Wrote {out_path}")
