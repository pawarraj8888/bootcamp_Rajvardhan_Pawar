# Stage 4 — Data Acquisition and Ingestion

## Overview
In this stage, we pulled financial data from an API and scraped a public table.  
All outputs are stored in `data/raw/` with timestamped filenames.

---

## Steps

### 1. API Pull
- Tried **Alpha Vantage** (with API key from `.env`).
- If not available, fallback to **Yahoo Finance (`yfinance`)**.
- Standardized columns: `Date, Open, High, Low, Close, Adj Close, Volume`.
- Saved raw CSV → `data/raw/<TICKER>_<source>_<timestamp>.csv`.

### 2. Table Scrape
- Source: [Wikipedia — List of S&P 500 companies](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies).
- Parsed with **BeautifulSoup**, built a DataFrame.
- Validated text/numeric columns.
- Saved raw CSV → `data/raw/sp500_constituents_<timestamp>.csv`.

### 3. Documentation
- `.env` holds secrets (not committed).  
- `.env.example` is committed as a template.  
- Validation rules ensure required columns and no empty data.  
- Risks: schema changes or API rate limits.

---

## Usage
```bash
# Setup
pip install -r requirements.txt
cp .env.example .env   # add your API key if using Alpha Vantage
