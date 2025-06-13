class HybridRouter:
def __init__(self, threshold_a=0.78, threshold_b=0.42):
self.threshold_a = threshold_a
self.threshold_b = threshold_b

def route_signal(self, opportunity):
# Core system A for high-confidence, fundamental plays
if (opportunity['fundamental_score'] > self.threshold_a and
opportunity['asset_class'] in ['large_cap', 'medium_cap']):
return {
'system': 'A',
'position_size': 'full',
'hold_time': '60-120 min',
'profit_target': '2.5%',
'stop_loss': '1.2%'
}

# Hybrid for medium-confidence opportunities
elif (opportunity['technical_score'] > 0.7 and
opportunity['sentiment_score'] > 0.6):
return {
'system': 'hybrid',
'position_size': 'medium',
'hold_time': '30-45 min',
'profit_target': '1.8%',
'stop_loss': '0.9%'
}

# System B for speculative, high-velocity plays
elif (opportunity['volatility'] > 0.08 and
opportunity['volume_ratio'] > 3.0 and
opportunity['liquidity'] > 500000):
return {
'system': 'B',
'position_size': 'small',
'hold_time': '10-20 min',
'profit_target': '1.2%',
'stop_loss': '0.6%'
}

return None

def update_thresholds(self, performance_data):
# Adaptive threshold adjustment
if performance_data['win_rate'] > 0.68:
self.threshold_a *= 0.98
self.threshold_b *= 0.97
elif performance_data['win_rate'] < 0.60:
self.threshold_a *= 1.02
self.threshold_b *= 1.03
