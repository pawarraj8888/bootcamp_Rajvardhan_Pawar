# Stage 06 — Data Preprocessing

## Goal
Create modular cleaning functions and apply them to the raw dataset. Save the cleaned dataset in multiple formats, update documentation, and keep everything reproducible.

---

## Workflow

1. **Functions in `src/cleaning.py`**
   - `drop_missing(df, thresh=0.95)`: drops columns with too many missing values.
   - `fill_missing_median(df, cols=None)`: fills numeric NaNs with the median.
   - `normalize_data(df, cols=None, method='zscore'|'minmax')`: scales numeric columns.

2. **Notebook Steps**
   - Load raw dataset from `./data/raw/`.
   - Apply cleaning functions in sequence:
     1. Drop columns with excessive missing values.  
     2. Fill numeric missing values with column medians.  
     3. Normalize numeric columns using z-score scaling.  
   - Compare original vs cleaned (shape, missingness).
   - Save final cleaned dataset.

3. **Outputs**
   - Cleaned CSV → `./data/processed/sample_data_cleaned.csv`
   - Cleaned Parquet → `./data/processed/sample_data_cleaned.parquet`
   - SQLite DB → `./data/processed/project.db` with tables:
     - `raw_sample` (raw data)  
     - `cleaned_sample` (cleaned data)

---

## Assumptions & Cleaning Strategy
- Columns with \<90% non-null values dropped.  
- Numeric NaNs replaced with column medians.  
- Categorical/text NaNs left untouched for later encoding.  
- Normalized numeric features (`age`, `income`, `credit_score`) with z-scores.  
- Data paths are relative (`./data/raw`, `./data/processed`) for reproducibility.  

---

## Requirements
- Python 3.9+  
- `pandas`, `numpy`, `sqlite3`, `pyarrow` (for Parquet), `python-dotenv`  

---

## Submission
- `src/cleaning.py`
- Preprocessing notebook
- Updated README (this file)
- Processed dataset (CSV, Parquet, DB)
