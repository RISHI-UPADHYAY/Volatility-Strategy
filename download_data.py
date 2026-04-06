import yfinance as yf
import os

os.makedirs("data", exist_ok=True)

spy = yf.download("SPY", start="2015-01-01", end="2024-01-01")

# Reset index so Date becomes a column
spy.reset_index(inplace=True)

# Save clean CSV
spy.to_csv("data/price_data.csv", index=False)

print("SPY data saved.")

# =========================
# DOWNLOAD VIX DATA
# =========================
vix = yf.download("^VIX", start="2015-01-01", end="2024-01-01")

# Reset index so Date becomes a column
vix.reset_index(inplace=True)

# Save clean CSV
vix.to_csv("data/VIX.csv", index=False)

print("VIX data saved.")

print("All data downloaded successfully!")