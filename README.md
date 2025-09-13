# Safeway Price Index (Bay Area) — 2022–Present

**Goal:** Quantify how advertised grocery prices at Bay Area Safeway stores have changed since Jan 2022, with special focus on the **difference between non-app shelf prices** and **digital/app prices**.

## Outputs
- **RSPI (Regular/Shelf Price Index):** price level faced by non-app shoppers (no clip, no digital).
- **MPI (Member/Club Index):** loyalty price requiring a card, not necessarily an app clip.
- **DPI (Digital/App Price Index):** prices requiring digital “Just for U”/in-app clipping.
- **App Advantage:** RSPI – DPI (and RSPI/DPI ratio) over time.
- Comparison overlay with **BLS San Francisco “Food at home” CPI**.

## Data sources
- Archived Safeway weekly ads/product pages via the Internet Archive (Wayback/CDX APIs).
- Archived third-party circular mirrors (e.g., Flipp) for static images/HTML of the same ads.
- Public BLS/FRED series for contextual comparison.

## Method (short)
1. Enumerate archived URLs (2022-01 → present) for our 3 target Bay Area stores using the **CDX API**.
2. Download ad pages and product pages; parse **item, size, price** and **promo text** (OCR+HTML).
3. Flag promos using `src/config/promo_rules.yaml`; extract **regular**, **member**, and **digital** prices when present.
4. Normalize to unit prices; build weekly → monthly series for RSPI/MPI/DPI.
5. Publish charts & CSVs; compare to BLS; document coverage and limitations.

## Setup
```bash
conda env create -f environment.yml
conda activate safeway-index
jupyter lab
