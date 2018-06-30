import csv
from datetime import datetime

class CSVParser:
    def __init__(self, args):
        self.csvfile = args.path
        self.count = 0

    def parse(self):
        with open(self.csvfile) as f:
            reader = csv.reader(f)
            header = next(reader)

            wpm, acc, date = [], [], []
            for row in reader:
                wpm.append(int(row[1]))
                acc.append(float(row[2]))
                date.append(date.time.strptime(row[6], "%Y-%m-%d %H:%M:%S"))

        self.wpm = wpm
        self.acc = acc
        self.count = len(wpm)

        return wpm, acc, len(wpm)
