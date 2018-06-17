class Plotter:
    def __init__(self, count=None):
        self.count = count
        self.step = self.get_segmentation_step()

    def get_segmentation_step(self, percentage=.025):
        items_per_segment = int(self.count * percentage)

        if items_per_segment > 0:
            return items_per_segment 
        else:
            return 1

    def get_x_plots(self):
        '''Creates a list of where the points along x-axis will be plotted'''
        stop = self.count
        quo, rem = divmod(self.count, self.step)

        if rem:
            stop += 1
        
        return list(range(1, stop, self.step))

    def get_y_plots(self, data, plots=list()):
        '''Returns a list containing the average of all values in each segment'''
        unplotted_count = len(data)

        if unplotted_count < self.step:
            step_sum = sum(data) / unplotted_count
            data = []
        else:
            step_sum = sum(data[0:self.step]) / self.step
            data = data[self.step:]

        plots.append(step_sum)

        if data:
            return self.get_y_plots(data, plots=plots)
        else:
            return plots
