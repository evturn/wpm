import csv

class CSVParser:
    def __init__(self, args):
        self.csvfile = f'wpm/{args.path}'
        self.count = 0

    def parse(self):
        with open(self.csvfile) as f:
            reader = csv.reader(f)
            header = next(reader)

            wpm, acc = [], []
            for row in reader:
                wpm.append(int(row[1]))
                acc.append(float(row[2]))

        self.wpm = wpm
        self.acc = acc
        self.count = len(wpm)

        return self
