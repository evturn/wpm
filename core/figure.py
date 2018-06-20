from matplotlib import pyplot as plt

from core import Plotter

class Figure:
    def __init__(self, count=None):
        fig, ax = plt.subplots(dpi=128, figsize=(14,7))
        self.fig = fig
        self.ax = ax

        self.count = count
        self.plotter = Plotter(count=count)
        self.step = self.plotter.step

    def draw_axis_ticks(self):
        plt.ylim(65, 100)

        plt.xticks(range(0, self.count, self.step))
        plt.yticks(range(58, 101, 2), fontsize=10)
        plt.grid(axis='y',
                 which='both',
                 ls='--',
                 lw=.5,
                 c='midnightblue')

    def plot(self, data):
        xs, ys = self.plotter.get_plots(data)

        self.draw_axis_ticks()

        plt.plot(xs,
                 ys,
                 c='midnightblue',
                 linewidth=6)

        plt.show()
