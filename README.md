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
