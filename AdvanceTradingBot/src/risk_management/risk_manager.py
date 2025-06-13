import numpy as np
import logging
from datetime import datetime

class RiskManager:
def __init__(self, initial_capital, config):
self.initial_capital = initial_capital
self.current_capital = initial_capital
self.config = config
self.active_positions = {}
self.trade_history = []
self.logger = logging.getLogger(__name__)

def evaluate_signal(self, signal):
symbol = signal['symbol']
price = signal['price']

# Check position limits
if self._position_exposure(symbol) > self.config['position_limits']['per_asset']:
self.logger.debug(f"Position limit reached for {symbol}")
return None

# Calculate position size
volatility = signal['indicators']['atr'] / price
position_size = self._calculate_position_size(signal, volatility)

# Check available capital
if position_size * price > self.current_capital * 0.9:
self.logger.warning("Insufficient capital for trade")
return None

return position_size

def _position_exposure(self, symbol):
position_value = self.active_positions.get(symbol, 0)
return position_value / self.current_capital if self.current_capital > 0 else 0

def _calculate_position_size(self, signal, volatility):
base_size = self.current_capital * self.config['risk_per_trade']
confidence_factor = signal.get('confidence', 0.5)

# Volatility adjustment
if volatility > 0.08:
size = base_size * 0.7 * confidence_factor
elif volatility < 0.04:
size = base_size * 1.3 * confidence_factor
else:
size = base_size * confidence_factor

return max(size, self.config['min_position_size'])

def update_position(self, symbol, size, price, action):
cost = size * price
if action == 'BUY':
self.current_capital -= cost
self.active_positions[symbol] = self.active_positions.get(symbol, 0) + size
elif action == 'SELL':
self.current_capital += cost
if symbol in self.active_positions:
self.active_positions[symbol] -= size
if self.active_positions[symbol] <= 0:
del self.active_positions[symbol]

# Record trade
self.trade_history.append({
'timestamp': datetime.now(),
'symbol': symbol,
'action': action,
'size': size,
'price': price,
'cost': cost
})
self.logger.info(f"Position updated: {action} {size} {symbol} @ {price}")

def get_portfolio_value(self):
return self.current_capital
