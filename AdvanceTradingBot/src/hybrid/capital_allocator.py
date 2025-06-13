class CapitalAllocator:
def __init__(self, total_capital):
self.total_capital = total_capital
self.system_allocation = {'A': 0.50, 'hybrid': 0.30, 'B': 0.20}
self.position_sizing = {
'A': {'base': 0.02, 'max': 0.05, 'vol_factor': 0.8},
'hybrid': {'base': 0.015, 'max': 0.03, 'vol_factor': 1.0},
'B': {'base': 0.008, 'max': 0.015, 'vol_factor': 1.2}
}

def get_position_size(self, system, volatility):
config = self.position_sizing[system]
base_size = self.total_capital * config['base']
vol_factor = 1 + (volatility - 0.05) * config['vol_factor']
size = base_size * vol_factor
return min(size, self.total_capital * config['max'])
