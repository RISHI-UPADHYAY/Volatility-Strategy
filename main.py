from src.volatility import compute_returns, compute_rv, compute_iv
from src.strategy import generate_signals, apply_holding_period
from src.backtester import backtest
from src.greeks import compute_greeks
from src.metrics import compute_metrics

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# LOAD DATA

price_data = pd.read_csv("data/price_data.csv", parse_dates=['Date'])
vix_data = pd.read_csv("data/VIX.csv", parse_dates=['Date'])

# Keep only required columns
price_data = price_data[['Date', 'Close']]
vix_data = vix_data[['Date', 'Close']]

# Merge datasets
data = pd.merge(price_data, vix_data, on='Date', how='inner')

# Rename columns
data.rename(columns={'Close_x': 'Close', 'Close_y': 'VIX'}, inplace=True)

# Sort data (VERY IMPORTANT)
data = data.sort_values('Date').reset_index(drop=True)


# FIX DATA TYPES (CRITICAL)

data['Close'] = pd.to_numeric(data['Close'], errors='coerce')
data['VIX'] = pd.to_numeric(data['VIX'], errors='coerce')

# Drop missing values early
data = data.dropna().reset_index(drop=True)


# PIPELINE
data = compute_returns(data)
data = compute_rv(data)
data = compute_iv(data)
data = compute_greeks(data)
data = generate_signals(data)
data = apply_holding_period(data)
data = backtest(data)

# Drop NaNs from rolling calculations
data = data.dropna().reset_index(drop=True)


# METRICS

results = compute_metrics(data)

print("\n===== PERFORMANCE METRICS =====")
for k, v in results.items():
    print(f"{k}: {v}")


# PLOTS

# Strategy vs Market
plt.figure(figsize=(10,5))
plt.plot(data['cumulative_market'], label='Market')
plt.plot(data['cumulative_strategy'], label='Strategy')
plt.legend()
plt.title("Strategy vs Market")
plt.show()

# Drawdown
equity = data['cumulative_strategy']
peak = equity.cummax()
drawdown = (equity - peak) / peak

plt.figure(figsize=(10,5))
plt.plot(drawdown)
plt.title("Drawdown")
plt.show()