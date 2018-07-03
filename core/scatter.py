from matplotlib import pyplot as plt
import numpy as np

from core import scatterplots

class Scatter:
    def __init__(self, data):
        self.data = data

    def draw(self, y_data):
        pc_count = len(self.data)
        pc_indices = np.arange(pc_count)

        sp_count = len(scatterplots)
        sp_indices = np.arange(sp_count)
        sps = [[] for i in sp_indices]

        for pc_idx in pc_indices:
            sp_idx = 100 - int(self.data[pc_idx] * 100)
            if sp_idx >= sp_count:
                sp_idx = sp_count - 1

            sps[sp_idx].append(pc_idx)

        for idx in sp_indices:
            xs = []
            ys = []

            for x in sps[idx]:
                xs.append(x)
                ys.append(y_data[x])

                label, color, alpha, shape, edge = scatterplots[idx]

            plt.scatter(xs,
                        ys,
                        c=color,
                        alpha=alpha,
                        s=shape,
                        edgecolor=edge,
                        label=label)
            plt.legend(loc=2, fontsize=13)
