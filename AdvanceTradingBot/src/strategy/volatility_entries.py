def detect_volatility_spike(data):
if len(data) < 20:
return False

volume_ratio = data['volume'][-1] / data['volume'].mean()
bb_width = (data['upper_band'][-1] - data['lower_band'][-1]) / data['sma'][-1]
return volume_ratio > 2.5 and bb_width < 0.04
