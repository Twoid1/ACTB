def liquidity_based_exit(position, order_book):
if not order_book or 'bids' not in order_book or 'asks' not in order_book:
return False

bid_ask_ratio = sum(bid[1] for bid in order_book['bids'][:3]) / sum(ask[1] for ask in order_book['asks'][:3])
position_profit = position['current_price'] / position['entry_price'] - 1
return bid_ask_ratio > 1.8 and position_profit > 0.01
