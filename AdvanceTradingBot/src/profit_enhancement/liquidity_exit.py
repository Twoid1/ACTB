def liquidity_based_exit(position, exchange):
"""Optimize exit timing based on market liquidity"""
order_book = exchange.get_order_book(position['symbol'])
if not order_book:
return False

bid_ask_ratio = sum(bid[1] for bid in order_book['bids'][:3]) / \
sum(ask[1] for ask in order_book['asks'][:3])
position_profit = position['current_price'] / position['entry_price'] - 1

if bid_ask_ratio > 1.8 and position_profit > 0.01:
return True
return False
