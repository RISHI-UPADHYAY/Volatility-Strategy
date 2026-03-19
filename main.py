from src.data_loader import load_data
from src.volatility import compute_returns, compute_rv, compute_iv
from src.strategy import generate_signals, apply_holding_period
from src.backtester import backtest
from src.greeks import compute_greeks


import numpy as np
import matplotlib.pyplot as plt

# Load data
data = load_data('AAPL')

# Pipeline
data = compute_returns(data)
data = compute_rv(data)
data = compute_iv(data)
data = compute_greeks(data)
data = generate_signals(data)
data = apply_holding_period(data)
data = backtest(data)


#Sharpe Ratio
sharpe = (data['strategy_returns'].mean() / data['strategy_returns'].std()) * np.sqrt(252)

#Max Drawdown
cum = data['cumulative_strategy']
peak = cum.cummax()
drawdown = (cum - peak) / peak

#CAGR
years = len(data)/252
cagr = data['cumulative_strategy'].iloc[-1] ** (1/years) - 1

#Trades
num_trades = data['trade'].sum()

print("CAGR: ", cagr)
print("Number of trades: ", num_trades)

print("Sharpe Ratio: ", sharpe)
print("Max Drawdown: ", drawdown.min())

# Plot
plt.figure(figsize=(10,5))
plt.plot(data['cumulative_market'], label='Market')
plt.plot(data['cumulative_strategy'], label='Strategy')
plt.legend()
plt.title("Strategy vs Market")
plt.show()

plt.figure(figsize=(10,5))
plt.plot(drawdown)
plt.title("Drawdown")
plt.show()