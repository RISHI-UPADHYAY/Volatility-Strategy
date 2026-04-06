import numpy as np

def backtest(data, cost=0.001):

    data['vol'] = data['returns'].rolling(20).std()

    
    data['position'] = data['signal'] / data['vol']

    # Handle NaNs and extreme values
    data['position'] = data['position'].replace([np.inf, -np.inf], 0).fillna(0)

    # Moderate cap (not too restrictive)
    data['position'] = data['position'].clip(-5, 5)

    
    # STRATEGY RETURNS
    data['strategy_returns'] = data['position'].shift(1) * data['returns']

    
    # TRADE DETECTION
    data['trade'] = (data['position'] != data['position'].shift(1)).astype(int)

    
    # TRANSACTION COST + SLIPPAGE
    data['strategy_returns'] -= data['trade'] * (cost + 0.0005)

    
    data['strategy_returns'] = np.clip(data['strategy_returns'], -0.05, 0.07)

    
    data['cumulative_strategy'] = (1 + data['strategy_returns']).cumprod()
    data['cumulative_market'] = (1 + data['returns']).cumprod()

    return data