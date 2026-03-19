def backtest(data, cost=0.001):
    data['strategy_returns'] = data['signal'].shift(1) * data['returns']

    data['trade'] = data['signal'].diff().abs()

    data['strategy_returns'] -= data['trade'] * cost

    data['cumulative_market'] = (1 + data['returns']).cumprod()
    data['cumulative_strategy'] = (1 + data['strategy_returns']).cumprod()

    return data