# Retail Intelligence Platform

An AI-native customer intelligence platform that turns public customer review data into actionable insights for Store Operations leaders.

Built entirely with free tools: **Groq** (LLM) · **Yelp Open Dataset** · **Streamlit** · **Plotly**

---

## Modules

| Module | What it does |
|---|---|
| **1. Voice of Customer AI** | Ingests reviews → AI clusters themes, detects store anomalies, writes executive summaries |
| **2. Store Pulse Map** | Interactive map benchmarking every store against its regional peer group |
| **3. Test & Learn Autopilot** | Upload pilot vs control CSVs → statistical significance + scale/kill verdict |
| **4. Analyst Copilot** | Plain-English Q&A chatbot with full dataset context |

---

## Quickstart

### Step 1 — Get the Yelp Dataset (free, one-time)
1. Go to: https://www.yelp.com/dataset
2. Click "Download Dataset" and create a free account
3. Download and extract the TAR file (~4 GB compressed)
4. Place these two files in the `data/` folder:
   - `yelp_academic_dataset_business.json`
   - `yelp_academic_dataset_review.json`

### Step 2 — Get a Groq API key (free, no credit card)
1. Go to: https://console.groq.com
2. Sign up → API Keys → Create Key
3. Copy the key

### Step 3 — Configure environment
```bash
git clone https://github.com/YOUR_USERNAME/retail-intelligence-platform
cd retail-intelligence-platform
pip install -r requirements.txt
cp .env.example .env
# Edit .env and paste your Groq API key
```

### Step 4 — Extract store reviews (run once, ~10 minutes)
```bash
python module1_voice_of_customer/01_extract_reviews.py
```
Outputs `data/businesses.csv` and `data/reviews.csv`.

### Step 5 — Launch
```bash
streamlit run main_app.py
```

---

## Deploy Free on Streamlit Cloud
1. Push repo to GitHub
2. Go to https://streamlit.io/cloud → connect repo
3. Add `GROQ_API_KEY` in Streamlit Secrets
4. Deploy — get a free public URL

---

## Configuration

Edit `config.py` to point the platform at any retail chain in the Yelp dataset:

```python
TARGET_BUSINESS_NAMES = ["your store name"]
```

The Yelp dataset contains 150,000+ businesses across many retail categories.

---

## Project Structure
```
retail-intelligence-platform/
├── main_app.py
├── config.py
├── requirements.txt
├── .env.example
├── data/
│   └── README_get_data.md
├── module1_voice_of_customer/
│   ├── 01_extract_reviews.py
│   ├── voc_analyzer.py
│   └── app.py
├── module2_store_pulse_map/
│   └── app.py
├── module3_test_and_learn/
│   └── app.py
└── module4_analyst_copilot/
    └── app.py
```
