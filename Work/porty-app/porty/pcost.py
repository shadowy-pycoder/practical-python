# pcost.py
#
# Exercise 1.27
import sys

from . import report


def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost


def main(args):
    if len(args) != 2:
        sys.exit(1)
    print(portfolio_cost(args[1]))


if __name__ == '__main__':
    main(sys.argv)
