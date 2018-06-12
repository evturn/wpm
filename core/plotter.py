from core import CSVParser

class Plotter:
    def __init__(self, args):
        csvparser = CSVParser(args)
        wpm, acc, count = csvparser.parse()
        self.wpm = wpm
        self.acc = acc
        self.count = count

        print(self.count)
