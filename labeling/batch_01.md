# Labeling batch 1 — rows 1-10

Open this file, read each listing, then come back to chat with overrides.
Format: `1=scam, 4=unsure, 7=scam` (silence on a row = accept proposed label)

---

## Row 1  —  stratum: `top50`

### Listing
- **Location**: Glen Burnie, MD  (ZIP 21061)
- **Listed price**: \$1028/mo
- **Size / layout**: 542 sqft  |  1.0 BR  |  1.0 BA
- **Per-bedroom**: \$1028/BR  |  **Per-sqft**: \$1.90/sqft
- **Amenities count**: 4
- **Listing date**: 2019-12-26 11:22:39

### Market context
- **ZORI baseline for this ZIP+month** (2019-12-31): \$1802/mo
- **ZORI source**: spatial k-NN, 3 neighbors at ~11.5km from ZIP 21061
- **price / ZORI baseline**: 0.571  ⇒  listing is at 57% of market
- **z-score within ZIP+month**: N/A (group too small)
- **City context** (Glen Burnie, MD): 177 listings  |  city median price: \$1205/mo  |  city median \$/sqft: \$1.49

### Model verdict
- **Snorkel P(SCAM)**: 1.0000  (SCAM)
- **LFs that fired**: zori_low(SCAM); price_anomaly(SCAM); auto_template_body(NOT_SCAM)

### Title
> One BR 362 Klagg Ct

### Body (full)
```
This unit is located at 362 Klagg Ct, Glen Burnie, 21061, MDMonthly rental rates range from $1028 - $1608We have one - three beds units available for rent
```

---

## Row 2  —  stratum: `top50`

### Listing
- **Location**: Spring Hill, FL  (ZIP 34608)
- **Listed price**: \$600/mo
- **Size / layout**: 250 sqft  |  1.0 BR  |  1.0 BA
- **Per-bedroom**: \$600/BR  |  **Per-sqft**: \$2.40/sqft
- **Amenities count**: 1
- **Listing date**: 2019-12-26 11:15:40

### Market context
- **ZORI baseline for this ZIP+month** (2019-12-31): \$1319/mo
- **ZORI source**: spatial k-NN, 1 neighbors at ~3.9km from ZIP 34608
- **price / ZORI baseline**: 0.455  ⇒  listing is at 45% of market
- **z-score within ZIP+month**: N/A (group too small)
- **City context** (Spring Hill, FL): 26 listings  |  city median price: \$1050/mo  |  city median \$/sqft: \$0.92

### Model verdict
- **Snorkel P(SCAM)**: 1.0000  (SCAM)
- **LFs that fired**: zori_low(SCAM); price_anomaly(SCAM); auto_template_body(NOT_SCAM)

### Title
> One BR Bishop Road

### Body (full)
```
This unit is located at Bishop Road, Spring Hill, 34608, FLMonthly rental rates range from $600We have 1 beds units available for rent Apartment features include:-- Furnished- Pool
```

---

## Row 3  —  stratum: `top50`

### Listing
- **Location**: Fort Collins, CO  (ZIP 80527)
- **Listed price**: \$785/mo
- **Size / layout**: 250 sqft  |  1.0 BR  |  1.0 BA
- **Per-bedroom**: \$785/BR  |  **Per-sqft**: \$3.14/sqft
- **Amenities count**: 0
- **Listing date**: 2019-12-26 11:15:30

### Market context
- **ZORI baseline for this ZIP+month** (2019-12-31): \$1434/mo
- **ZORI source**: spatial k-NN, 4 neighbors at ~3.3km from ZIP 80527
- **price / ZORI baseline**: 0.548  ⇒  listing is at 55% of market
- **z-score within ZIP+month**: N/A (group too small)
- **City context** (Fort Collins, CO): 343 listings  |  city median price: \$1429/mo  |  city median \$/sqft: \$1.59

### Model verdict
- **Snorkel P(SCAM)**: 1.0000  (SCAM)
- **LFs that fired**: zori_low(SCAM); price_anomaly(SCAM); auto_template_body(NOT_SCAM)

### Title
> One BR Finch Ct

### Body (full)
```
This unit is located at Finch Ct, Fort Collins, 80525, COMonthly rental rates range from $785We have 1 beds units available for rent Apartment features include:-- Furnished
```

---

## Row 4  —  stratum: `top50`

### Listing
- **Location**: Concord, CA  (ZIP 94519)
- **Listed price**: \$930/mo
- **Size / layout**: 250 sqft  |  1.0 BR  |  1.0 BA
- **Per-bedroom**: \$930/BR  |  **Per-sqft**: \$3.72/sqft
- **Amenities count**: 0
- **Listing date**: 2019-12-22 11:45:46

### Market context
- **ZORI baseline for this ZIP+month** (2019-12-31): \$2202/mo
- **ZORI source**: spatial k-NN, 5 neighbors at ~5.6km from ZIP 94519
- **price / ZORI baseline**: 0.422  ⇒  listing is at 42% of market
- **z-score within ZIP+month**: N/A (group too small)
- **City context** (Concord, CA): 133 listings  |  city median price: \$1275/mo  |  city median \$/sqft: \$1.15

### Model verdict
- **Snorkel P(SCAM)**: 1.0000  (SCAM)
- **LFs that fired**: zori_low(SCAM); price_anomaly(SCAM); auto_template_body(NOT_SCAM)

### Title
> One BR Torino Court

### Body (full)
```
This unit is located at Torino Court, Concord, 94518, CAMonthly rental rates range from $930We have 1 beds units available for rent Apartment available amenities:-- Furnished
```

---

## Row 5  —  stratum: `top50`

### Listing
- **Location**: Lorton, VA  (ZIP 22079)
- **Listed price**: \$850/mo
- **Size / layout**: 250 sqft  |  1.0 BR  |  1.0 BA
- **Per-bedroom**: \$850/BR  |  **Per-sqft**: \$3.40/sqft
- **Amenities count**: 1
- **Listing date**: 2019-12-26 11:20:51

### Market context
- **ZORI baseline for this ZIP+month** (2019-12-31): \$1729/mo
- **ZORI source**: direct ZIP match (22079)
- **price / ZORI baseline**: 0.492  ⇒  listing is at 49% of market
- **z-score within ZIP+month**: N/A (group too small)
- **City context** (Lorton, VA): 28 listings  |  city median price: \$1842/mo  |  city median \$/sqft: \$1.79

### Model verdict
- **Snorkel P(SCAM)**: 1.0000  (SCAM)
- **LFs that fired**: zori_low(SCAM); price_anomaly(SCAM); auto_template_body(NOT_SCAM)

### Title
> One BR Duck Hawk Way

### Body (full)
```
This unit is located at Duck Hawk Way, Lorton, 22079, VAMonthly rental rates range from $850We have 1 beds units available for rent Apartment features include:-- Pool- Furnished
```

---

## Row 6  —  stratum: `top50`

### Listing
- **Location**: Bloomington, IN  (ZIP 47426)
- **Listed price**: \$550/mo
- **Size / layout**: 470 sqft  |  3.0 BR  |  1.0 BA
- **Per-bedroom**: \$183/BR  |  **Per-sqft**: \$1.17/sqft
- **Amenities count**: 4
- **Listing date**: 2019-12-26 11:17:26

### Market context
- **ZORI baseline for this ZIP+month** (2019-12-31): \$1118/mo
- **ZORI source**: spatial k-NN, 1 neighbors at ~3.1km from ZIP 47426
- **price / ZORI baseline**: 0.492  ⇒  listing is at 49% of market
- **z-score within ZIP+month**: N/A (group too small)
- **City context** (Bloomington, IN): 84 listings  |  city median price: \$985/mo  |  city median \$/sqft: \$1.32

### Model verdict
- **Snorkel P(SCAM)**: 1.0000  (SCAM)
- **LFs that fired**: zori_low(SCAM); auto_template_body(NOT_SCAM)

### Title
> Studio apartment 2663 E. 7th Street

### Body (full)
```
This unit is located at 2663 E. seventh Street, Bloomington, 47408, INMonthly rental rates range from $550 - $970We have studio - 3 beds units available for rent Apartment features include:-- Trash Removal Included- Refrigerator- Balcony, Deck, Patio- On-Site Laundry- Fitness facilities- Furnished- Water Included- On Bus Line
```

---

## Row 7  —  stratum: `top50`

### Listing
- **Location**: Marina Del Rey, CA  (ZIP 90292)
- **Listed price**: \$1600/mo
- **Size / layout**: 250 sqft  |  1.0 BR  |  1.0 BA
- **Per-bedroom**: \$1600/BR  |  **Per-sqft**: \$6.40/sqft
- **Amenities count**: 1
- **Listing date**: 2019-12-14 11:14:08

### Market context
- **ZORI baseline for this ZIP+month** (2019-12-31): \$3211/mo
- **ZORI source**: direct ZIP match (90292)
- **price / ZORI baseline**: 0.498  ⇒  listing is at 50% of market
- **z-score within ZIP+month**: N/A (group too small)
- **City context** (Marina Del Rey, CA): 90 listings  |  city median price: \$2985/mo  |  city median \$/sqft: \$3.67

### Model verdict
- **Snorkel P(SCAM)**: 1.0000  (SCAM)
- **LFs that fired**: zori_low(SCAM); price_anomaly(SCAM); auto_template_body(NOT_SCAM)

### Title
> One BR Via Marina

### Body (full)
```
This unit is located at Via Marina, Marina Del Rey, 90292, CAMonthly rental rates range from $1600We have 1 beds units available for rent Apartment available amenities:-- Pool- Furnished
```

---

## Row 8  —  stratum: `top50`

### Listing
- **Location**: Meridian, ID  (ZIP 83642)
- **Listed price**: \$646/mo
- **Size / layout**: 656 sqft  |  1.0 BR  |  1.0 BA
- **Per-bedroom**: \$646/BR  |  **Per-sqft**: \$0.98/sqft
- **Amenities count**: 3
- **Listing date**: 2019-12-26 11:18:52

### Market context
- **ZORI baseline for this ZIP+month** (2019-12-31): \$1297/mo
- **ZORI source**: direct ZIP match (83642)
- **price / ZORI baseline**: 0.498  ⇒  listing is at 50% of market
- **z-score within ZIP+month**: N/A (group too small)
- **City context** (Meridian, ID): 11 listings  |  city median price: \$1195/mo  |  city median \$/sqft: \$1.14

### Model verdict
- **Snorkel P(SCAM)**: 1.0000  (SCAM)
- **LFs that fired**: zori_low(SCAM); auto_template_body(NOT_SCAM)

### Title
> One BR 1103 W. Pine Avenue

### Body (full)
```
This unit is located at 1103 W. Pine Avenue, Meridian, 83642, IDMonthly rental rates range from $646We have 1 beds units available for rent Apartment features include:-- Dishwasher- Balcony, Deck, Patio- On-Site Laundry- Air conditioned- Sheltered parking- Business facility- Fitness facilities
```

---

## Row 9  —  stratum: `top50`

### Listing
- **Location**: Woodbridge, VA  (ZIP 22193)
- **Listed price**: \$850/mo
- **Size / layout**: 250 sqft  |  1.0 BR  |  1.0 BA
- **Per-bedroom**: \$850/BR  |  **Per-sqft**: \$3.40/sqft
- **Amenities count**: 1
- **Listing date**: 2019-12-26 11:20:50

### Market context
- **ZORI baseline for this ZIP+month** (2019-12-31): \$1405/mo
- **ZORI source**: direct ZIP match (22193)
- **price / ZORI baseline**: 0.605  ⇒  listing is at 60% of market
- **z-score within ZIP+month**: N/A (group too small)
- **City context** (Woodbridge, VA): 202 listings  |  city median price: \$1588/mo  |  city median \$/sqft: \$1.73

### Model verdict
- **Snorkel P(SCAM)**: 1.0000  (SCAM)
- **LFs that fired**: zori_low(SCAM); price_anomaly(SCAM); auto_template_body(NOT_SCAM)

### Title
> One BR Gordon Blvd

### Body (full)
```
This unit is located at Gordon Blvd, Woodbridge, 22192, VAMonthly rental rates range from $850We have 1 beds units available for rent Apartment features include:-- Furnished- Pool
```

---

## Row 10  —  stratum: `top50`

### Listing
- **Location**: Riverview, FL  (ZIP 33569)
- **Listed price**: \$865/mo
- **Size / layout**: 219 sqft  |  1.0 BR  |  1.0 BA
- **Per-bedroom**: \$865/BR  |  **Per-sqft**: \$3.95/sqft
- **Amenities count**: 1
- **Listing date**: 2019-12-22 11:47:28

### Market context
- **ZORI baseline for this ZIP+month** (2019-12-31): \$1462/mo
- **ZORI source**: direct ZIP match (33569)
- **price / ZORI baseline**: 0.592  ⇒  listing is at 59% of market
- **z-score within ZIP+month**: N/A (group too small)
- **City context** (Riverview, FL): 31 listings  |  city median price: \$1375/mo  |  city median \$/sqft: \$1.14

### Model verdict
- **Snorkel P(SCAM)**: 1.0000  (SCAM)
- **LFs that fired**: zori_low(SCAM); price_anomaly(SCAM); auto_template_body(NOT_SCAM)

### Title
> One BR Windmill Cove Dr

### Body (full)
```
This unit is located at Windmill Cove Dr, Riverview, 33569, FLMonthly rental rates range from $865We have 1 beds units available for rent Apartment available amenities:-- Pool- Furnished
```

---

