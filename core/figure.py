from matplotlib import pyplot as plt

class Figure:
    def __init__(self, plotter):
        fig, ax = plt.subplots(dpi=128, figsize=(14,7))
        self.fig = fig
        self.ax = ax

        self.set_markings(plotter.count, plotter.stop)

    def set_markings(self, count, stop):
        plt.ylim(65, 100)

        plt.xticks(range(0, count, stop))
        plt.yticks(range(58, 101, 2), fontsize=10)
        plt.grid(axis='y',
                 which='both',
                 ls='--',
                 lw=.5,
                 c='midnightblue')


