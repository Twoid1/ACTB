from datetime import datetime

def optimize_exit(position, strategy_type):
current_profit = position['current_price'] / position['entry_price'] - 1
position_duration = (datetime.now() - position['entry_time']).total_seconds() / 60

# Secure gains early
if current_profit >= position['profit_target'] * 0.8:
return "EARLY_GAIN_SECURE"

# Avoid stagnant trades
avg_win_time = 45 if strategy_type == 'hybrid' else 90
if position_duration > avg_win_time * 1.3 and current_profit < 0.005:
return "STAGNANT_TRADE"

return None
