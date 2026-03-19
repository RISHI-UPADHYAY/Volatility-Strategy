import numpy as np
from scipy.stats import norm

def compute_greeks(data, T=30/252, r=0.01):
    # Convert to numpy arrays (fixes shape issues)
    S = data['Close'].values
    sigma = data['RV'].values

    # Avoid division by zero
    sigma = np.where(sigma == 0, np.nan, sigma)

    # ATM assumption → log(S/K)=0
    d1 = (r + 0.5 * sigma**2) * T / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    delta = norm.cdf(d1)
    vega = S * norm.pdf(d1) * np.sqrt(T)
    theta = - (S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))

    # Assign back to dataframe
    data['delta'] = delta
    data['vega'] = vega
    data['theta'] = theta

    return data