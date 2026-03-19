def generate_signals(data, window=20, threshold=0.02):
    spread = data["IV"] - data["RV"]

    rolling_mean = spread.rolling(window).mean()
    rolling_std = spread.rolling(window).std()

    data["z_score"] = (spread - rolling_mean) / rolling_std

    data['signal'] = 0

    #Use Vega as filter
    data.loc[(data['z_score'] > threshold) & (data['vega'] > data['vega'].median()), 'signal'] = -1
    data.loc[(data['z_score'] < -threshold) & (data['vega'] > data['vega'].median()), 'signal'] = 1

    return data


def apply_holding_period(data, holding_period=5):
    current_signal = 0
    hold_days = 0

    new_signals = []

    for signal in data['signal']:
        if hold_days > 0 :
            new_signals.append(current_signal)
            hold_days -= 1
        else:
            current_signal = signal
            new_signals.append(signal)
            if signal != 0:
                hold_days = holding_period
    
    data['signal'] = new_signals
    return data