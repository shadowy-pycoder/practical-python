# follow.py
import os
import time


def follow(filename):
    '''
    Generator that produces a sequence of lines being written at the end of a file.
    '''
    f = open(filename, 'r')
    f.seek(0, os.SEEK_END)
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)    # Sleep briefly to avoid busy wait
            continue
        yield line


# Example use
if __name__ == '__main__':
    import report

    portfolio = report.read_portfolio('Data/portfolio.csv')

    for line in follow('Data/stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
