from core import CSVParser

class Plotter:
    def __init__(self, args):
        csvparser = CSVParser(args)
        wpm, acc, count = csvparser.parse()
        self.wpm = wpm
        self.acc = acc
        self.count = count

        print(self.count)

    def get_segment_count(self, percentage=.025):
        items_per_segment = int(self.count * percentage)

        if items_per_segment > 0:
            return items_per_segment 
        else:
            return 1

    def get_segmented_x_axis_values(self, count, segment_count):
        '''Creates a list of where the points along x-axis will be plotted'''
        quo, rem = divmod(count, segment_count)

        if rem:
            count += 1
        
        return list(range(1, count, segment_count))
