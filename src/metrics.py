import numpy as np

def compute_metrics(data):

    returns = data['strategy_returns'].dropna()

    sharpe = np.mean(returns) / np.std(returns) * np.sqrt(252)

    equity = (1 + returns).cumprod()
    peak = np.maximum.accumulate(equity)
    drawdown = (equity - peak) / peak
    max_dd = np.min(drawdown)

    n = len(returns)
    cagr = equity.iloc[-1] ** (252 / n) - 1

    # FIXED TRADE-LEVEL WIN RATE
    trade_returns = data.loc[data['trade'] == 1, 'strategy_returns']
    win_rate = (trade_returns > 0).sum() / len(trade_returns)

    trades = data['trade'].sum()

    return {
        "Sharpe": sharpe,
        "Max Drawdown": max_dd,
        "CAGR": cagr,
        "Win Rate": win_rate,
        "Trades": trades
    }