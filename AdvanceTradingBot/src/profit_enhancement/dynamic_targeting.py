def adaptive_profit_target(volatility, regime, base_target=0.018):
volatility_adjustment = min(0.03, volatility * 0.25)
regime_multiplier = {
'bull_strong': 1.25,
'bear_strong': 1.15,
'high_volatility': 0.85,
'low_volatility': 1.10,
'neutral': 1.0
}.get(regime, 1.0)
return base_target * regime_multiplier + volatility_adjustment
