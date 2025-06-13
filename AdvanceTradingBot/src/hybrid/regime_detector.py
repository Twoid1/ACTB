class MarketRegimeDetector:
def __init__(self):
self.regime = "neutral"

def update_regime(self, volatility, trend_strength):
if volatility > 0.08 and trend_strength > 0.7:
self.regime = "bull_strong"
elif volatility > 0.08 and trend_strength < -0.7:
self.regime = "bear_strong"
elif volatility > 0.06:
self.regime = "high_volatility"
elif volatility < 0.03:
self.regime = "low_volatility"
else:
self.regime = "neutral"
return self.regime

def get_strategy_weights(self):
return {
'bull_strong': {'A': 0.6, 'hybrid': 0.3, 'B': 0.1},
'bear_strong': {'A': 0.3, 'hybrid': 0.4, 'B': 0.3},
'high_volatility': {'A': 0.2, 'hybrid': 0.3, 'B': 0.5},
'low_volatility': {'A': 0.7, 'hybrid': 0.2, 'B': 0.1},
'neutral': {'A': 0.5, 'hybrid': 0.3, 'B': 0.2}
}.get(self.regime, {'A': 0.5, 'hybrid': 0.3, 'B': 0.2})
