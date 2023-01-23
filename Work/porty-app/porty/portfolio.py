from collections import Counter
from . import fileparse
from . import stock


class Portfolio:
    def __init__(self):
        self.holdings = []

    def append(self, holding):
        if not isinstance(holding, stock.Stock):
            raise TypeError('Expected a Stock instance')
        self.holdings.append(holding)

    @classmethod
    def from_csv(cls, lines, **opts):
        self = cls()
        portdicts = fileparse.parse_csv(lines,
                                        select=['name', 'shares', 'price'],
                                        types=[str, int, float],
                                        **opts)

        for d in portdicts:
            self.append(stock.Stock(**d))

        return self

    def __iter__(self):
        return self.holdings.__iter__()

    def __len__(self):
        return len(self.holdings)

    def __getitem__(self, index):
        return self.holdings[index]

    def __contains__(self, name):
        return any(s.name == name for s in self.holdings)

    @property
    def total_cost(self):
        return sum(s.cost for s in self.holdings)

    def tabulate_shares(self):
        total_shares = Counter()
        for s in self.holdings:
            total_shares[s.name] += s.shares
        return total_shares
