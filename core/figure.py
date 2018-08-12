from matplotlib import pyplot as plt

from core import Plotter
from core import Scatter
from core import Annotate

class Figure:
    def __init__(self, count=None, file=None, dates=None):
        fig, ax = plt.subplots(dpi=128, figsize=(14,7))
        self.fig = fig
        self.ax = ax

        self.count = count
        self.file = file
        self.plotter = Plotter(count=count, dates=dates)
        self.step = self.plotter.step

    def draw_axis_ticks(self):
        plt.ylim(65, 100)

        x_locs = self.plotter.get_x_ticks()
        x_dates = self.plotter.get_dates()

        plt.xticks(x_locs, x_dates, rotation=0)
        plt.yticks(range(58, 111, 4), fontsize=10)

        plt.grid(axis='y',
                 which='both',
                 ls='--',
                 lw=.75,
                 c='midnightblue')

        
        plt.title(f'Average every {self.plotter.step} items\nTotal of {self.plotter.count} items')

    def plot(self, data, pcts):
        xs, ys = self.plotter.get_plots(data)

        self.draw_axis_ticks()

        scatter = Scatter(pcts)
        scatter.draw(data)

        plt.plot(xs,
                 ys,
                 c='black',
                 linewidth=6)
        annotate = Annotate(xs, ys)
        annotate.draw()

        self.draw()

    def draw(self):
        if self.file:
            plt.savefig(self.file)
            print('File created: ' + self.file)
        else:
            plt.show()

