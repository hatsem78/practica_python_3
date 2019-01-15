from functools import reduce
import datetime
from model.trades import Trade


class TradeStore(list):
    """
        Registra el Trade que ingresa un Stock
    """


    def __init__(self):
        self.trades = []

    """
        Registra un trade para de stock.
        :param trade: Es un objeto Trade.
    """
    def record_trade(self, trade: Trade):
        self.trades.append(trade)  # append tuple to self

    def count_trade(self):
        return len(self.trades)

    def volume_weighted_price(self):
        """
            Calcula el Índice de Acciones Compartidas de GBCE utilizando la media geométrica
            del Precio de Acciones Ponderado en Volumen para todas las acciones
            :return:  GBCE
        """

        if not isinstance(self.trades, list):
            raise TypeError('Trades no es un objeto List')

        volume = 0
        price_quantity = 0

        for trade in self.trades:
            volume += trade.quantity
            price_quantity += trade.quantity * trade.price

        return price_quantity / volume

    def geometric_mean(self):
        """
            Calcula el precio de las acciones ponderadas por volumen según las operaciones realizadas
            en los últimos 5 minutos
            :return: geometric_mean
        """

        if not isinstance(self.trades, list):
            raise TypeError('Trades no es un objeto List')

        last_five_minutes = datetime.datetime.now() - datetime.timedelta(minutes=5)

        #filtra trades que se encuentran en los ultimos 5 minutos
        last_trades = list(filter(lambda trade: (last_five_minutes.minute - trade.timestamp.minute) <= 5, self.trades))



        prices = reduce(lambda x, y: x * y, [trade.price for trade in last_trades], 1)

        return prices ** (1 / len(self.trades))
