"""
Configuration — edit this file to target any retail chain.

To use with a different company:
1. Update TARGET_BUSINESS_NAMES with name variations to match
2. Update PLATFORM_TITLE and PLATFORM_SUBTITLE for the UI
3. Re-run: python module1_voice_of_customer/01_extract_reviews.py
"""

TARGET_BUSINESS_NAMES = [
    "Ross Dress For Less",
    "Ross Dress for Less",
]

PLATFORM_TITLE    = "Retail Intelligence Platform"
PLATFORM_SUBTITLE = "Customer Insights & Store Operations"
PLATFORM_ICON     = "🏪"

GROQ_MODEL = "groq/compound-mini"

DATA_DIR          = "data"
BUSINESSES_CSV    = "data/businesses.csv"
REVIEWS_CSV       = "data/reviews.csv"

YELP_BUSINESS_JSON = "data/yelp_academic_dataset_business.json"
YELP_REVIEW_JSON   = "data/yelp_academic_dataset_review.json"

ANOMALY_THRESHOLD_STARS   = 0.4
PEER_GROUP_COLUMN         = "state"
SIGNIFICANT_DELTA_STARS   = 0.3
