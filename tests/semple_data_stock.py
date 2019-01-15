from model.stock import Stock


class SempleData:

    def __init__(self):
        self.list_data = []

    def semple_data(self):
        self.list_data.append(
            Stock('TEA', 'Common', 0, '', 100),
        )
        self.list_data.append(
            Stock('POP', 'Common', 8, '', 100),
        )
        self.list_data.append(
            Stock('ALE', 'Common', 23, '', 60),
        )

        self.list_data.append(
            Stock('GIN', 'Preferred', 8, '2%', 100),
        )
        self.list_data.append(
            Stock('JOE', 'Common', 13, '', 250),
        )
        return self.list_data

