# Labeling batch 3 — rows 21-30

Open this file, read each listing, then come back to chat with overrides.
Format: `1=scam, 4=unsure, 7=scam` (silence on a row = accept proposed label)

---

## Row 21  —  stratum: `high`

### Listing
- **Location**: Ann Arbor, MI  (ZIP 48109)
- **Listed price**: \$4430/mo
- **Size / layout**: 2995 sqft  |  6.0 BR  |  2.5 BA
- **Per-bedroom**: \$738/BR  |  **Per-sqft**: \$1.48/sqft
- **Amenities count**: 0
- **Listing date**: 2019-12-26 11:22:50

### Market context
- **ZORI baseline for this ZIP+month** (2019-12-31): \$1721/mo
- **ZORI source**: spatial k-NN, 4 neighbors at ~4.1km from ZIP 48109
- **price / ZORI baseline**: 2.574  ⇒  listing is at 257% of market
- **z-score within ZIP+month**: 2.03
- **City context** (Ann Arbor, MI): 35 listings  |  city median price: \$1395/mo  |  city median \$/sqft: \$1.64

### Model verdict
- **Snorkel P(SCAM)**: 1.0000  (SCAM)
- **LFs that fired**: auto_template_body(NOT_SCAM)

### Title
> Six BR 1537 Packard St

### Body (full)
```
This unit is located at 1537 Packard St, Ann Arbor, 48104, MIMonthly rental rates range from $4430We have 6 beds units available for rent
```

---

## Row 22  —  stratum: `high`

### Listing
- **Location**: Reno, NV  (ZIP 89505)
- **Listed price**: \$1334/mo
- **Size / layout**: 708 sqft  |  1.0 BR  |  1.0 BA
- **Per-bedroom**: \$1334/BR  |  **Per-sqft**: \$1.88/sqft
- **Amenities count**: 1
- **Listing date**: 2019-12-26 11:10:25

### Market context
- **ZORI baseline for this ZIP+month** (2019-12-31): \$1246/mo
- **ZORI source**: spatial k-NN, 5 neighbors at ~4.6km from ZIP 89505
- **price / ZORI baseline**: 1.071  ⇒  listing is at 107% of market
- **z-score within ZIP+month**: -0.24
- **City context** (Reno, NV): 336 listings  |  city median price: \$1295/mo  |  city median \$/sqft: \$1.55

### Model verdict
- **Snorkel P(SCAM)**: 1.0000  (SCAM)
- **LFs that fired**: auto_template_body(NOT_SCAM)

### Title
> One BR 1001 S Meadows Pkwy

### Body (full)
```
This unit is located at 1001 S Meadows Pkwy, Reno, 89521, NVMonthly rental rates range from $1334 - $2367We have one - three beds units available for rent Apartment features include:-- Sheltered parking- Fitness facilities
```

---

## Row 23  —  stratum: `high`

### Listing
- **Location**: Buford, GA  (ZIP 30518)
- **Listed price**: \$1070/mo
- **Size / layout**: 828 sqft  |  1.0 BR  |  1.0 BA
- **Per-bedroom**: \$1070/BR  |  **Per-sqft**: \$1.29/sqft
- **Amenities count**: 5
- **Listing date**: 2019-12-26 11:08:03

### Market context
- **ZORI baseline for this ZIP+month** (2019-12-31): \$1300/mo
- **ZORI source**: direct ZIP match (30518)
- **price / ZORI baseline**: 0.823  ⇒  listing is at 82% of market
- **z-score within ZIP+month**: N/A (group too small)
- **City context** (Buford, GA): 5 listings  |  city median price: \$1450/mo  |  city median \$/sqft: \$0.98

### Model verdict
- **Snorkel P(SCAM)**: 1.0000  (SCAM)
- **LFs that fired**: auto_template_body(NOT_SCAM)

### Title
> One BR 2910 Buford Drive Ne

### Body (full)
```
This unit is located at 2910 Buford Drive Ne, Buford, 30519, GAMonthly rental rates range from $1070 - $1318We have one - three beds units available for rent Apartment features include:-- Internet Included- Surface Parking- Sheltered parking- Pool- Fitness facilities- On-Site Laundry- Dishwasher- Refrigerator
```

---

## Row 24  —  stratum: `high`

### Listing
- **Location**: Fenton, MO  (ZIP 63026)
- **Listed price**: \$784/mo
- **Size / layout**: 780 sqft  |  2.0 BR  |  1.0 BA
- **Per-bedroom**: \$392/BR  |  **Per-sqft**: \$1.01/sqft
- **Amenities count**: 10
- **Listing date**: 2019-12-26 11:07:38

### Market context
- **ZORI baseline for this ZIP+month** (2019-12-31): N/A
- **ZORI source**: no baseline (AK/HI/PR or rural)
- **price / ZORI baseline**: N/A
- **z-score within ZIP+month**: N/A (group too small)
- **City context** (Fenton, MO): 9 listings  |  city median price: \$850/mo  |  city median \$/sqft: \$0.89

### Model verdict
- **Snorkel P(SCAM)**: 1.0000  (SCAM)
- **LFs that fired**: auto_template_body(NOT_SCAM)

### Title
> Two BR 1054 Green Mountain Ct.

### Body (full)
```
This unit is located at 1054 Green Mountain Ct., Fenton, 63026, MOMonthly rental rates range from $784We have 2 beds units available for rent Apartment features include:-- Dishwasher- Fitness facilities- On-Site Laundry- Garbage Disposal- Refrigerator- Storage- Pool- Air conditioned
```

---

## Row 25  —  stratum: `high`

### Listing
- **Location**: Grand Forks, ND  (ZIP 58202)
- **Listed price**: \$685/mo
- **Size / layout**: 640 sqft  |  1.0 BR  |  1.0 BA
- **Per-bedroom**: \$685/BR  |  **Per-sqft**: \$1.07/sqft
- **Amenities count**: 0
- **Listing date**: 2019-12-26 11:31:50

### Market context
- **ZORI baseline for this ZIP+month** (2019-12-31): N/A
- **ZORI source**: no baseline (AK/HI/PR or rural)
- **price / ZORI baseline**: N/A
- **z-score within ZIP+month**: N/A (group too small)
- **City context** (Grand Forks, ND): 108 listings  |  city median price: \$872/mo  |  city median \$/sqft: \$0.90

### Model verdict
- **Snorkel P(SCAM)**: 1.0000  (SCAM)
- **LFs that fired**: auto_template_body(NOT_SCAM)

### Title
> One BR 2650 26th Avenue S.

### Body (full)
```
This unit is located at 2650 26th Avenue S., Grand Forks, 58201, NDMonthly rental rates range from $685 - $910We have one - two beds units available for rent
```

---

## Row 26  —  stratum: `mid`

### Listing
- **Location**: Oxon Hill, MD  (ZIP 20745)
- **Listed price**: \$1229/mo
- **Size / layout**: 886 sqft  |  2.0 BR  |  1.0 BA
- **Per-bedroom**: \$614/BR  |  **Per-sqft**: \$1.39/sqft
- **Amenities count**: 2
- **Listing date**: 2019-09-17 20:44:33

### Market context
- **ZORI baseline for this ZIP+month** (2019-09-30): \$1593/mo
- **ZORI source**: direct ZIP match (20745)
- **price / ZORI baseline**: 0.772  ⇒  listing is at 77% of market
- **z-score within ZIP+month**: -0.85
- **City context** (Oxon Hill, MD): 44 listings  |  city median price: \$1480/mo  |  city median \$/sqft: \$1.60

### Model verdict
- **Snorkel P(SCAM)**: 0.5000  (ABSTAIN)
- **LFs that fired**: (none)

### Title
> Pet Friendly 2+1 Apartment in Oxon Hill. Pet OK!

### Body (full)
```
Experience ultimate Apartments in Oxon Hill, MD. South gives you everything you want in an Oxon Hill, MD apartment: a convenient location, excellent community amenities and lots of room to live. All of our stylish and spacious one-, two- and 3 beds apartments include eat-in kitchens, gas stoves and individually controlled heat and air. Plus, you'll have access to the pool and sundeck. And, did we the location You'll be close to the exciting shopping, dining and nightlife of National. South is a perfect choice for , convenient and comfortable apartments in Oxon Hill, MD. And, you're just a short hop to DC! Income Requirement: Must have 3. 0x the rent in total household income before taxes, include income from all adults. Utilities: Renter responsible for all utilities. Pet restrictions: Weight and breed restrictions apply. Parking Information: Open Parking: 1st come, 1st serve. More units available: two Bd / 1 Bedrooms 1,106 sq-ft for $1,437/mo | two Bd / 1 Bedrooms 1,288 sq.
```

---

## Row 27  —  stratum: `mid`

### Listing
- **Location**: Lenexa, KS  (ZIP 66250)
- **Listed price**: \$986/mo
- **Size / layout**: 920 sqft  |  2.0 BR  |  2.0 BA
- **Per-bedroom**: \$493/BR  |  **Per-sqft**: \$1.07/sqft
- **Amenities count**: 0
- **Listing date**: 2019-02-22 07:19:33

### Market context
- **ZORI baseline for this ZIP+month** (2019-02-28): \$1225/mo
- **ZORI source**: spatial k-NN, 2 neighbors at ~10.1km from ZIP 66250
- **price / ZORI baseline**: 0.805  ⇒  listing is at 80% of market
- **z-score within ZIP+month**: -0.63
- **City context** (Lenexa, KS): 103 listings  |  city median price: \$1190/mo  |  city median \$/sqft: \$1.17

### Model verdict
- **Snorkel P(SCAM)**: 0.5000  (ABSTAIN)
- **LFs that fired**: (none)

### Title
> $986 / Two BR - Great Deal. MUST SEE!

### Body (full)
```
The new apartments youve been searching for in Lenexa can be found. Center Apartments. We provide spacious homes in a picturesque community, complete with a myriad of resident privileges. The fully remodeled exterior sets the scene for our established apartment homes. Though, its truly the interiors that are what set our apartments apart from the rest. Spacious, yet comfortable, these roomy one, two, and three beds floor plans are sure to delight. Our peaceful location is conveniently close to Interstate 435, and is minutes from the Lenexa City Center which boasts exceptional shopping, dining, and entertainment opportunities that the Kansas City area has to offer. Let us welcome you to The Pointe and come home to our apartments, where rest and relaxation is a part of the lifestyle!today! Income Requirement: Must have 3. 0x the rent in total household income before taxes, include income from all adults. Utilities: Renter responsible for all utilities. Additional Charges: Renter's insurance required.
```

---

## Row 28  —  stratum: `mid`

### Listing
- **Location**: Matawan, NJ  (ZIP 07747)
- **Listed price**: \$2265/mo
- **Size / layout**: 1301 sqft  |  2.0 BR  |  2.0 BA
- **Per-bedroom**: \$1132/BR  |  **Per-sqft**: \$1.74/sqft
- **Amenities count**: 0
- **Listing date**: 2019-09-18 00:42:34

### Market context
- **ZORI baseline for this ZIP+month** (2019-09-30): N/A
- **ZORI source**: no baseline (AK/HI/PR or rural)
- **price / ZORI baseline**: N/A
- **z-score within ZIP+month**: N/A (group too small)
- **City context** (Matawan, NJ): 20 listings  |  city median price: \$2005/mo  |  city median \$/sqft: \$1.77

### Model verdict
- **Snorkel P(SCAM)**: 0.5000  (ABSTAIN)
- **LFs that fired**: (none)

### Title
> Two BR Apartment - Live the lifestyle you.

### Body (full)
```
Square footage: 1301 square feet A brand new high-end apartment community offering spacious 1 and 2 beds apartment homes. With 9 ft ceilings, stainless appliances and premium granite counter tops, these are just a few of the outstanding features you will come home to! Our beautiful community will offer incredible convenience to its residents with shops and eateries below the apartments. The offers commuter convenience, the Matawan Aberdeen Railway station is just minutes away, and a NJ Transit bus community. Be the 1st to rent a 1st class apartment ! IMMEDIATE OCCUPANCY! LIMITED AVAILABILITY!TODAY & HEAR ABOUT OUR SPECIALS. More units available: one Bd / 1 Bedrooms 883 square feet for $1,845/mo | two Bd / 2 Bedrooms 1,434 square ft for $2,515/mo | one Bd / 1 Bedrooms 1,163 square ft for $2,015/mo | two Bd / 2 Bedrooms 1,267 sq-ft for $2,240/mo | one Bd / 1 Bedrooms 977 square feet for $1,995/mo | two Bd / 2 Bedrooms 1,299 sq-ft for $2,365/mo | one Bd / 1 Bedrooms 1,003 sq.
```

---

## Row 29  —  stratum: `mid`

### Listing
- **Location**: Charlotte, NC  (ZIP 28204)
- **Listed price**: \$1324/mo
- **Size / layout**: 617 sqft  |  1.0 BR  |  1.0 BA
- **Per-bedroom**: \$1324/BR  |  **Per-sqft**: \$2.15/sqft
- **Amenities count**: 0
- **Listing date**: 2019-02-22 06:06:23

### Market context
- **ZORI baseline for this ZIP+month** (2019-02-28): \$1371/mo
- **ZORI source**: direct ZIP match (28204)
- **price / ZORI baseline**: 0.966  ⇒  listing is at 97% of market
- **z-score within ZIP+month**: -0.31
- **City context** (Charlotte, NC): 1,125 listings  |  city median price: \$1229/mo  |  city median \$/sqft: \$1.27

### Model verdict
- **Snorkel P(SCAM)**: 0.5000  (ABSTAIN)
- **LFs that fired**: (none)

### Title
> Indulge your Dilworth.

### Body (full)
```
Square footage: 617 sq-ft, unit number: 634. Our boutique inspired studio, 1 and 2 beds luxury apartment homes allow you to live in luxurious in Midtown. Live in Charlotte s most celebrated neighborhood, Dilworth, where an extensive collection of fine dining restaurants, coffee roasters, and purveyors of handcrafted cocktails are just steps from your front door. With sophisticated interiors featuring bright, white subway tiles and sharp, clean lines you will love the state of the art design of Berkshire Dilworth. Your new home will boast condo-quality appointments such as chef-inspired gourmet kitchens with granite counter tops and customized cabinets, state of the art satin nickel hardware & fixtures, wood inspired plank flooring, soaking tubs, walk-in showers with tile surrounds, and USB charging ports in each residence. More units available: one Bd / 1 Bedrooms 870 sq. feet for $1,590/mo | two Bd / 2.5 Bedrooms 1,619 sq.
```

---

## Row 30  —  stratum: `mid`

### Listing
- **Location**: Greensboro, NC  (ZIP 27406)
- **Listed price**: \$1295/mo
- **Size / layout**: 1555 sqft  |  4.0 BR  |  2.5 BA
- **Per-bedroom**: \$324/BR  |  **Per-sqft**: \$0.83/sqft
- **Amenities count**: 1
- **Listing date**: 2019-09-17 20:36:21

### Market context
- **ZORI baseline for this ZIP+month** (2019-09-30): \$750/mo
- **ZORI source**: direct ZIP match (27406)
- **price / ZORI baseline**: 1.726  ⇒  listing is at 173% of market
- **z-score within ZIP+month**: 3.21
- **City context** (Greensboro, NC): 502 listings  |  city median price: \$887/mo  |  city median \$/sqft: \$0.96

### Model verdict
- **Snorkel P(SCAM)**: 0.6978  (SCAM)
- **LFs that fired**: zori_high(NOT_SCAM)

### Title
> Four BR Apartment in Greensboro

### Body (full)
```
Looking for luxurious in the Triad Look no further when you come to Juliet ! Juliet offers spacious 1 and 2 beds ok for pets floor plans with ample closet space, laundry hookups, and fully equipped kitchens. Some apartments include bright, airy sunrooms and soaring ceilings. Ideally located in the Greensboro area, Juliet is just minutes from downtown, UNCG, the Greensboro Coliseum Complex, 4 Seasons Town Centre Mall, Wet n Wild Emerald Pointe Water Park, and more! Enjoy all of the nearby shops, restaurants, museums, and attractions, and then return home to the peaceful comfort of Juliet. With our professional management office onsite team and 24-hr emergency maintenance services, you willll be sure to have a more carefree lifestyle!Be sure to ask us about our HOUSES that we also have Max two Pet per Apartment Breed Restrictions Apply. More units available: two Bd / 2 Bedrooms 1,218 square feet for $879/mo | two Bd / 2 Bedrooms 1,080 sq-ft for $799/mo |
```

---

