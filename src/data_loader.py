import yfinance as yf

def load_data(symbol):
    data = yf.download(symbol, period="5y", interval="1d")

    if data.empty:
        raise ValueError("No data fetched")

    #  FIX: flatten columns
    if isinstance(data.columns, tuple) or hasattr(data.columns, "levels"):
        data.columns = data.columns.get_level_values(0)

    # Keep only Close as Series
    data = data[['Close']].copy()

    return data