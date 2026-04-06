# Volatility Trading Strategy

## Overview
This project implements a volatility-based trading strategy using the spread between implied volatility (IV) and realized volatility (RV). The strategy is designed to capture mispricing in volatility by identifying periods where implied volatility deviates significantly from realized volatility.

---

## Strategy Idea

- Implied Volatility (IV) is proxied using VIX
- Realized Volatility (RV) is computed from rolling log returns
- The strategy trades on the **IV - RV spread**

### Signal Logic:
- **Short Volatility** when IV >> RV (overpriced volatility)
- **Long Volatility** when IV << RV (underpriced volatility)

Signals are generated using **rolling z-scores** of the volatility spread.

---

## Features

- Rolling realized volatility estimation
- Implied volatility proxy using VIX
- Z-score based signal generation
- Volatility regime filtering
- Volatility-scaled position sizing
- Transaction cost and slippage modeling
- Risk management via position caps and stop-loss
- Backtesting with performance evaluation

---

## Data

- Underlying: SPY (S&P 500 ETF)
- Implied Volatility Proxy: VIX
- Frequency: Daily data
- Period: 2015 – 2024

---

## Backtesting Framework

The strategy follows a modular pipeline:

1. Data Loading & Cleaning
2. Feature Engineering (returns, RV, IV)
3. Signal Generation (z-score of IV-RV spread)
4. Position Sizing (volatility scaling)
5. Execution Simulation (with costs)
6. Performance Evaluation

---

## Results

| Metric        | Value |
|--------------|------|
| Sharpe Ratio | 0.69 |
| CAGR         | 13.7% |
| Max Drawdown | -24% |
| Win Rate     | 17.6% |
| Trades       | 222 |

---

## Key Insights

- The strategy exhibits **low win rate but positive expectancy**, driven by large gains during volatility dislocations.
- Performance is **asymmetric**, with occasional large profits offsetting frequent small losses.
- Risk management significantly reduces drawdowns while preserving signal quality.

---


## How to Run

1. Install dependencies: pip install -r requirements.txt


2. Download data: python download_data.py


3. Run the strategy: python main.py


---

## Future Improvements

- Use options data instead of VIX proxy
- Incorporate volatility term structure (VIX vs VIX3M)
- Add walk-forward validation
- Extend to multi-asset portfolios
- Improve execution modeling