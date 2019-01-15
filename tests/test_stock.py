from unittest import TestCase

from model.stock import StockType, Stock


class TestStockType(TestCase):
    def test_class_has_stock_attributes(self):
        """
        test para identificar el tipo de stock
        """
        self.assertTrue(hasattr(StockType, 'common'))
        self.assertTrue(hasattr(StockType, 'preferred'))


class TestStock(TestCase):
    def setUp(self):
        self.stock = Stock('TEA', 'Common', 3, '', 100)
        self.stock = Stock('GIN', 'Preferred', 8, '2%', 100)

    def test_required_properties(self):
        self.assertTrue(hasattr(self.stock, 'symbol'))
        self.assertTrue(hasattr(self.stock, 'type_stock'))
        self.assertTrue(hasattr(self.stock, 'last_dividend'))
        self.assertTrue(hasattr(self.stock, 'fixed_dividend'))
        self.assertTrue(hasattr(self.stock, 'par_value'))

        #symbol, type_stock, last_dividend, fixed_dividend, par_value


    def test_set_properties(self):
        self.assertEqual(self.stock.symbol, 'GIN')
        self.assertEqual(self.stock.type_stock, 'Preferred')
        self.assertEqual(self.stock.last_dividend, 8)
        self.assertEqual(self.stock.fixed_dividend, '2%')
        self.assertEqual(self.stock.par_value, 100)

    def test_type_stock_raises_error(self):
        with self.assertRaises(TypeError):
            self.stock.type_stock = ''

    def test_last_dividend_raises_error(self):
        with self.assertRaises(TypeError):
            self.stock.last_dividend = ''

    def test_fixed_dividend_raises_error(self):
        with self.assertRaises(TypeError):
            self.stock.fixed_dividend = None

    def test_par_value_raises_error(self):
        with self.assertRaises(TypeError):
            self.stock.par_value = ''
