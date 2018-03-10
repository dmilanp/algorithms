from __future__ import absolute_import, unicode_literals

import numpy as np
import pandas as pd


class KMeans(object):

    def __init__(self, from_df=None, dimension=2, initial_count=50):
        super(KMeans, self).__init__()
        self.dimension = dimension
        self.initial_point_count = initial_count
        self.points = pd.DataFrame()

        if not from_df:
            self.append_random_points(initial_count)

    def append_random_points(self, point_count):
        for i in xrange(point_count):
            self.points = self.points.assign(**{str(i):self.random_point_of_dimension(dimension=self.dimension)})

    def append_points(self, points):
        for point in points:
            self._assert_point_dimension(point)
            self.points.append(point)

    @staticmethod
    def random_point_of_dimension(dimension):
        # Not very random for now
        return np.random.randn(dimension)

    def _assert_point_dimension(self, point):
        assert len(point) == self.dimension


if __name__ == '__main__':
    a = KMeans()
    print a.points