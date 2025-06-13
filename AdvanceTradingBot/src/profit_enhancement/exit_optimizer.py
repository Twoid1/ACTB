from datetime import datetime

def optimize_exit(position, strategy_data):
"""Implement win rate optimization through smart exits"""
current_profit = position['current_price'] / position['entry_price'] - 1
rsi = position['indicators']['rsi']
time_in_trade = (datetime.now() - position['entry_time']).total_seconds() / 60

# Early profit securing
if current_profit >= position['profit_target'] * 0.8 and rsi > 65:
return True, "EARLY_GAIN_SECURE"

# Stagnant trade avoidance
avg_win_time = strategy_data['avg_win_time']
if time_in_trade > avg_win_time * 1.3 and current_profit < 0.005:
return True, "STAGNANT_TRADE"

return False, None

def should_early_exit(position, strategy_type):
"""Determine if position should exit early based on optimization rules"""
strategy_stats = {
'A': {'avg_win_time': 90},
'hybrid': {'avg_win_time': 45},
'B': {'avg_win_time': 20}
}
return optimize_exit(position, strategy_stats[strategy_type])
