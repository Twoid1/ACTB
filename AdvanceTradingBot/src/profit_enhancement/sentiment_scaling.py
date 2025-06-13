def apply_sentiment_scaling(signal, sentiment):
if sentiment > 0.85:
signal['size'] = signal.get('size', 0) * 1.4
signal['profit_target'] = signal.get('profit_target', 0.018) * 1.25
signal['stop_loss'] = signal.get('stop_loss', 0.01) * 1.15
return signal
