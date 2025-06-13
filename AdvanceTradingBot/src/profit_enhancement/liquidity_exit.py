def liquidity_based_exit(order_book, position_profit):
if len(order_book['bids']) < 3 or len(order_book['asks']) < 3:
return False

bid_ask_ratio = sum(bid[1] for bid in order_book['bids'][:3]) / sum(ask[1] for ask in order_book['asks'][:3])
return bid_ask_ratio > 1.8 and position_profit > 0.01
