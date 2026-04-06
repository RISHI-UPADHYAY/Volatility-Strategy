import numpy as np

def compute_returns(data):
    data['returns'] = np.log(data['Close'] / data['Close'].shift(1))
    return data

def compute_rv(data, window=20):
    data['RV'] = data['returns'].rolling(window).std() * np.sqrt(252)
    return data

def compute_iv(data):
    # Use VIX as implied volatility proxy
    if 'VIX' not in data.columns:
        raise ValueError("VIX column required for real implied volatility")

    data['IV'] = data['VIX'] / 100 
    return data