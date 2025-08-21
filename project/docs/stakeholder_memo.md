# Stakeholder Memo: Regime Switch for Statistical Arbitrage

**To:** Portfolio Manager  
**From:** Rajvardhan Pawar, Quant Researcher  
**Date:** August 15th 2025  

---

### Context
Our statistical arbitrage strategy (pairs/mean reversion) sometimes underperforms badly when correlations break or volatility spikes.  
We propose a daily **regime-switching signal** to decide when to **trade vs. stand down**, protecting capital during unstable regimes.

---

### Goals
- Protect capital on “bad regime” days.  
- Maintain stable Sharpe ratio over time.  
- Provide a simple daily output: **Trade / Stand Down**.  

---

### Stakeholder Impact
- **PM**: Improved risk-adjusted performance and reduced drawdowns.  
- **Traders**: Clear rules on when to pause trading, avoiding bleed.  
- **Firm**: Stronger capital preservation and smoother equity curve.  

---

### Next Steps
1. Build initial prototype using volatility & correlation breakdown features.  
2. Backtest predictive accuracy of the signal.  
3. Deploy decision rule for live next-day trading.
