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

    def get_segmented_y_axis_values(self, item_values, segment_count, plot_values):
        '''Returns a list containing the average of all values in each segment'''
        unplotted_count = len(item_values)

        if unplotted_count < segment_count:
            segment_sum = sum(item_values) / unplotted_count
            item_values = []
        else:
            segment_sum = sum(item_values[0:segment_count]) / segment_count
            item_values = item_values[segment_count:]

        plot_values.append(segment_sum)

        if item_values:
            return self.get_segmented_y_axis_values(item_values, segment_count, plot_values)
        else:
            return plot_values

