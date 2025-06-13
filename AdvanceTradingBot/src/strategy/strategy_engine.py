import numpy as np
import logging
from .indicators import calculate_vwap, calculate_rsi, calculate_atr

class StrategyEngine:
def __init__(self, config):
self.config = config
self.indicators = {}
self.logger = logging.getLogger(__name__)

def initialize_symbol(self, symbol):
if symbol not in self.indicators:
self.indicators[symbol] = {
'vwap': {'values': [], 'window': 20},
'rsi': {'values': [], 'window': 14},
'atr': {'values': [], 'window': 14},
'volume': {'values': [], 'window': 20}
}

def process_tick(self, tick):
symbol = tick['symbol']
self.initialize_symbol(symbol)

# Update indicators
self._update_indicators(symbol, tick)

# Get current values
vwap = self.indicators[symbol]['vwap']['current']
rsi = self.indicators[symbol]['rsi']['current']
atr = self.indicators[symbol]['atr']['current']
avg_volume = self.indicators[symbol]['volume']['average']

# Generate signal
signal = self._generate_signal(tick, vwap, rsi, atr, avg_volume)
return signal

def _update_indicators(self, symbol, tick):
# Update price and volume
self.indicators[symbol]['vwap']['values'].append(tick)
self.indicators[symbol]['volume']['values'].append(tick['volume'])

# Trim to window size
for indicator in self.indicators[symbol].values():
if 'window' in indicator and len(indicator['values']) > indicator['window']:
indicator['values'] = indicator['values'][-indicator['window']:]

# Calculate indicators
self.indicators[symbol]['vwap']['current'] = calculate_vwap(
self.indicators[symbol]['vwap']['values']
)
self.indicators[symbol]['rsi']['current'] = calculate_rsi(
[t['price'] for t in self.indicators[symbol]['vwap']['values']]
)
self.indicators[symbol]['atr']['current'] = calculate_atr(
self.indicators[symbol]['vwap']['values']
)
self.indicators[symbol]['volume']['average'] = np.mean(
self.indicators[symbol]['volume']['values']
)

def _generate_signal(self, tick, vwap, rsi, atr, avg_volume):
price = tick['price']
volume = tick['volume']

# Bull market strategy
if price > vwap and rsi < 65 and volume > avg_volume * 2:
return {
'action': 'BUY',
'symbol': tick['symbol'],
'price': price,
'confidence': min(1.0, (rsi - 35) / 30),
'indicators': {
'vwap': vwap,
'rsi': rsi,
'atr': atr
}
}

# Bear market strategy
if price < vwap * 0.98 and rsi > 70 and volume > avg_volume * 3:
return {
'action': 'SELL',
'symbol': tick['symbol'],
'price': price,
'confidence': min(1.0, (70 - rsi) / 30),
'indicators': {
'vwap': vwap,
'rsi': rsi,
'atr': atr
}
}

return {'action': 'HOLD'}
