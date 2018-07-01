import csv
from datetime import datetime
from collections import namedtuple

Date = namedtuple('Date', ['year', 'month', 'day'])

class CSVParser:
    def __init__(self, args):
        self.csvfile = args.path
        self.count = 0

    def parse(self):
        with open(self.csvfile) as f:
            reader = csv.reader(f)
            header = next(reader)

            wpm, acc, dates = [], [], []
            for row in reader:
                wpm.append(int(row[1]))
                acc.append(float(row[2]))
                dates.append(self.splitDate(row[6]))

        self.wpm = wpm
        self.acc = acc
        self.dates = dates
        self.count = len(wpm)

        return wpm, acc, dates, len(wpm)

    def splitDate(self, date):
        d = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        return Date(d.year, d.month, d.day)

