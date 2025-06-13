from datetime import datetime

def optimize_exit(position):
current_profit = (position['current_price'] / position['entry_price']) - 1
rsi = position.get('rsi', 50) # Default if not available

# Secure gains early
if current_profit >= position['profit_target'] * 0.8 and rsi > 65:
return True, "EARLY_GAIN_SECURE"

# Avoid stagnant trades
position_duration = (datetime.now() - position['entry_time']).total_seconds() / 60
if 'avg_win_time' in position and position_duration > position['avg_win_time'] * 1.3:
if current_profit < 0.005: # Less than 0.5%
return True, "STAGNANT_TRADE"

return False, None
