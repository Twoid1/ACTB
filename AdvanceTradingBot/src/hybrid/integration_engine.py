import asyncio
from .hybrid_router import HybridRouter
from .capital_allocator import CapitalAllocator
from .regime_detector import MarketRegimeDetector
from src.execution.order_executor import OrderExecutor

class HybridIntegration:
def __init__(self, capital=20000):
self.scanner = MarketScanner()
self.router = HybridRouter()
self.allocator = CapitalAllocator(capital)
self.regime_detector = MarketRegimeDetector()
self.executor = OrderExecutor()
self.active_trades = {}

async def run(self):
while True:
# Update market regime
regime = self.regime_detector.update_regime()
self.allocator.update_weights(
self.regime_detector.get_strategy_weights()
)

# Scan for opportunities
opportunities = self.scanner.scan_markets()

for opportunity in opportunities:
# Route opportunity
trade_plan = self.router.route_signal(opportunity)
if not trade_plan:
continue

# Calculate position size
size = self.allocator.get_position_size(
trade_plan['system'],
opportunity
)

# Execute trade
await self.execute_trade(opportunity, trade_plan, size)

# Monitor active trades
await self.monitor_trades()

await asyncio.sleep(10) # 10-second cycle

async def execute_trade(self, opportunity, trade_plan, size):
# Implementation would go here
print(f"Executing {trade_plan['system']} trade on {opportunity['symbol']}")

async def monitor_trades(self):
# Check active trades and exit if needed
pass
