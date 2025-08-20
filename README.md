“This repo contains a regime-switching signal for statistical arbitrage. It includes reproducible notebooks, source code, and configuration for development.”
# Regime Switch for Statistical Arbitrage
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
Our mean-reversion/pairs strategy tends to bleed on correlation breaks and volatility spikes. We need a daily, rules-driven switch that predicts when the strategy is likely to underperform tomorrow so we can **stand down** and protect capital while keeping Sharpe stable.

## Stakeholder & User
- **Decision owner:** Portfolio Manager (PM).
- **User:** Quant Researcher/Trader operating the stat-arb engine.
- **When/Where:** Signal computed after market close; decision is next-day deployment.

## Useful Answer & Decision
- **Type:** Predictive classification — *Trade* vs *Stand Down* for the next session.
- **Primary metric:** Recall/F1 on “Bad regime” days (minimize trading on bad days); track avoided drawdown and Sharpe delta.
- **Artifact:** Notebook that produces the signal + confusion matrix & next-day PnL comparison; short stakeholder memo.

## Assumptions & Constraints
- No look-ahead; all inputs available T+0 after close.
- Inputs: realized vol (5/20d), cross-sectional dispersion, overnight gap stats, pair residual z-scores, VIX level/changes (if allowed).
- Latency: signal completes within minutes post-close; monthly re-fit for drift.
- Compliance: research only; no non-public data.

## Known Unknowns / Risks
- Regime drift over time → time-split CV + periodic recalibration.
- Class imbalance (bad days rarer) → class weights & threshold tuning.
- Overfitting risk → walk-forward validation and stability checks.

## Lifecycle Mapping
Goal → Stage → Deliverable
- Reduce drawdowns on bad regimes → Stage 01 → README + stakeholder memo


## Goals → Lifecycle → Deliverables Mapping

| Goal                                               | Lifecycle Stage              | Deliverable                          |
|----------------------------------------------------|------------------------------|--------------------------------------|
| Detect when stat-arb strategy is likely to underperform | Data analysis → Modeling      | Regime-switch signal (daily flag)    |
| Protect capital during adverse regimes             | Modeling → Evaluation        | Backtested results showing reduced drawdowns |
| Provide actionable decision support for PM/traders | Deployment → Monitoring      | Trade/Stand-Down recommendation report |
| Maintain stable risk-adjusted returns (Sharpe)     | Evaluation → Iteration       | Performance metrics & monitoring notebook |

- Build baseline model & backtest → Stage 02/03 → Notebook + report
- Integrate with engine → Later stage → CLI/script + monitoring

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

