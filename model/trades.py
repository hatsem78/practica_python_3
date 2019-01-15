import datetime
from enum import Enum


class TreadeIndicator(Enum):
    BUY = 1
    SELL = 2

class Trade(object):

    def __init__(self, timestamp, quantity, indicator, price):
        self.timestamp = timestamp
        self.quantity = quantity
        self.indicator = indicator
        self.price = price

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        if not isinstance(value, datetime.datetime):
            raise TypeError('Debe ser un objeto datetime')
        self._timestamp = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Quantity debe ser decimal o entero")
        self._quantity = value

    @property
    def indicator(self):
        return self._indicator

    @indicator.setter
    def indicator(self, value):
        if not isinstance(value, TreadeIndicator):
            raise TypeError("indicador debe ser un tipo TreadeIndicator")
        self._indicator = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Price debe ser un entero')
        elif value <= 0.0:
            raise ValueError('Price debería ser mayor que 0')
        else:
            self._price = value
