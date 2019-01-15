import datetime
from random import randint, choice, random
from unittest import TestCase

from model.trade_store import TradeStore
from tests.semple_data_stock import SempleData
from model.stock_market import StockMarket
from model.trades import TreadeIndicator, Trade

class TestStockMarketIntegration(TestCase):

    data = SempleData()
    data.semple_data()

    list_trade = TradeStore()
    print("Stock | Dividend yield | P/E Ratio")
    for element in data.list_data:
        super_market = StockMarket(
            element.symbol,
            element.type_stock,
            element.last_dividend,
            element.fixed_dividend,
            element.par_value,
        )

        price = randint(1, 300)
        count = data.list_data.index(element) + 3
        timestamp = datetime.datetime.now() - datetime.timedelta(minutes=(5 + count))
        indicator = choice([TreadeIndicator.BUY, TreadeIndicator.SELL])
        price = random() * 100

        list_trade.record_trade(Trade(timestamp, quantity=randint(1, 30), indicator=indicator, price=price))

        print('%s     %s           %f' % (element.symbol, element.type_stock, super_market.pe_ratio(price)), super_market.dividend_yield(price))
    print()
    print('Geometric Mean')
    print(list_trade.geometric_mean())
    print()
    print('Volume Weighted Stock Price')
    print(list_trade.volume_weighted_price())