# def read_portfolio(filename):
#     portfolio = []
#     with open(filename, 'rt') as file:
#         rows = csv.reader(file)
#         headers = next(rows)
#         for row in rows:
#             holding = (row[0], int(row[1]), float(row[2]))
#             portfolio.append(holding)
#     return portfolio


# Exercise 2.5: List of Dictionaries


# def read_portfolio(filename):
#     portfolio = []
#     with open(filename, 'rt') as file:
#         rows = csv.reader(file)
#         headers = next(rows)
#         for row in rows:
#             holding = dict(name=row[0], shares=int(row[1]), price=float(row[2]))
#             portfolio.append(holding)
#     return portfolio


# Exercise 2.6: Dictionaries as a container


def read_prices2(filename):
    prices = {}
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices

    # Exercise 2.7: Finding out if you can retire


def can_retire(stocks, prices):
    total_old = 0.0
    total_new = 0.0
    for stock in stocks:
        total_new += int(stock['shares']) * prices.get(stock['name'], 0.0)
        total_old += int(stock['shares']) * float(stock['price'])
    return total_old, total_new, total_new - total_old > 0


# Exercise 2.16: Using the zip() function


def read_portfolio2(filename):
    portfolio = []
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                'name': record['name'],
                'shares': int(record['shares']),
                'price': float(record['price'])
            }
            portfolio.append(stock)
    return portfolio


def portfolio_report2(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)


def portfolio_cost0(filename):
    total = 0
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            _, shares, price = row
            try:
                total += int(shares) * float(price)
            except ValueError:
                print("Couldn't parse", row)
    return total


# Exercise 2.15: A practical enumerate() examp
def portfolio_cost2(filename):
    total = 0
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for index, row in enumerate(rows, 1):
            _, shares, price = row
            try:
                total += int(shares) * float(price)
            except ValueError:
                print(f'Row {index}: Couldn\'t convert: {row}')
    return total


# Exercise 2.16: Using the zip() function
def portfolio_cost3(filename):
    total = 0
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for index, row in enumerate(rows, 1):
            record = dict(zip(headers, row))
            try:
                total += int(record['shares']) * float(record['price'])
            except ValueError:
                print(f'Row {index}: Couldn\'t convert: {row}')
    return total
