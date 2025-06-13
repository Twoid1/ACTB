class HybridRouter:
def __init__(self, threshold_a=0.8, threshold_b=0.4):
self.threshold_a = threshold_a
self.threshold_b = threshold_b

def route_signal(self, opportunity):
if opportunity.get('fundamental_score', 0) > self.threshold_a:
return {
'system': 'A',
'position_size': 'full',
'hold_time': '60-120 min',
'profit_target': '2.5%',
'stop_loss': '1.2%'
}
elif opportunity.get('technical_score', 0) > 0.7:
return {
'system': 'hybrid',
'position_size': 'medium',
'hold_time': '30-45 min',
'profit_target': '1.8%',
'stop_loss': '0.9%'
}
elif opportunity.get('volatility', 0) > 0.08:
return {
'system': 'B',
'position_size': 'small',
'hold_time': '10-20 min',
'profit_target': '1.2%',
'stop_loss': '0.6%'
}
return None
