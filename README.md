# Volatility Trading Strategy (IV vs RV)

## 📌 Overview
This project implements a volatility-based trading strategy that exploits the divergence between **Implied Volatility (IV)** and **Realized Volatility (RV)**.

The strategy uses statistical signals (Z-score) and incorporates transaction costs and risk metrics to simulate realistic trading performance.

---

## 🧠 Strategy Idea

- **Realized Volatility (RV):** Computed from historical returns
- **Implied Volatility (IV):** Approximated using rolling average of RV
- **Signal:** Based on Z-score of (IV - RV)

### Trading Logic:
- If Z-score > threshold → **Sell volatility**
- If Z-score < -threshold → **Buy volatility**

---

## ⚙️ Features

- Rolling volatility estimation (RV)
- Proxy implied volatility (IV)
- Z-score based signal generation
- Holding period to reduce overtrading
- Transaction cost modeling
- Backtesting engine
- Performance metrics (Sharpe Ratio, CAGR, Drawdown)
- Greeks calculation (Delta, Vega, Theta) using Black-Scholes approximation

---

## 📊 Results

- Strategy vs Market performance plotted
- Drawdown visualization
- Trade statistics and risk-adjusted metrics

---

## 🧪 Key Insights

- Strategy performs better during stable volatility regimes
- Performance degrades during sudden volatility spikes
- Vega filtering improves trade quality by focusing on high sensitivity periods

---

## 🛠️ Tech Stack

- Python
- pandas, numpy
- matplotlib
- yfinance
- scipy

---

## 📂 Project Structure
# Volatility Trading Strategy (IV vs RV)

## 📌 Overview
This project implements a volatility-based trading strategy that exploits the divergence between **Implied Volatility (IV)** and **Realized Volatility (RV)**.

The strategy uses statistical signals (Z-score) and incorporates transaction costs and risk metrics to simulate realistic trading performance.

---

## 🧠 Strategy Idea

- **Realized Volatility (RV):** Computed from historical returns
- **Implied Volatility (IV):** Approximated using rolling average of RV
- **Signal:** Based on Z-score of (IV - RV)

### Trading Logic:
- If Z-score > threshold → **Sell volatility**
- If Z-score < -threshold → **Buy volatility**

---

## ⚙️ Features

- Rolling volatility estimation (RV)
- Proxy implied volatility (IV)
- Z-score based signal generation
- Holding period to reduce overtrading
- Transaction cost modeling
- Backtesting engine
- Performance metrics (Sharpe Ratio, CAGR, Drawdown)
- Greeks calculation (Delta, Vega, Theta) using Black-Scholes approximation

---

## 📊 Results

- Strategy vs Market performance plotted
- Drawdown visualization
- Trade statistics and risk-adjusted metrics

---

## 🧪 Key Insights

- Strategy performs better during stable volatility regimes
- Performance degrades during sudden volatility spikes
- Vega filtering improves trade quality by focusing on high sensitivity periods

---

## 🛠️ Tech Stack

- Python
- pandas, numpy
- matplotlib
- yfinance
- scipy

---
## 📂 Project Structure

volatility-strategy/
│
├── src/
│ ├── data_loader.py
│ ├── volatility.py
│ ├── greeks.py
│ ├── strategy.py
│ ├── backtester.py
│
├── main.py
├── requirements.txt
└── README.md


---

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py