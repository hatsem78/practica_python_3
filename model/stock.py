from enum import Enum

class StockType (Enum):

    common = "COMMON"
    preferred = "PREFERRED"


class Stock(object):

    def __init__(self, symbol, type_stock, last_dividend, fixed_dividend, par_value):
        self.__symbol = symbol
        self.symbol = symbol
        self.type_stock = type_stock
        self.last_dividend = last_dividend
        self.fixed_dividend = fixed_dividend
        self.par_value = par_value

    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, value):
        if value is None:
            raise ValueError
        self.__symbol = value

    @property
    def type_stock(self):
        return self.__type_stock

    @type_stock.setter
    def type_stock(self, value):
        if value.upper() not in (StockType.common.value, StockType.preferred.value):
            raise TypeError("Type stock  debe ser COMMON o PREFERRED")
        if not isinstance(value, str):
            raise TypeError("Quantity debe ser decimal o entero")

        self.__type_stock = value

    @property
    def last_dividend(self):
        return self.__last_dividend

    @last_dividend.setter
    def last_dividend(self, value):
        if value is None:
            raise ValueError
        elif not isinstance(value, (int, float)):
            raise TypeError("Quantity debe ser decimal o entero")
        self.__last_dividend = value

    @property
    def fixed_dividend(self):
        return self.__fixed_dividend

    @fixed_dividend.setter
    def fixed_dividend(self, value):
        if not isinstance(value, (str)):
            raise TypeError("Quantity debe ser decimal o entero")
        self.__fixed_dividend = value

    @property
    def par_value(self):
        return self.__par_value

    @par_value.setter
    def par_value(self, value):
        if value is None:
            raise ValueError
        elif not isinstance(value, (int, float)):
            raise TypeError("Quantity debe ser decimal o entero")
        self.__par_value = value


