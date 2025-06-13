from src.strategy.sentiment_analyzer import get_sentiment_score

def apply_sentiment_scaling(signal):
"""Enhance trades during high sentiment events"""
sentiment = get_sentiment_score(signal['symbol'])
if sentiment > 0.85:
signal['size'] *= 1.4
signal['profit_target'] *= 1.25
signal['stop_loss'] *= 1.15
return signal
