import websockets
import json
import asyncio
import logging

class MarketDataStreamer:
def __init__(self, symbols, exchange='binance'):
self.symbols = symbols
self.exchange = exchange
self.ws_url = self._get_ws_url()
self.websocket = None
self.logger = logging.getLogger(__name__)

def _get_ws_url(self):
urls = {
'binance': 'wss://stream.binance.com:9443/ws',
'kraken': 'wss://ws.kraken.com',
'coinbase': 'wss://ws-feed.pro.coinbase.com'
}
return urls.get(self.exchange, 'binance')

async def connect(self):
try:
self.websocket = await websockets.connect(self.ws_url)
await self._subscribe()
self.logger.info(f"Connected to {self.exchange} WebSocket")
except Exception as e:
self.logger.error(f"Connection failed: {str(e)}")
raise

async def _subscribe(self):
if self.exchange == 'binance':
streams = [f"{symbol.lower()}@ticker" for symbol in self.symbols]
sub_msg = json.dumps({
"method": "SUBSCRIBE",
"params": streams,
"id": 1
})
await self.websocket.send(sub_msg)
# Add other exchange subscriptions as needed

async def stream_data(self):
while True:
try:
data = await self.websocket.recv()
normalized = self._normalize(json.loads(data))
yield normalized
except websockets.ConnectionClosed:
self.logger.warning("Connection closed. Reconnecting...")
await self.connect()
except Exception as e:
self.logger.error(f"Error receiving data: {str(e)}")
await asyncio.sleep(1)

def _normalize(self, data):
# Normalize data to common format
if self.exchange == 'binance':
return {
'symbol': data['s'],
'exchange': self.exchange,
'timestamp': data['E'],
'price': float(data['c']),
'volume': float(data['v']),
'high': float(data['h']),
'low': float(data['l']),
'type': 'ticker'
}
# Add other exchange normalizations
return data
