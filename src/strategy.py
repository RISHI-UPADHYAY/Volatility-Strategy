def generate_signals(data, window=20, threshold=1.5):

    # Volatility spread
    spread = data["IV"] - data["RV"]

    # Z-score
    rolling_mean = spread.rolling(window).mean()
    rolling_std = spread.rolling(window).std()
    data["z_score"] = (spread - rolling_mean) / rolling_std

    # Volatility regime filter
    data['vol_regime'] = data['RV'] > data['RV'].rolling(50).mean()

    data['signal'] = 0

    # SHORT VOL (IV >> RV)
    data.loc[
        (data['z_score'] > threshold) &
        (data['vol_regime']),
        'signal'
    ] = -1

    # LONG VOL (IV << RV)
    data.loc[
        (data['z_score'] < -threshold) &
        (data['vol_regime']),
        'signal'
    ] = 1

    return data


def apply_holding_period(data, max_holding=5):

    position = 0
    days = 0
    new_signal = []

    for sig in data['signal']:
        if position != 0:
            days += 1

            # Exit if holding too long or signal disappears
            if days >= max_holding or sig == 0:
                position = 0
                days = 0
        else:
            if sig != 0:
                position = sig
                days = 0

        new_signal.append(position)

    data['signal'] = new_signal
    return data