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
            if y > last_max or i == (self.plot_count - 1):
                last_max = y
                plt.annotate(s=str(y),
                             xy=(x, y),
                             xycoords='data',
                             xytext=(x, y),
                             textcoords='data',
                             size=6.5,
                             va='center',
                             ha='center',
                             bbox=dict(boxstyle="round4",
                                       fc="white",
                                       ec="navy",
                                       lw="1.2")
                             )


