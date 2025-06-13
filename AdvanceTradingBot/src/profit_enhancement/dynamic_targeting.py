def adaptive_profit_target(volatility, regime, base_target=0.018):
"""Dynamically adjust profit targets based on market conditions"""
volatility_adjustment = min(0.03, volatility * 0.25)
regime_multiplier = {
'bull_strong': 1.25,
'bear_strong': 1.15,
'high_volatility': 0.85,
'low_volatility': 1.10,
'neutral': 1.0
}.get(regime, 1.0)
return base_target * regime_multiplier + volatility_adjustment

def set_dynamic_targets(trade_signal, market_regime):
"""Apply dynamic profit targets to trade signals"""
volatility = trade_signal['indicators']['atr'] / trade_signal['price']
trade_signal['profit_target'] = adaptive_profit_target(
volatility,
market_regime,
base_target=0.018
)
trade_signal['stop_loss'] = trade_signal['profit_target'] * 0.6
return trade_signal
