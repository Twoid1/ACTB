class CapitalAllocator:
def __init__(self, total_capital):
self.total_capital = total_capital
self.system_allocation = {
'A': 0.50, # 50% to core strategy
'hybrid': 0.30, # 30% to hybrid
'B': 0.20 # 20% to high-frequency
}
self.position_sizing_rules = {
'A': {
'base': 0.02, # 2% per trade
'max': 0.05, # 5% max
'volatility_factor': 0.8
},
'hybrid': {
'base': 0.015,
'max': 0.03,
'volatility_factor': 1.0
},
'B': {
'base': 0.008,
'max': 0.015,
'volatility_factor': 1.2
}
}

def get_position_size(self, system, opportunity):
config = self.position_sizing_rules[system]
base_size = self.total_capital * config['base']

# Volatility adjustment
volatility_factor = 1 + (opportunity['volatility'] - 0.05) * config['volatility_factor']
size = base_size * volatility_factor

# Apply caps
return min(size, self.total_capital * config['max'])

def update_weights(self, new_weights):
self.system_allocation = new_weights
