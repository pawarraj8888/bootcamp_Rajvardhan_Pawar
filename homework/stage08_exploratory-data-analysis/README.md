# Stage 08 — Exploratory Data Analysis (EDA)

## Overview
In this stage, we performed a comprehensive exploratory data analysis (EDA) on the project dataset.  
The goal was to understand variable distributions, relationships, and potential data quality issues before moving on to preprocessing and modeling.

---

## Steps Completed
1. **Dataset Profiling**  
   - Used `.info()` and `.describe()` for summary statistics.  
   - Checked missing values and data types.  

2. **Distributional Analysis**  
   - Histograms and boxplots for `age`, `income`, `transactions`, and `spend`.  
   - Identified skewness, spread, and outliers.  

3. **Bivariate Relationships**  
   - Scatterplots of `income vs. spend` and `transactions vs. spend`.  
   - Regional differences visualized via color grouping.  

4. **Correlation Analysis**  
   - Generated a heatmap of numeric features.  
   - Found `transactions` and `spend` to have the strongest correlation (0.48).  

5. **Findings, Risks, and Assumptions**  
   - Spending is more strongly driven by **number of transactions** than **income**.  
   - Synthetic data includes injected missingness and outliers that must be handled.  
   - Assumed relationships are linear; non-linear effects may exist.  

6. **Implications for Next Step**  
   - Plan to handle missing values (imputation or removal).  
   - Consider capping/winsorizing outliers.  
   - Normalize/scale numeric variables and encode categorical (`region`).  
   - Engineer features around **transaction frequency** for future modeling.  

---

## Deliverables
- **EDA Notebook** with profiling, visualizations, and markdown interpretation.  
- **Plots**: Histograms, boxplots, scatterplots, and a correlation heatmap.  
- **Documentation**: Findings, risks, assumptions, and next-step plan.  


