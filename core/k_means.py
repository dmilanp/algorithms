import logging
import sys

import matplotlib as mpl
import pandas as pd

from utils.pandas import random_point_of_dimension, random_dataframe_rows
from utils.misc import point_distance, random_color

mpl.use('TkAgg')

import matplotlib.pyplot as plt

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger(__name__)

COL_CLUSTER = 'cluster'


class KMeans(object):

    THRESHOLD = 5./1000

    def __init__(self, from_df=None, dimension=2, initial_count=50):
        super(KMeans, self).__init__()
        self.dimension = dimension
        self.points = from_df or pd.DataFrame()
        self.points[COL_CLUSTER] = None

        if not from_df:
            self.add_random_points(initial_count)

    def add_random_points(self, count):
        for i in xrange(count):
            self.points = self.points.append(
                random_point_of_dimension(dimension=self.dimension),
                ignore_index=True
            )

    def calculate_k_means(self, k):
        assert 1 < k < self.point_count
        logging.info('Calculating {} means for {} points of dimension {}'.format(k, self.point_count, self.dimension))

        # Forgy initialization method
        self.k_means = random_dataframe_rows(self.points, k).drop(COL_CLUSTER, axis=1)
        logging.info('Assigned random k-means from initial points')

        while True:
            self._map_points_to_clusters(k)
            maximum_update_step = self._update_means(k)

            logging.info('Maximum update step for a mean is {}'.format(maximum_update_step))
            if maximum_update_step < self.THRESHOLD:
                break

        logging.info('Found K means')
        self._plot_clusters(k)
        return self.k_means

    def _map_points_to_clusters(self, k):
        for point_index in xrange(self.point_count):
            # Check all points. Select all columns except COL_CLUSTER.
            point = self.points.iloc[point_index][:-1]
            cluster_index = 0
            distance_to_cluster_mean = point_distance(self.k_means.iloc[cluster_index], point)

            for cluster_candidate_index in xrange(1, k):
                # Check to which centroid the point is closest
                candidate_distance = point_distance(self.k_means.iloc[cluster_candidate_index], point)

                if candidate_distance < distance_to_cluster_mean:
                    cluster_index = cluster_candidate_index
                    distance_to_cluster_mean = candidate_distance

            self.points.loc[point_index, COL_CLUSTER] = cluster_index

    def _update_means(self, num_means):
        maximum_step = 0

        for i in xrange(num_means):
            points_in_cluster = pd.DataFrame(self.points.query('{} == {}'.format(COL_CLUSTER, i)))
            cluster_size = len(points_in_cluster)
            item_wise_sum = points_in_cluster.sum()

            if cluster_size == 0:
                logging.info('Cluster {} has no members'.format(i))
                continue

            updated_mean = item_wise_sum[:-1] / cluster_size
            update_length = point_distance(self.k_means.iloc[i], updated_mean)

            if update_length > maximum_step:
                maximum_step = update_length

            self.k_means.iloc[i] = updated_mean

        return maximum_step

    @property
    def point_count(self):
        return len(self.points)

    def _plot_clusters(self, k):
        points_in_cluster = pd.DataFrame(self.points.query('{} == {}'.format(COL_CLUSTER, 0)))
        plot = points_in_cluster.plot(x=0, y=1, linestyle="", marker="o", c=random_color())

        for i in xrange(1, k):
            points_in_cluster = pd.DataFrame(self.points.query('{} == {}'.format(COL_CLUSTER, i)))
            points_in_cluster.plot(ax=plot, x=0, y=1, linestyle="", marker="o", c=random_color())

        plt.show()
