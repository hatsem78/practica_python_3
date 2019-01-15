from unittest import TestCase

from model.stock import StockType, Stock
from model.stock_market import StockMarket


class TestStockMarket(TestCase):

    def setUp(self):
        self.stock_common = StockMarket('TEA', 'COMMON', 3, '', 100)
        self.stock_preferred = StockMarket('GIN', 'Preferred', 8, '2%', 100)
        self.stock_pe_ratio_common = StockMarket('ALE', 'Common', 23, '', 60)
        self.stock_pe_ratio_preferred = StockMarket('GIN', 'Preferred', 8, '2%', 100)

    def test_dividend_yield_stock_common_value(self):
        self.assertEqual(self.stock_common.dividend_yield(12.5), 0.24)

    def test_dividend_yield_stock_preferred_value(self):
        self.assertEqual(self.stock_preferred.dividend_yield(23.5), 8.51063829787234)

    def test_pe_ratio__common_value(self):
        self.assertEqual(self.stock_pe_ratio_common.pe_ratio(69.25), 208.50271739130434)

    def test_stock_pe_ratio_preferred_value(self):
        self.assertEqual(self.stock_pe_ratio_preferred.pe_ratio(82.25), 33.8253125)
