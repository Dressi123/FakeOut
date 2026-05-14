# Labeling batch 2 — rows 11-20

Open this file, read each listing, then come back to chat with overrides.
Format: `1=scam, 4=unsure, 7=scam` (silence on a row = accept proposed label)

---

## Row 11  —  stratum: `top50`

### Listing
- **Location**: Torrance, CA  (ZIP 90503)
- **Listed price**: \$1300/mo
- **Size / layout**: 250 sqft  |  1.0 BR  |  1.0 BA
- **Per-bedroom**: \$1300/BR  |  **Per-sqft**: \$5.20/sqft
- **Amenities count**: 1
- **Listing date**: 2019-12-22 11:56:27

### Market context
- **ZORI baseline for this ZIP+month** (2019-12-31): \$2229/mo
- **ZORI source**: direct ZIP match (90503)
- **price / ZORI baseline**: 0.583  ⇒  listing is at 58% of market
- **z-score within ZIP+month**: N/A (group too small)
- **City context** (Torrance, CA): 72 listings  |  city median price: \$1968/mo  |  city median \$/sqft: \$2.95

### Model verdict
- **Snorkel P(SCAM)**: 1.0000  (SCAM)
- **LFs that fired**: zori_low(SCAM); price_anomaly(SCAM); auto_template_body(NOT_SCAM)

### Title
> One BR Spencer Street #404

### Body (full)
```
This unit is located at Spencer Street #404, Torrance, 90503, CAMonthly rental rates range from $1300We have 1 beds units available for rent Apartment available amenities:-- Pool
```

---

## Row 12  —  stratum: `top50`

### Listing
- **Location**: San Francisco, CA  (ZIP 94114)
- **Listed price**: \$1400/mo
- **Size / layout**: 1100 sqft  |  3.0 BR  |  2.0 BA
- **Per-bedroom**: \$467/BR  |  **Per-sqft**: \$1.27/sqft
- **Amenities count**: 0
- **Listing date**: 2019-08-06 11:51:30

### Market context
- **ZORI baseline for this ZIP+month** (2019-08-31): \$3760/mo
- **ZORI source**: direct ZIP match (94114)
- **price / ZORI baseline**: 0.372  ⇒  listing is at 37% of market
- **z-score within ZIP+month**: N/A (group too small)
- **City context** (San Francisco, CA): 133 listings  |  city median price: \$3500/mo  |  city median \$/sqft: \$6.00

### Model verdict
- **Snorkel P(SCAM)**: 1.0000  (SCAM)
- **LFs that fired**: zori_low(SCAM); price_anomaly(SCAM); auto_template_body(NOT_SCAM)

### Title
> Three BR 340 Fremont

### Body (full)
```
This unit is located at 340 Fremont, San Francisco, 94105, CAMonthly rental rates range from $1400We have 3 beds units available for rent
```

---

## Row 13  —  stratum: `top50`

### Listing
- **Location**: Germantown, MD  (ZIP 20876)
- **Listed price**: \$750/mo
- **Size / layout**: 250 sqft  |  1.0 BR  |  1.0 BA
- **Per-bedroom**: \$750/BR  |  **Per-sqft**: \$3.00/sqft
- **Amenities count**: 1
- **Listing date**: 2019-12-26 11:20:52

### Market context
- **ZORI baseline for this ZIP+month** (2019-12-31): \$1835/mo
- **ZORI source**: spatial k-NN, 3 neighbors at ~7.2km from ZIP 20876
- **price / ZORI baseline**: 0.409  ⇒  listing is at 41% of market
- **z-score within ZIP+month**: N/A (group too small)
- **City context** (Germantown, MD): 113 listings  |  city median price: \$1596/mo  |  city median \$/sqft: \$1.73

### Model verdict
- **Snorkel P(SCAM)**: 1.0000  (SCAM)
- **LFs that fired**: zori_low(SCAM); price_anomaly(SCAM); auto_template_body(NOT_SCAM)

### Title
> One BR Grey Eagle Court

### Body (full)
```
This unit is located at Grey Eagle Court, Germantown, 20874, MDMonthly rental rates range from $750We have 1 beds units available for rent Apartment features include:-- Pool- Furnished
```

---

## Row 14  —  stratum: `top50`

### Listing
- **Location**: Sarasota, FL  (ZIP 34239)
- **Listed price**: \$860/mo
- **Size / layout**: 250 sqft  |  1.0 BR  |  1.0 BA
- **Per-bedroom**: \$860/BR  |  **Per-sqft**: \$3.44/sqft
- **Amenities count**: 1
- **Listing date**: 2019-12-26 11:18:58

### Market context
- **ZORI baseline for this ZIP+month** (2019-12-31): \$1490/mo
- **ZORI source**: spatial k-NN, 4 neighbors at ~5.2km from ZIP 34239
- **price / ZORI baseline**: 0.577  ⇒  listing is at 58% of market
- **z-score within ZIP+month**: N/A (group too small)
- **City context** (Sarasota, FL): 204 listings  |  city median price: \$1430/mo  |  city median \$/sqft: \$1.59

### Model verdict
- **Snorkel P(SCAM)**: 1.0000  (SCAM)
- **LFs that fired**: zori_low(SCAM); price_anomaly(SCAM); auto_template_body(NOT_SCAM)

### Title
> One BR Mauna Loa Boulevard

### Body (full)
```
This unit is located at Mauna Loa Boulevard, Sarasota, 34241, FLMonthly rental rates range from $860We have 1 beds units available for rent Apartment features include:-- Pool
```

---

## Row 15  —  stratum: `top50`

### Listing
- **Location**: Parsippany, NJ  (ZIP 07054)
- **Listed price**: \$1425/mo
- **Size / layout**: 650 sqft  |  1.0 BR  |  1.0 BA
- **Per-bedroom**: \$1425/BR  |  **Per-sqft**: \$2.19/sqft
- **Amenities count**: 0
- **Listing date**: 2019-12-26 11:37:32

### Market context
- **ZORI baseline for this ZIP+month** (2019-12-31): \$2326/mo
- **ZORI source**: spatial k-NN, 1 neighbors at ~10.1km from ZIP 07054
- **price / ZORI baseline**: 0.613  ⇒  listing is at 61% of market
- **z-score within ZIP+month**: N/A (group too small)
- **City context** (Parsippany, NJ): 38 listings  |  city median price: \$1513/mo  |  city median \$/sqft: \$2.21

### Model verdict
- **Snorkel P(SCAM)**: 1.0000  (SCAM)
- **LFs that fired**: zori_low(SCAM); auto_template_body(NOT_SCAM)

### Title
> One BR 300 Parsippany Rd

### Body (full)
```
This unit is located at 300 Parsippany Rd, Parsippany, 07054, NJMonthly rental rates range from $1425 - $1825We have one - two beds units available for rent
```

---

## Row 16  —  stratum: `high`

### Listing
- **Location**: Los Angeles, CA  (ZIP 90020)
- **Listed price**: \$1020/mo
- **Size / layout**: 250 sqft  |  0.0 BR  |  1.0 BA
- **Per-bedroom**: (studio or N/A)  |  **Per-sqft**: \$4.08/sqft
- **Amenities count**: 7
- **Listing date**: 2019-09-17 19:17:15

### Market context
- **ZORI baseline for this ZIP+month** (2019-09-30): \$1815/mo
- **ZORI source**: direct ZIP match (90020)
- **price / ZORI baseline**: 0.562  ⇒  listing is at 56% of market
- **z-score within ZIP+month**: -2.56
- **City context** (Los Angeles, CA): 2,433 listings  |  city median price: \$2603/mo  |  city median \$/sqft: \$3.28

### Model verdict
- **Snorkel P(SCAM)**: 0.7978  (SCAM)
- **LFs that fired**: zori_low(SCAM); long_detailed_body(NOT_SCAM)

### Title
> Experience Urban Living WITHOUT the high cost of living in Downtown.

### Body (full)
```
Built in the 1920's and formerly known as Kipling, this hip and comfortable studio home is full of historical charm. Enjoy our newly upgraded amenities, state of the art fitness facilities or venture off to nearby parks in this walkable neighborhood. Anthony Bourdain did a special about Koreatown, and it definitely is an up and coming neighborhood. " - Review by Charity C Yelp Package Receiving, Management office onsite, Night Patrol, Availability 24 Hours, Free Weights, Controlled Access/Gated, Walkable Neighborhood, Adjacent to Mid Wilshire and Downtown LA, Historial 1920's Building, Clean and Elegant Lobby, Walkable distance to Grocery and Dining, Professional and Caring Management, Elevator, Fitness facilities with Mirrored Walls, Historic Building, Laundry area, On-Site Maintenance, Near Metro Local Line, Spanish Speaking Staff, Window Coverings, Air conditioning, Cable/DSL Ready, Ceiling Fan, Upgrade Interiors, New Cabinets, Kitchenette, Generous Closet Space, Refrigerator. Pets are not allowed.
```

---

## Row 17  —  stratum: `high`

### Listing
- **Location**: Cleveland, OH  (ZIP 44115)
- **Listed price**: \$675/mo
- **Size / layout**: 320 sqft  |  1.0 BR  |  1.0 BA
- **Per-bedroom**: \$675/BR  |  **Per-sqft**: \$2.11/sqft
- **Amenities count**: 2
- **Listing date**: 2019-09-17 20:31:18

### Market context
- **ZORI baseline for this ZIP+month** (2019-09-30): \$783/mo
- **ZORI source**: spatial k-NN, 4 neighbors at ~5.9km from ZIP 44115
- **price / ZORI baseline**: 0.862  ⇒  listing is at 86% of market
- **z-score within ZIP+month**: -2.03
- **City context** (Cleveland, OH): 617 listings  |  city median price: \$1340/mo  |  city median \$/sqft: \$1.57

### Model verdict
- **Snorkel P(SCAM)**: 0.9027  (SCAM)
- **LFs that fired**: zori_low(SCAM)

### Title
> Cleveland Luxurious Studio + 1

### Body (full)
```
Income Requirement: Must have 3. 0x the rent in total household income before taxes, include income from all adults. Utilities included: Cable, Electric, Gas, Hot Water, Internet, Sewer, Trash, Water. More units available: 0 Bd / 1 Bedrooms 448 sq-ft for $775/mo | 0 Bd / 1 Bedrooms 387 sq. feet for $700/mo | 0 Bd / 1 Bedrooms 481 sq. feet for $875/mo
```

---

## Row 18  —  stratum: `high`

### Listing
- **Location**: Temple Hills, MD  (ZIP 20757)
- **Listed price**: \$1168/mo
- **Size / layout**: 600 sqft  |  1.0 BR  |  1.0 BA
- **Per-bedroom**: \$1168/BR  |  **Per-sqft**: \$1.95/sqft
- **Amenities count**: 1
- **Listing date**: 2019-09-17 21:09:46

### Market context
- **ZORI baseline for this ZIP+month** (2019-09-30): N/A
- **ZORI source**: no baseline (AK/HI/PR or rural)
- **price / ZORI baseline**: N/A
- **z-score within ZIP+month**: N/A (group too small)
- **City context** (Temple Hills, MD): 63 listings  |  city median price: \$1258/mo  |  city median \$/sqft: \$1.49

### Model verdict
- **Snorkel P(SCAM)**: 0.7001  (SCAM)
- **LFs that fired**: price_anomaly(SCAM)

### Title
> One BA \ One BR - convenient location. Cat OK!

### Body (full)
```
Very Convenient Location Close to The Beltway, Wilson Bridge & Washington, DC National ! Income Requirement: Must have 3. 0x the rent in total household income before taxes, include income from all adults. Utilities included: Electric, Gas. Parking Info: We have free, unreserved parking spaces on our surface lots no garages. Residents must display a current, community-issued times. Visitors may park anywhere on-site from 6: 00 AM - 12: 00 midnight, after which they must park in designated spaces or display a current, community-issued visitor permit. More units available: two Bd / 1 Bedrooms 825 sq. feet for $1,288/mo | one Bd / 1 Bedrooms 720 square feet for $1,248/mo | two Bd / 1 Bedrooms 945 sq-ft for $1,398/mo | one Bd / 1 Bedrooms 600 square ft for $1,199/mo | three Bd / 2 Bedrooms 1,135 sq. feet for $1,546/mo |
```

---

## Row 19  —  stratum: `high`

### Listing
- **Location**: Nashville, TN  (ZIP 37212)
- **Listed price**: \$1796/mo
- **Size / layout**: 634 sqft  |  1.0 BR  |  1.0 BA
- **Per-bedroom**: \$1796/BR  |  **Per-sqft**: \$2.83/sqft
- **Amenities count**: 5
- **Listing date**: 2019-12-26 11:36:13

### Market context
- **ZORI baseline for this ZIP+month** (2019-12-31): \$1612/mo
- **ZORI source**: direct ZIP match (37212)
- **price / ZORI baseline**: 1.114  ⇒  listing is at 111% of market
- **z-score within ZIP+month**: 0.04
- **City context** (Nashville, TN): 219 listings  |  city median price: \$1324/mo  |  city median \$/sqft: \$1.59

### Model verdict
- **Snorkel P(SCAM)**: 1.0000  (SCAM)
- **LFs that fired**: auto_template_body(NOT_SCAM)

### Title
> One BR 3102 Belwood St

### Body (full)
```
This unit is located at 3102 Belwood St, Nashville, 37203, TNMonthly rental rates range from $1796We have 1 beds units available for rent
```

---

## Row 20  —  stratum: `high`

### Listing
- **Location**: Mequon, WI  (ZIP 53092)
- **Listed price**: \$1595/mo
- **Size / layout**: 954 sqft  |  1.0 BR  |  1.0 BA
- **Per-bedroom**: \$1595/BR  |  **Per-sqft**: \$1.67/sqft
- **Amenities count**: 9
- **Listing date**: 2019-12-26 11:11:56

### Market context
- **ZORI baseline for this ZIP+month** (2019-12-31): N/A
- **ZORI source**: no baseline (AK/HI/PR or rural)
- **price / ZORI baseline**: N/A
- **z-score within ZIP+month**: N/A (group too small)
- **City context** (Mequon, WI): 5 listings  |  city median price: \$1500/mo  |  city median \$/sqft: \$1.67

### Model verdict
- **Snorkel P(SCAM)**: 1.0000  (SCAM)
- **LFs that fired**: auto_template_body(NOT_SCAM)

### Title
> One BR 6300 W Mequon Rd

### Body (full)
```
This unit is located at 6300 W Mequon Rd, Mequon, 53092, WIMonthly rental rates range from $1595 - $2495We have one - three beds units available for rent Apartment features include:-- In-Unit Laundry- Dishwasher- Controlled Access- Storage- Air conditioned- Balcony, Deck, Patio- Sheltered parking- Fitness facilities
```

---

