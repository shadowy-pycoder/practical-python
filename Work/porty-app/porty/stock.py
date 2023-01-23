from . import fileparse
from .typedproperty import typedproperty


class Stock:
    name = typedproperty('name', str)
    shares = typedproperty('shares', int)
    price = typedproperty('price', float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, num):
        self.shares -= num

    def __repr__(self):
        return f'{__class__.__name__}({self.name!r}, {self.shares!r}, {self.price!r})'


if __name__ == '__main__':
    a = Stock('GOOG', 100, 490.10)
    print(a.cost)
    a.sell(25)
    print(a.cost)
    with open('Data/portfolio.csv') as lines:
        portdicts = fileparse.parse_csv(lines, select=['name', 'shares', 'price'], types=[
                                        str, int, float], has_headers=True)

    portfolio = [Stock(d['name'], d['shares'], d['price']) for d in portdicts]
    total = sum([s.cost for s in portfolio])
    print(total)
    print(a)
