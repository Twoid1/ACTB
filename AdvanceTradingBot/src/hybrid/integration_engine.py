import asyncio
from .hybrid_router import HybridRouter
from .capital_allocator import CapitalAllocator
from .regime_detector import MarketRegimeDetector

class HybridIntegrationEngine:
def __init__(self, capital=20000):
self.router = HybridRouter()
self.allocator = CapitalAllocator(capital)
self.regime_detector = MarketRegimeDetector()

async def process_opportunity(self, opportunity, volatility, trend_strength):
# Update market regime
regime = self.regime_detector.update_regime(volatility, trend_strength)
self.allocator.system_allocation = self.regime_detector.get_strategy_weights()

# Route opportunity
trade_plan = self.router.route_signal(opportunity)
if not trade_plan:
return None

# Calculate position size
size = self.allocator.get_position_size(
trade_plan['system'],
volatility
)

return {
'symbol': opportunity['symbol'],
'system': trade_plan['system'],
'size': size,
'profit_target': float(trade_plan['profit_target'].rstrip('%')) / 100,
'stop_loss': float(trade_plan['stop_loss'].rstrip('%')) / 100
}
