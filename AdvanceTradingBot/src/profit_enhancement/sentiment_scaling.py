def apply_sentiment_scaling(signal, sentiment_score):
if sentiment_score > 0.85:
return {
'size': signal['size'] * 1.4,
'profit_target': signal['profit_target'] * 1.25,
'stop_loss': signal['stop_loss'] * 1.15
}
return signal
