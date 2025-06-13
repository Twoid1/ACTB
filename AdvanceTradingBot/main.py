import asyncio
import yaml
import logging
import HybridIntegration
from src.data_processing.market_data_stream import MarketDataStreamer
from src.strategy.strategy_engine import StrategyEngine
from src.risk_management.risk_manager import RiskManager
from src.execution.order_executor import OrderExecutor
from src.hybrid.integration_engine
from binance.client import Client

# Configure logging
logging.basicConfig(
level=logging.INFO,
format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
handlers=[
logging.FileHandler("trading_bot.log"),
logging.StreamHandler()
]
)
logger = logging.getLogger(__name__)

async def main():
# Load configuration
with open("config/paper_trading.yaml", "r") as f:
config = yaml.safe_load(f)

# Initialize exchange API
exchange_api = Client(
api_key=config['exchanges']['binance']['api_key'],
api_secret=config['exchanges']['binance']['secret'],
testnet=config['exchanges']['binance']['paper_trading']
)

# Initialize components
streamer = MarketDataStreamer(config['symbols'])
strategy = StrategyEngine(config)
risk_manager = RiskManager(config['initial_capital'], config['risk_parameters'])
executor = OrderExecutor(exchange_api)
hybrid_engine = HybridIntegration(capital=20000)

asyncio.run(hybrid_engine.run())

# Connect to market data
await streamer.connect()

# Main trading loop
async for tick in streamer.stream_data():
try:
logger.info(f"Processing tick: {tick['symbol']} @ {tick['price']}")

# Generate trading signal
signal = strategy.process_tick(tick)

if signal['action'] != 'HOLD':
logger.info(f"Signal generated: {signal['action']} {signal['symbol']}")

# Evaluate risk and position size
size = risk_manager.evaluate_signal(signal)

if size:
logger.info(f"Executing trade: {signal['action']} {size} {signal['symbol']}")

# Execute trade
execution_result = executor.execute_order(signal, size)

if execution_result['status'] == 'FILLED':
# Update portfolio
risk_manager.update_position(
signal['symbol'],
size,
execution_result['price'],
signal['action']
)
logger.info(f"Position updated. Current capital: ${risk_manager.get_portfolio_value():.2f}")

except Exception as e:
logger.error(f"Error processing tick: {str(e)}")

if __name__ == "__main__":
asyncio.run(main())
