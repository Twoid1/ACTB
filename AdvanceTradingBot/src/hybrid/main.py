import asyncio
import yaml
from .integration_engine import HybridIntegration
from src.data_processing.market_data_stream import MarketDataStreamer

def load_config(config_path="config/hybrid.yaml"):
with open(config_path, 'r') as f:
return yaml.safe_load(f)

async def main():
config = load_config()

# Initialize components
streamer = MarketDataStreamer(config['hybrid']['asset_universe']['primary'])
hybrid_engine = HybridIntegration(capital=20000)

# Start market data stream
await streamer.connect()

# Run hybrid engine
await hybrid_engine.run()

if __name__ == "__main__":
asyncio.run(main())
