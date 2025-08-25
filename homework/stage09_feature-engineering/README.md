# Stage 09 — Feature Engineering

## Overview
In this stage, we extended our project dataset by creating new **engineered features** from raw stock price data.  
We replaced the starter synthetic dataset with real financial data (MSFT & AAPL), aligning this stage with our overall **Regime Switch for Statistical Arbitrage** project.

## Steps Completed
1. **Data Acquisition**
   - Pulled daily adjusted close prices for MSFT and AAPL using `yfinance`.
   - Saved raw dataset to `data/raw/prices_msft_aapl.csv`.

2. **Feature Engineering**
   Implemented 3 new features:
   - **Spread Z-Score**  
     Standardized measure of how far the MSFT–AAPL spread deviates from its 20-day rolling mean.  
     Helps detect mean-reversion vs. divergence regimes.  

   - **Volatility Ratio (5d / 20d)**  
     Compares short-term vs. long-term realized volatility of MSFT returns.  
     Captures volatility regime shifts where strategies may underperform.  

   - **Spread Momentum** *(optional)*  
     First difference of the spread, highlighting sudden directional jumps that may signal regime changes.

3. **Outputs**
   - Saved engineered dataset with new features to `data/processed/features_stat_arb.csv`.
   - Documented rationale for each feature in the notebook.
   - Included optional plots and correlation checks.

## File Locations
- Notebook: `notebooks/stage09_feature-engineering_homework-starter.ipynb`
- Raw data: `data/raw/prices_msft_aapl.csv`
- Processed data: `data/processed/features_stat_arb.csv`

