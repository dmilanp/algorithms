from __future__ import absolute_import, unicode_literals

import logging
from bisect import bisect_right

import numpy as np

from utils.panda_utils import (
    center_dataframe,
    covariance_dataframe,
    decreasing_eigenvalues_with_eigenvectors,
    first_columns,
    outer_product,
)


class PCA(object):
    def __init__(self, df):
        super(PCA, self).__init__()
        self.points = df
        self.dimension = len(df.columns)
        self.eigenvalues = None
        self.eigenvectors = None

    def _get_eigendata(self):
        if self.eigenvalues is not None and self.eigenvectors is not None:
            return

        centered_dataframe = center_dataframe(self.points)
        covariance_from_dataset = covariance_dataframe(centered_dataframe)
        self.eigenvalues, self.eigenvectors = decreasing_eigenvalues_with_eigenvectors(covariance_from_dataset)

    def principal_components(self, p):
        self._get_eigendata()
        p_eigenvectors = first_columns(self.eigenvectors, p)
        pca = outer_product(first=self.points, second=p_eigenvectors)
        return pca

    def cumulative_energy(self):
        if not self.eigenvalues:
            logging.info('Please run principal_components first')
            return

        total_energy = float(sum(self.eigenvalues))
        return map(lambda x: x/total_energy, np.cumsum(self.eigenvalues))

    def principal_components_for_target_energy(self, energy):
        assert 0 <= energy <= 1
        self._get_eigendata()
        sufficient_components = bisect_right(self.cumulative_energy(), energy) + 1
        return self.principal_components(sufficient_components)
