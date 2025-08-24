# Stage 07 – Outliers, Risks & Assumptions

## Overview
In this stage, we explored methods for detecting, removing, and adjusting outliers in a dataset. Outliers can heavily influence statistical summaries and regression models, so handling them carefully is important. We applied multiple approaches and compared how results change **with vs. without outliers**.

## Steps Completed
1. **Data Loading**  
   - Used `data/raw/outliers_homework.csv` (or synthetic fallback).  

2. **Outlier Detection Functions**  
   - `detect_outliers_iqr(series, k=1.5)` → IQR-based method.  
   - `detect_outliers_zscore(series, threshold=3.0)` → Z-score method.  
   - `winsorize_series(series, lower=0.05, upper=0.95)` → Optional capping of extremes.  

3. **Application**  
   - Applied to numeric column (`daily_return`).  
   - Created boolean flags (`outlier_iqr`, `outlier_zscore`).  
   - Generated winsorized series for comparison.  

4. **Sensitivity Analysis**  
   - Compared summary stats (mean, median, std) before vs. after outlier removal.  
   - Fit simple linear regression (`daily_return_2 ~ daily_return`) and compared coefficients/R² with and without outliers.  

5. **Reflection**  
   - Documented assumptions behind IQR, Z-score, and winsorizing.  
   - Discussed impacts on results and risks if assumptions are violated.  

## Key Takeaways
- Outliers significantly affect mean and standard deviation.  
- Regression coefficients and R² shifted once outliers were excluded.  
- Winsorizing is a compromise: keeps all data points but reduces extreme influence.  
- Method choice depends on context (risk modeling vs. explanatory analysis).  

## Deliverables
- Implemented functions with docstrings.  
- Sensitivity comparison (tables/plots).  
- Reflection write-up in Markdown cell.  

---
✅ Functions, ✅ Documentation, ✅ Sensitivity comparison, ✅ Reflection.  
