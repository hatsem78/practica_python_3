from functools import reduce

from model.stock import Stock, StockType
from model.trades import Trade


class StockMarket(Stock, Trade):

    def __init__(self, symbol, type_stock, last_dividend, fixed_dividend=None, par_value=None):
        super().__init__(symbol, type_stock, last_dividend, fixed_dividend, par_value)
        self.fixed_dividend = fixed_dividend

    def add_trade(self, timestamp, quantity, indicator, price):
        assert quantity > 0;
        self.trade.append(Trade(timestamp, quantity, indicator, price))

    @property
    def fixed_dividend(self):
        return self._fixed_dividend

    @fixed_dividend.setter
    def fixed_dividend(self, value):
        if StockType.preferred.value == self.type_stock.upper():
            self._fixed_dividend = float(value.replace('%', '') or 0)
        else:
            self._fixed_dividend = 0.0

    def dividend_yield(self, price):

        if price is None or price == 0:
            raise ValueError('Market precio es cero')

        if StockType.common.value == self.type_stock.upper():
            return self.last_dividend / price
        elif StockType.preferred.value == self.type_stock.upper():
            return (self.fixed_dividend * self.par_value) / price


    def pe_ratio(self, market_price):
        """
        calcula the P/E ratio
        :param market_price: precio del stock
        :return: P/E ratio
        :raises ValueError si es dividido por cero
        """
        dividend = self.dividend_yield(market_price)
        if dividend > 0.0:
            return market_price/dividend
        else:
            return 0



