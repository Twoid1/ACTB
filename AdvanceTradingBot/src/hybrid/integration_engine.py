import asyncio
from .hybrid_router import HybridRouter
from .capital_allocator import CapitalAllocator
from .regime_detector import MarketRegimeDetector
from src.execution.order_executor import HighFrequencyExecutor
from src.profit_enhancement import (
dynamic_targeting,
sentiment_scaling,
session_scaling
)

class HybridIntegration:
def __init__(self, capital=20000):
self.scanner = ParallelMarketScanner()
self.router = HybridRouter()
self.allocator = CapitalAllocator(capital)
self.regime_detector = MarketRegimeDetector()
self.executor = HighFrequencyExecutor()

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

# Apply profit enhancements
opportunity = dynamic_targeting.set_dynamic_targets(opportunity, regime)
opportunity = sentiment_scaling.apply_sentiment_scaling(opportunity)
opportunity = session_scaling.apply_session_scaling(opportunity)

# Execute trade
await self.executor.execute_trade(opportunity, trade_plan, size)

await asyncio.sleep(10) # 10-second cycle
