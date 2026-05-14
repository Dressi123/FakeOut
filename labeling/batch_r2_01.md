# Labeling batch (round 2) 1 — rows 51-60

Reply format: `52=scam, 55=unsure` (silence on a row = accept proposed label)

---

## Row 51  —  stratum: `top_new`

### Listing
- **Location**: Waltham, MA  (ZIP 02451)
- **Listed price**: \$1890/mo  |  **Effective price**: \$1890/mo
- **Range pattern**: no range pattern detected
- **Size / layout**: 300 sqft  |  1.0 BR  |  1.0 BA
- **Per-bedroom**: \$1890/BR  |  **Per-sqft**: \$6.30
- **Amenities count**: 3  |  **Has photo**: Yes  |  **Source**: RentDigs.com
- **Listing date**: 2019-09-17 22:59:08

### Market context
- **ZORI baseline** (2019-09-30): \$2313/mo  (spatial k-NN, 4 neighbors at ~5.3km)
- **Effective / ZORI ratio**: 0.817
- **City** (Waltham, MA): 124 listings  |  median \$2442/mo  |  median \$2.49/sqft

### Model verdict
- **Snorkel P(SCAM)**: 0.9342  (SCAM)
- **LFs that fired**: price_anomaly(SCAM); template_body(NOT_SCAM); long_detailed_body(NOT_SCAM); weekly_rental(NOT_SCAM)

### Title
> Waltham - 1bd/One BA 300sqft Apartment for rent

### Body (full)
```
NOTICE: You can now easily reserve our lowest rates available on-line! To unlock these rates, click "Visit the property's management " under the Helpful Details section below, and reserve today!Welcome to Extended Stay America, your solution for short term housing. Enjoy a furnished terrific price with free utilities, free cable, free Wi-Fi, no lease to sign, and no credit check! means you won't have to pay extra monthly bills for electric, gas, water, cable, or internet, that could mean a savings of several hundred dollars each month!Each of our furnished, pets allowed studios comes equipped with a refrigerator, stove top, microwave, toaster, and coffee maker. You'll also enjoy our convenient on-site laundry facilities and free grab-and-go breakfast every morning. Housekeeping services are also Additional charges may apply. Booking restrictions and taxes apply.
```

---

## Row 52  —  stratum: `top_new`

### Listing
- **Location**: Denver, CO  (ZIP 80237)
- **Listed price**: \$1080/mo  |  **Effective price**: \$1080/mo
- **Range pattern**: no range pattern detected
- **Size / layout**: 270 sqft  |  1.0 BR  |  1.0 BA
- **Per-bedroom**: \$1080/BR  |  **Per-sqft**: \$4.00
- **Amenities count**: 3  |  **Has photo**: Yes  |  **Source**: RentDigs.com
- **Listing date**: 2019-09-17 21:27:04

### Market context
- **ZORI baseline** (2019-09-30): \$1509/mo  (direct ZIP match (80237))
- **Effective / ZORI ratio**: 0.716
- **City** (Denver, CO): 2,755 listings  |  median \$1499/mo  |  median \$1.84/sqft

### Model verdict
- **Snorkel P(SCAM)**: 0.9342  (SCAM)
- **LFs that fired**: price_anomaly(SCAM); template_body(NOT_SCAM); long_detailed_body(NOT_SCAM); weekly_rental(NOT_SCAM)

### Title
> Denver, Great Location, One BR Apartment.

### Body (full)
```
NOTICE: You can now easily reserve our lowest rates available on-line! To unlock these rates, click "Visit the property's management " under the Helpful Info section below, and reserve today!Welcome to Extended Stay America, your solution for short term housing. Enjoy a furnished good price with free utilities, free cable, free Wi-Fi, no lease to sign, and no credit check! means you won't have to pay extra monthly bills for electric, gas, water, cable, or internet, that could mean a savings of several hundred dollars each month!Each of our furnished, ok for pets studios comes equipped with a refrigerator, stove top, microwave, toaster, and coffee maker. You'll also enjoy our convenient on-site laundry facilities and free grab-and-go breakfast every morning. Housekeeping services are also Additional charges may apply. Booking restrictions and taxes apply.
```

---

## Row 53  —  stratum: `top_new`

### Listing
- **Location**: Richmond, VA  (ZIP 23224)
- **Listed price**: \$1019/mo  |  **Effective price**: \$1019/mo
- **Range pattern**: no range pattern detected
- **Size / layout**: 1320 sqft  |  2.0 BR  |  1.0 BA
- **Per-bedroom**: \$510/BR  |  **Per-sqft**: \$0.77
- **Amenities count**: 7  |  **Has photo**: No  |  **Source**: RentDigs.com
- **Listing date**: 2019-02-22 19:36:17

### Market context
- **ZORI baseline** (2019-02-28): \$1028/mo  (direct ZIP match (23224))
- **Effective / ZORI ratio**: 0.991
- **City** (Richmond, VA): 914 listings  |  median \$1280/mo  |  median \$1.55/sqft

### Model verdict
- **Snorkel P(SCAM)**: 0.9348  (SCAM)
- **LFs that fired**: section8_income(NOT_SCAM); student_housing(NOT_SCAM); template_body(NOT_SCAM); long_detailed_body(NOT_SCAM)

### Title
> Two BR Apartment - Large & Bright

### Body (full)
```
Take loft living to the next Hudson. We offer newly upgraded one, two, and 3 beds spacious apartments in the lively city of, VA. Our pets allowed community is the definition of industrial chic with its tasteful designs, hallway painting, flexible spaces and coveted amenities. You ll love diving into this full-service apartment experience. Explore the nearby locations such as University of, Huguenot High School, Martin Luther King Jr. Middle School, Blackwell Elementary School, the VCU campus and Carytown. Stroll by the James River, visit the beautiful Forest Hill Park and its stone house known as Boscobel or tour around the historic area of Shockoe Bottom which hosts the Edgar Allan Poe Museum, Adam Craig House as well as various popular restaurants. When the time comes, the Interstate 95 provides for an easy commute to s West End, Short Pump, MCV and many other places.
```

---

## Row 54  —  stratum: `top_new`

### Listing
- **Location**: Waltham, MA  (ZIP 02451)
- **Listed price**: \$2100/mo  |  **Effective price**: \$2100/mo
- **Range pattern**: no range pattern detected
- **Size / layout**: 300 sqft  |  1.0 BR  |  1.0 BA
- **Per-bedroom**: \$2100/BR  |  **Per-sqft**: \$7.00
- **Amenities count**: 4  |  **Has photo**: Yes  |  **Source**: RentDigs.com
- **Listing date**: 2019-09-17 22:58:58

### Market context
- **ZORI baseline** (2019-09-30): \$2313/mo  (spatial k-NN, 4 neighbors at ~5.3km)
- **Effective / ZORI ratio**: 0.908
- **City** (Waltham, MA): 124 listings  |  median \$2442/mo  |  median \$2.49/sqft

### Model verdict
- **Snorkel P(SCAM)**: 0.9342  (SCAM)
- **LFs that fired**: price_anomaly(SCAM); template_body(NOT_SCAM); long_detailed_body(NOT_SCAM); weekly_rental(NOT_SCAM)

### Title
> Lease Spacious 1+1. Approx 300 sf of Living Space. Parking Available!

### Body (full)
```
NOTICE: You can now easily reserve our lowest rates available on-line! To unlock these rates, click "Visit the property's management " under the Helpful Details section below, and reserve today!Welcome to Extended Stay America, your solution for short term housing. Enjoy a furnished good price with free utilities, free cable, free Wi-Fi, no lease to sign, and no credit check! means you won't have to pay extra monthly bills for electric, gas, water, cable, or internet, that could mean a savings of several hundred dollars each month!Each of our furnished, pets allowed studios comes equipped with a refrigerator, stove top, microwave, toaster, and coffee maker. You'll also enjoy our convenient on-site laundry facilities and free grab-and-go breakfast every morning. Housekeeping services are also Additional charges may apply. Booking restrictions and taxes apply.
```

---

## Row 55  —  stratum: `top_new`

### Listing
- **Location**: Columbia, MD  (ZIP 21046)
- **Listed price**: \$1470/mo  |  **Effective price**: \$1470/mo
- **Range pattern**: no range pattern detected
- **Size / layout**: 300 sqft  |  1.0 BR  |  1.0 BA
- **Per-bedroom**: \$1470/BR  |  **Per-sqft**: \$4.90
- **Amenities count**: 3  |  **Has photo**: Yes  |  **Source**: RentDigs.com
- **Listing date**: 2019-09-18 02:47:18

### Market context
- **ZORI baseline** (2019-09-30): \$1648/mo  (spatial k-NN, 5 neighbors at ~5.8km)
- **Effective / ZORI ratio**: 0.892
- **City** (Columbia, MD): 352 listings  |  median \$1492/mo  |  median \$1.52/sqft

### Model verdict
- **Snorkel P(SCAM)**: 0.9342  (SCAM)
- **LFs that fired**: price_anomaly(SCAM); template_body(NOT_SCAM); long_detailed_body(NOT_SCAM); weekly_rental(NOT_SCAM)

### Title
> Columbia - superb Apartment nearby fine dining. Pet OK!

### Body (full)
```
NOTICE: You can now easily reserve our lowest rates available on-line! To unlock these rates, click "Visit the property's management " under the Helpful Info section below, and reserve today!Welcome to Extended Stay America, your solution for short term housing. Enjoy a furnished terrific price with free utilities, free cable, free Wi-Fi, no lease to sign, and no credit check! means you won't have to pay extra monthly bills for electric, gas, water, cable, or internet, that could mean a savings of several hundred dollars each month!Each of our furnished, ok for pets studios comes equipped with a refrigerator, stove top, microwave, toaster, and coffee maker. You'll also enjoy our convenient on-site laundry facilities and free grab-and-go breakfast every morning. Housekeeping services are also Additional charges may apply. Booking restrictions and taxes apply.
```

---

## Row 56  —  stratum: `top_new`

### Listing
- **Location**: Los Angeles, CA  (ZIP 90045)
- **Listed price**: \$2420/mo  |  **Effective price**: \$2420/mo
- **Range pattern**: no range pattern detected
- **Size / layout**: 300 sqft  |  1.0 BR  |  1.0 BA
- **Per-bedroom**: \$2420/BR  |  **Per-sqft**: \$8.07
- **Amenities count**: 3  |  **Has photo**: Yes  |  **Source**: RentDigs.com
- **Listing date**: 2019-09-17 21:15:28

### Market context
- **ZORI baseline** (2019-09-30): \$2479/mo  (direct ZIP match (90045))
- **Effective / ZORI ratio**: 0.976
- **City** (Los Angeles, CA): 2,433 listings  |  median \$2603/mo  |  median \$3.28/sqft

### Model verdict
- **Snorkel P(SCAM)**: 0.9342  (SCAM)
- **LFs that fired**: price_anomaly(SCAM); template_body(NOT_SCAM); long_detailed_body(NOT_SCAM); weekly_rental(NOT_SCAM)

### Title
> This Apartment is a must see!

### Body (full)
```
NOTICE: You can now easily reserve our lowest rates available on-line! To unlock these rates, click "Visit the property's management " under the Helpful Info section below, and reserve today!Welcome to Extended Stay America, your solution for short term housing. Enjoy a furnished terrific price with free utilities, free cable, free Wi-Fi, no lease to sign, and no credit check! means you won't have to pay extra monthly bills for electric, gas, water, cable, or internet, that could mean a savings of several hundred dollars each month!Each of our furnished, pets allowed studios comes equipped with a refrigerator, stove top, microwave, toaster, and coffee maker. You'll also enjoy our convenient on-site laundry facilities and free grab-and-go breakfast every morning. Housekeeping services are also Additional charges may apply. Booking restrictions and taxes apply.
```

---

## Row 57  —  stratum: `top_new`

### Listing
- **Location**: Richmond, VA  (ZIP 23224)
- **Listed price**: \$1028/mo  |  **Effective price**: \$1028/mo
- **Range pattern**: no range pattern detected
- **Size / layout**: 1328 sqft  |  2.0 BR  |  1.0 BA
- **Per-bedroom**: \$514/BR  |  **Per-sqft**: \$0.77
- **Amenities count**: 7  |  **Has photo**: Yes  |  **Source**: RentDigs.com
- **Listing date**: 2019-02-22 19:36:25

### Market context
- **ZORI baseline** (2019-02-28): \$1028/mo  (direct ZIP match (23224))
- **Effective / ZORI ratio**: 1.000
- **City** (Richmond, VA): 914 listings  |  median \$1280/mo  |  median \$1.55/sqft

### Model verdict
- **Snorkel P(SCAM)**: 0.9348  (SCAM)
- **LFs that fired**: section8_income(NOT_SCAM); student_housing(NOT_SCAM); template_body(NOT_SCAM); long_detailed_body(NOT_SCAM)

### Title
> This Apartment is a must see. Pet OK!

### Body (full)
```
Take loft living to the next Hudson. We offer newly upgraded one, two, and 3 beds spacious apartments in the lively city of, VA. Our ok for pets community is the definition of industrial chic with its tasteful designs, hallway painting, flexible spaces and coveted amenities. You ll love diving into this full-service apartment experience. Explore the nearby locations such as University of, Huguenot High School, Martin Luther King Jr. Middle School, Blackwell Elementary School, the VCU campus and Carytown. Stroll by the James River, visit the beautiful Forest Hill Park and its stone house known as Boscobel or tour around the historic area of Shockoe Bottom which hosts the Edgar Allan Poe Museum, Adam Craig House as well as various popular restaurants. When the time comes, the Interstate 95 provides for an easy commute to s West End, Short Pump, MCV and many other places.
```

---

## Row 58  —  stratum: `top_new`

### Listing
- **Location**: Raleigh, NC  (ZIP 27608)
- **Listed price**: \$1156/mo  |  **Effective price**: \$1156/mo
- **Range pattern**: no range pattern detected
- **Size / layout**: 300 sqft  |  1.0 BR  |  1.0 BA
- **Per-bedroom**: \$1156/BR  |  **Per-sqft**: \$3.85
- **Amenities count**: 3  |  **Has photo**: Yes  |  **Source**: RentDigs.com
- **Listing date**: 2019-09-18 01:30:44

### Market context
- **ZORI baseline** (2019-09-30): \$1176/mo  (spatial k-NN, 5 neighbors at ~4.6km)
- **Effective / ZORI ratio**: 0.983
- **City** (Raleigh, NC): 865 listings  |  median \$1173/mo  |  median \$1.24/sqft

### Model verdict
- **Snorkel P(SCAM)**: 0.9342  (SCAM)
- **LFs that fired**: price_anomaly(SCAM); template_body(NOT_SCAM); long_detailed_body(NOT_SCAM); weekly_rental(NOT_SCAM)

### Title
> Raleigh, One BR, One BA for rent

### Body (full)
```
NOTICE: You can now easily reserve our lowest rates available on-line! To unlock these rates, click "Visit the property's management " under the Helpful Details section below, and reserve today!Welcome to Extended Stay America, your solution for short term housing. Enjoy a furnished terrific price with free utilities, free cable, free Wi-Fi, no lease to sign, and no credit check! means you won't have to pay extra monthly bills for electric, gas, water, cable, or internet, that could mean a savings of several hundred dollars each month!Each of our furnished, pets allowed studios comes equipped with a refrigerator, stove top, microwave, toaster, and coffee maker. You'll also enjoy our convenient on-site laundry facilities and free grab-and-go breakfast every morning. Housekeeping services are also Additional charges may apply. Booking restrictions and taxes apply.
```

---

## Row 59  —  stratum: `top_new`

### Listing
- **Location**: Kent, WA  (ZIP 98032)
- **Listed price**: \$1530/mo  |  **Effective price**: \$1530/mo
- **Range pattern**: no range pattern detected
- **Size / layout**: 300 sqft  |  1.0 BR  |  1.0 BA
- **Per-bedroom**: \$1530/BR  |  **Per-sqft**: \$5.10
- **Amenities count**: 3  |  **Has photo**: Yes  |  **Source**: RentDigs.com
- **Listing date**: 2019-09-18 02:33:18

### Market context
- **ZORI baseline** (2019-09-30): \$1539/mo  (direct ZIP match (98032))
- **Effective / ZORI ratio**: 0.994
- **City** (Kent, WA): 361 listings  |  median \$1421/mo  |  median \$1.84/sqft

### Model verdict
- **Snorkel P(SCAM)**: 0.9342  (SCAM)
- **LFs that fired**: price_anomaly(SCAM); template_body(NOT_SCAM); long_detailed_body(NOT_SCAM); weekly_rental(NOT_SCAM)

### Title
> $1,530/mo - Kent - Apartment - must see to believe.

### Body (full)
```
NOTICE: You can now easily reserve our lowest rates available on-line! To unlock these rates, click "Visit the property's management " under the Helpful Details section below, and reserve today!Welcome to Extended Stay America, your solution for short term housing. Enjoy a furnished terrific price with free utilities, free cable, free Wi-Fi, no lease to sign, and no credit check! means you won't have to pay extra monthly bills for electric, gas, water, cable, or internet, that could mean a savings of several hundred dollars each month!Each of our furnished, pets allowed studios comes equipped with a refrigerator, stove top, microwave, toaster, and coffee maker. You'll also enjoy our convenient on-site laundry facilities and free grab-and-go breakfast every morning. Housekeeping services are also Additional charges may apply. Booking restrictions and taxes apply.
```

---

## Row 60  —  stratum: `top_new`

### Listing
- **Location**: Denver, CO  (ZIP 80235)
- **Listed price**: \$1339/mo  |  **Effective price**: \$1339/mo
- **Range pattern**: no range pattern detected
- **Size / layout**: 300 sqft  |  1.0 BR  |  1.0 BA
- **Per-bedroom**: \$1339/BR  |  **Per-sqft**: \$4.46
- **Amenities count**: 3  |  **Has photo**: Yes  |  **Source**: RentDigs.com
- **Listing date**: 2019-09-17 21:17:20

### Market context
- **ZORI baseline** (2019-09-30): \$1412/mo  (spatial k-NN, 5 neighbors at ~6.3km)
- **Effective / ZORI ratio**: 0.948
- **City** (Denver, CO): 2,755 listings  |  median \$1499/mo  |  median \$1.84/sqft

### Model verdict
- **Snorkel P(SCAM)**: 0.9342  (SCAM)
- **LFs that fired**: price_anomaly(SCAM); template_body(NOT_SCAM); long_detailed_body(NOT_SCAM); weekly_rental(NOT_SCAM)

### Title
> Denver, Great Location, One BR Apartment. Pet OK!

### Body (full)
```
NOTICE: You can now easily reserve our lowest rates available on-line! To unlock these rates, click "Visit the property's management " under the Helpful Details section below, and reserve today!Welcome to Extended Stay America, your solution for short term housing. Enjoy a furnished good price with free utilities, free cable, free Wi-Fi, no lease to sign, and no credit check! means you won't have to pay extra monthly bills for electric, gas, water, cable, or internet, that could mean a savings of several hundred dollars each month!Each of our furnished, ok for pets studios comes equipped with a refrigerator, stove top, microwave, toaster, and coffee maker. You'll also enjoy our convenient on-site laundry facilities and free grab-and-go breakfast every morning. Housekeeping services are also Additional charges may apply. Booking restrictions and taxes apply.
```

---

