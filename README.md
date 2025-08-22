

## Repo Plan
`/data/`, `/src/`, `/notebooks/`, `/docs/`; weekly updates; PRs for major changes.

## Stage 06: Data Preprocessing (Cleaning Strategy)

### Approach
This stage standardizes the raw dataset before analysis. We modularized the cleaning into three reusable functions (`src/cleaning.py`) and applied them in `notebooks/stage06_preprocessing.ipynb`.

1. **`fill_missing_median(df)`**  
   - Numeric NaNs are filled with the **median** of that column.  
   - Rationale: Median is robust to skew and outliers compared to mean.

2. **`drop_missing(df, threshold=0.8)`**  
   - Drops columns if **more than 80% of values are missing**.  
   - Rationale: Columns dominated by NaNs add noise if imputed.

3. **`normalize_data(df)`**  
   - Applies Min–Max scaling to numeric columns (→ [0,1]).  
   - If no numeric columns exist, scaling is skipped gracefully.  
   - Rationale: Normalization ensures comparability across features.

---

### Assumptions
- **Categorical/text fields**: left unchanged at this stage (no encoding, no imputation).  
- **Row drops**: not applied unless explicitly required (to avoid reducing sample size).  
- **Numeric parsing**: assumed correct; if a numeric column is read as string (due to $, %, commas), it should be fixed upstream.  
- **No outlier clipping**: outliers are kept for now since removal is highly task-specific.  
- **Guardrails**: If no numeric columns exist (like the current S&P 500 constituents dataset), `fill_missing_median` and `normalize_data` will no-op by design.

---

### Outputs
- **Processed file** saved to: `data/processed/cleaned_<filename>.csv`  
- **Notebook comparison** shows:  
  - Shape before vs after  
  - Missing values per column before vs after  
  - Summary stats of numeric columns (if present)

---

### Trade-offs
- **Imputation vs dropping**: Filling preserves data volume; dropping reduces noise.  
- **Median choice**: Median avoids distortion from outliers, but loses mean-based interpretability.  
- **Min–Max scaling**: Works best when bounded values are desirable; alternative is z-score if Gaussian assumption matters.

