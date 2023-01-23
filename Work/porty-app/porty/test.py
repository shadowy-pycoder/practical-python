import report
from tableformat import create_formatter, print_table

portfolio = report.read_portfolio('Data/portfolio.csv')
formatter = create_formatter('html')
print_table(portfolio, ['name', 'shares'], formatter)
