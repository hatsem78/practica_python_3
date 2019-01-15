import datetime
import unittest
from unittest import TestCase

from model.trades import TreadeIndicator, Trade


class TestTreadeIndicator(TestCase):

    def test_type_indicator(self):
        """
            test tipo de indicador
        """
        self.assertTrue(hasattr(TreadeIndicator, 'BUY'))
        self.assertTrue(hasattr(TreadeIndicator, 'SELL'))


class TestTrade(TestCase):
    def setUp(self):
        self.timestamp = datetime.datetime.now()
        self.trade = Trade(self.timestamp, 12, TreadeIndicator.SELL, 15.9)

    def test_required_properties(self):
        self.assertTrue(hasattr(self.trade, 'timestamp'))
        self.assertTrue(hasattr(self.trade, 'quantity'))
        self.assertTrue(hasattr(self.trade, 'indicator'))
        self.assertTrue(hasattr(self.trade, 'price'))

    def test_set_properties(self):
        self.assertEqual(self.trade.timestamp, self.timestamp)
        self.assertEqual(self.trade.quantity, 12)
        self.assertEqual(self.trade.indicator, TreadeIndicator.SELL)
        self.assertEqual(self.trade.price, 15.9)

    def test_setter_timestamp_raises_error(self):
        with self.assertRaises(TypeError):
            self.trade.timestamp = '2018-01-01'

    def test_setter_quantity_raises_error(self):
        with self.assertRaises(TypeError):
            self.trade.quantity = "10"

    def test_setter_direction_raises_error(self):
        with self.assertRaises(TypeError):
            self.trade.indicator = 6

    def test_setter_price_raises_error(self):
        with self.assertRaises(TypeError):
            self.trade.price = "10"

if __name__ == '__main__':
    unittest.main()