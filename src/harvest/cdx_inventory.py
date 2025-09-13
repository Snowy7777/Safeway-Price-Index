# src/harvest/cdx_inventory.py
# Fetch CDX capture listings for your seed URLs and save JSONL files.

import json
import pathlib
import time
from typing import List, Dict, Iterable
import requests

CDX_ENDPOINT = "https://web.archive.org/cdx/search/cdx"

# --- Your three stores (exact URLs you provided) ---
SEED_URLS = [
    "https://local.safeway.com/safeway/ca/oakland/3550-fruitvale-ave.html",
    "https://local.safeway.com/safeway/ca/pleasanton/1701-santa-rita-rd.html",
    "https://local.safeway.com/safeway/ca/san-francisco/4950-mission-st.html",
]

# --- Optional: add extra seeds that often contain weekly-ad content ---
OPTIONAL_URLS = [
    "https://www.safeway.com/weeklyad/",
    "https://flipp.com/en-us/stores/safeway/",
]

FIELDS = ["timestamp", "original", "mimetype", "statuscode", "digest", "length"]

def cdx_query(
    url: str,
    from_date: str = "20220101",
    to_date: str = "20250913",
    match_type: str = "prefix",
    filters: List[str] | None = None,
    collapse: str | None = "digest",
    limit: int | None = None,
    gzip: bool = False,
    session: requests.Session | None = None,
) -> List[Dict]:
    """Query the IA CDX API and return a list of dict rows (header mapped to values)."""
    s = session or requests.Session()
    params = {
        "url": url if match_type != "prefix" or url.endswith("/*") else f"{url}/*",
        "output": "json",
        "from": from_date,
        "to": to_date,
        "fl": ",".join(FIELDS),   # field order (aka 'fl' param)
        "matchType": match_type,  # exact | prefix | host | domain
        "gzip": "false" if not gzip else "true",
    }
    if filters:
        # multiple 'filter' params are allowed
        params_list = []
        for k, v in params.items():
            params_list.append((k, v))
        for f in filters:
            params_list.append(("filter", f))
        params = params_list
    if collapse:
        # collapse by content digest to reduce duplicates
        if isinstance(params, list):
            params.append(("collapse", collapse))
        else:
            params["collapse"] = collapse
    if limit:
        if isinstance(params, list):
            params.append(("limit", str(limit)))
        else:
            params["limit"] = str(limit)

    resp = s.get(CDX_ENDPOINT, params=params, timeout=45)
    resp.raise_for_status()
    data = resp.json()
    if not data:
        return []
    header, *rows = data
    return [dict(zip(header, r)) for r in rows]

def save_jsonl(rows: Iterable[Dict], out_path: pathlib.Path):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

def inventory():
    out_dir = pathlib.Path("data/raw/cdx")
    s = requests.Session()

    seeds = []
    seeds.extend(SEED_URLS)
    seeds.extend(OPTIONAL_URLS)

    for url in seeds:
        print(f"[CDX] Querying: {url}")
        rows = cdx_query(
            url=url,
            from_date="20220101",
            to_date="20250913",
            match_type="prefix",                 # use 'prefix' or tailor per-URL
            filters=["statuscode:200"],          # only successful captures to start
            collapse="digest",
            gzip=False,
            session=s,
        )
        # Save as one file per seed
        safe_name = (
            url.replace("https://", "")
               .replace("http://", "")
               .replace("/", "_")
               .strip("_")
        )
        out_path = out_dir / f"{safe_name}.jsonl"
        save_jsonl(rows, out_path)
        print(f"  -> {len(rows)} rows -> {out_path}")
        time.sleep(1.0)  # be gentle to IA

if __name__ == "__main__":
    inventory()
