import unittest
from src.hybrid.integration_engine import HybridIntegration
from src.hybrid.regime_detector import MarketRegimeDetector
from unittest.mock import MagicMock, patch

class TestHybridIntegration(unittest.TestCase):
    @patch('src.hybrid.integration_engine.ParallelMarketScanner')
    def setUp(self, mock_scanner):
        self.mock_scanner = mock_scanner
        self.integration = HybridIntegration(capital=20000)

    def test_regime_detection(self):
        detector = MarketRegimeDetector()
        market_data = MagicMock()
        regime = detector.update_regime(market_data)
        self.assertIn(regime, [
            'bull_strong', 'bear_strong', 
            'high_volatility', 'low_volatility', 'neutral'
        ])

    def test_capital_allocation(self):
        weights = self.integration.allocator.system_allocation
        total = weights['A'] + weights['hybrid'] + weights['B']
        self.assertAlmostEqual(total, 1.0)

    def test_hybrid_router(self):
        opportunity = {
            'fundamental_score': 0.85,
            'asset_class': 'large_cap',
            'technical_score': 0.75,
            'sentiment_score': 0.65,
            'volatility': 0.09,
            'volume_ratio': 3.5,
            'liquidity': 750000
        }
        plan = self.integration.router.route_signal(opportunity)
        self.assertEqual(plan['system'], 'A')

    @patch('src.hybrid.integration_engine.HighFrequencyExecutor')
    async def test_trade_execution(self, mock_executor):
        # Prepare scanner and router mocks
        self.mock_scanner.scan_markets.return_value = [MagicMock()]
        self.integration.router.route_signal.return_value = {'system': 'A', 'size': 100}
        mock_executor.execute_trade = MagicMock()

        await self.integration.run()
        mock_executor.execute_trade.assert_called_once()

if __name__ == '__main__':
    unittest.main()
