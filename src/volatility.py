import numpy as np

def compute_returns(data):
    data['returns'] = np.log(data['Close'] / data['Close'].shift(1))
    return data

def compute_rv(data, window=20):
    data['RV'] = data['returns'].rolling(window).std() * np.sqrt(252)
    return data

def compute_iv(data):
    data['IV'] = data['RV'].rolling(5).mean()
    return data