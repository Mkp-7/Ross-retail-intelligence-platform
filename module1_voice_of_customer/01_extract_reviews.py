"""
Step 1 — Extract target store reviews from the Yelp Open Dataset.

Edit config.py to set TARGET_BUSINESS_NAMES before running.

Usage:
    python module1_voice_of_customer/01_extract_reviews.py

Output:
    data/businesses.csv
    data/reviews.csv
"""

import json
import csv
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import (
    TARGET_BUSINESS_NAMES,
    YELP_BUSINESS_JSON,
    YELP_REVIEW_JSON,
    BUSINESSES_CSV,
    REVIEWS_CSV,
    DATA_DIR,
)

try:
    from tqdm import tqdm
except ImportError:
    def tqdm(iterable, **kwargs):
        return iterable


def matches_target(name: str) -> bool:
    name_lower = name.lower()
    return any(t.lower() in name_lower for t in TARGET_BUSINESS_NAMES)


def extract_businesses() -> set:
    print(f"\nStep 1/2 — Scanning businesses in Yelp dataset...")
    print(f"Looking for: {TARGET_BUSINESS_NAMES}")

    if not os.path.exists(YELP_BUSINESS_JSON):
        print(f"\nERROR: File not found: {YELP_BUSINESS_JSON}")
        print("See data/README_get_data.md for download instructions.")
        return set()

    matched_ids = set()
    matched_rows = []

    with open(YELP_BUSINESS_JSON, "r", encoding="utf-8") as f:
        for line in tqdm(f, desc="Scanning"):
            line = line.strip()
            if not line:
                continue
            try:
                biz = json.loads(line)
                if matches_target(biz.get("name", "")):
                    matched_ids.add(biz["business_id"])
                    matched_rows.append({
                        "business_id":  biz["business_id"],
                        "name":         biz.get("name", ""),
                        "address":      biz.get("address", ""),
                        "city":         biz.get("city", ""),
                        "state":        biz.get("state", ""),
                        "postal_code":  biz.get("postal_code", ""),
                        "latitude":     biz.get("latitude", ""),
                        "longitude":    biz.get("longitude", ""),
                        "stars":        biz.get("stars", ""),
                        "review_count": biz.get("review_count", 0),
                        "is_open":      biz.get("is_open", 1),
                    })
            except json.JSONDecodeError:
                continue

    if matched_rows:
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(BUSINESSES_CSV, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=matched_rows[0].keys())
            writer.writeheader()
            writer.writerows(matched_rows)
        print(f"\nFound {len(matched_rows)} locations → saved to {BUSINESSES_CSV}")
    else:
        print("\nNo matching locations found. Check TARGET_BUSINESS_NAMES in config.py.")

    return matched_ids


def extract_reviews(target_ids: set) -> None:
    if not target_ids:
        print("\nNo business IDs to filter. Skipping review extraction.")
        return

    print(f"\nStep 2/2 — Extracting reviews for {len(target_ids)} locations...")
    print("This reads a 5+ GB file — takes 5–10 minutes.")

    if not os.path.exists(YELP_REVIEW_JSON):
        print(f"\nERROR: File not found: {YELP_REVIEW_JSON}")
        print("See data/README_get_data.md for download instructions.")
        return

    rows = []

    with open(YELP_REVIEW_JSON, "r", encoding="utf-8") as f:
        for line in tqdm(f, desc="Scanning", mininterval=2.0):
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
                if r.get("business_id") in target_ids:
                    rows.append({
                        "review_id":   r.get("review_id", ""),
                        "business_id": r.get("business_id", ""),
                        "user_id":     r.get("user_id", ""),
                        "stars":       r.get("stars", ""),
                        "date":        r.get("date", ""),
                        "text":        r.get("text", "").replace("\n", " ").strip(),
                        "useful":      r.get("useful", 0),
                        "funny":       r.get("funny", 0),
                        "cool":        r.get("cool", 0),
                    })
            except json.JSONDecodeError:
                continue

    if rows:
        with open(REVIEWS_CSV, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
        print(f"\nExtracted {len(rows):,} reviews → saved to {REVIEWS_CSV}")
    else:
        print("\nNo reviews found for these locations.")


def main():
    print("=" * 55)
    print("  Retail Intelligence Platform — Data Extractor")
    print("=" * 55)
    os.makedirs(DATA_DIR, exist_ok=True)
    ids = extract_businesses()
    extract_reviews(ids)
    print("\n" + "=" * 55)
    print("  Done. Run: streamlit run main_app.py")
    print("=" * 55 + "\n")


if __name__ == "__main__":
    main()
