import numpy as np
import pandas as pd
import matplotlib as mpl

mpl.use('TkAgg')

import matplotlib.pyplot as plt


class KMeans(object):

    def __init__(self, from_df=None, dimension=2, initial_count=100):
        super(KMeans, self).__init__()
        self.dimension = dimension
        self.points = from_df or pd.DataFrame()

        if not from_df:
            self.add_random_points(initial_count)

    def add_random_points(self, count):
        for i in xrange(count):
            self.points = self.points.append(
                self.random_point_of_dimension(dimension=self.dimension),
                ignore_index=True
            )

    def feed_points(self, df):
        raise NotImplementedError

    @staticmethod
    def random_point_of_dimension(dimension):
        return pd.DataFrame(np.random.randn(1, dimension))

    @property
    def point_count(self):
        return len(self.points)

    def plot_points(self):
        self.points.plot(x=0, y=1, linestyle="", marker="o")
        plt.show()

if __name__ == '__main__':
    a = KMeans()
    print '{} has {} points'.format(a, a.point_count)
    a.plot_points()
