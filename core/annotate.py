from matplotlib import pyplot as plt
import numpy as np

class Annotate:
    def __init__(self, xs, ys):
        self.xs = xs
        self.ys = ys
        self.plot_count = len(xs)

    def draw(self):
        last_max = 0
        for i in np.arange(self.plot_count):
            x = self.xs[i]
            y = int(self.ys[i])
            if y > last_max:
                last_max = y
                self.annotate(x, 
                              y, 
                              dict(boxstyle="round4",
                                   fc="gold",
                                   ec="midnightblue",
                                   lw="1"),
                              size=11)
            else:
                self.annotate(x, 
                              y, 
                              dict(boxstyle="round4",
                                   fc="white",
                                   ec="midnightblue",
                                   lw="1"))

    def annotate(self, x, y, bbox, size=7):
        plt.annotate(s=str(y),
                     xy=(x, y),
                     xycoords='data',
                     xytext=(x, y),
                     textcoords='data',
                     size=size,
                     va='center',
                     ha='center',
                     bbox=bbox)


