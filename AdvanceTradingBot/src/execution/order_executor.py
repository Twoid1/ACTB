import logging
from binance.client import Client

class OrderExecutor:
def __init__(self, exchange_api):
self.exchange_api = exchange_api
self.logger = logging.getLogger(__name__)

def execute_order(self, signal, size):
symbol = signal['symbol']
action = signal['action']
target_price = signal['price']

try:
# Execute entry order
if action == 'BUY':
order_result = self.exchange_api.create_order(
symbol=symbol,
side=Client.SIDE_BUY,
type=Client.ORDER_TYPE_MARKET,
quantity=size
)
else: # SELL
order_result = self.exchange_api.create_order(
symbol=symbol,
side=Client.SIDE_SELL,
type=Client.ORDER_TYPE_MARKET,
quantity=size
)

self.logger.info(f"Order executed: {action} {size} {symbol} @ {order_result['price']}")
return {
'symbol': symbol,
'action': action,
'size': size,
'price': order_result['price'],
'status': 'FILLED'
}
except Exception as e:
self.logger.error(f"Order execution failed: {str(e)}")
return {
'status': 'FAILED',
'error': str(e)
}
