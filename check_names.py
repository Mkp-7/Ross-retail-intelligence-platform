import pandas as pd
import os

biz_path = "data/businesses.csv"
rev_path = "data/reviews.csv"

if os.path.exists(biz_path):
    biz = pd.read_csv(biz_path)
    print("=== businesses.csv ===")
    print("Columns:", list(biz.columns))
    print("Rows:", len(biz))
    print("Sample:\n", biz.head(3).to_string())
else:
    print("businesses.csv NOT FOUND")

if os.path.exists(rev_path):
    rev = pd.read_csv(rev_path)
    print("\n=== reviews.csv ===")
    print("Columns:", list(rev.columns))
    print("Rows:", len(rev))
    print("Sample:\n", rev.head(3).to_string())
else:
    print("reviews.csv NOT FOUND")