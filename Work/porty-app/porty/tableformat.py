# tableformat.py

class FormatError(Exception):
    ...


class TableFormatter:

    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''

    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''

    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''

    def headings(self, headers):
        headers = ''.join(f'<th>{h}</th>' for h in headers)
        print(f'<tr>{headers}</tr>')

    def row(self, rowdata):
        rowdata = ''.join(f'<th>{h}</th>' for h in rowdata)
        print(f'<tr>{rowdata}</tr>')


def create_formatter(fmt):
    if fmt == 'txt':
        return TextTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter()
    elif fmt == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError('Unknown table format %s' % fmt)


def print_table(portfolio, columns, formatter):
    formatter.headings(columns)
    for stock in portfolio:
        rowdata = [str(getattr(stock, colname)) for colname in columns]
        formatter.row(rowdata)
