import random

import matplotlib as mpl
mpl.use('TkAgg')
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from numpy import linalg


def random_point_of_dimension(dimension):
    return pd.DataFrame(np.random.randn(1, dimension))


def sample_dataframe_rows(df, n):
    if n > len(df):
        raise ValueError('Cannot fetch more rows than the size of DataFrame')

    return pd.DataFrame(
        df.iloc[random.sample(df.index, n)],
    )


def basic_dataframe_plot(df):
    if len(df.columns) > 2:
        raise NotImplementedError('Cant project higher dimension points to 2D yet')

    df.plot(x=0, y=1, linestyle="", marker="o", c='b')
    plt.show()


def center_dataframe(df):
    means = pd.DataFrame()
    row_count = len(df)

    for i in xrange(len(df.columns)):
        means[i] = df.iloc[:, i].mean() * np.ones(row_count)

    return df - means.values


def covariance_dataframe(df):
    n = len(df)
    return np.dot(np.transpose(df), df) / (n - 1)


def decreasing_eigenvalues_with_eigenvectors(df):
    eigengvalues, eigenvectors = linalg.eig(df)

    eigengvalues = list(eigengvalues)
    eigenvectors = pd.DataFrame(eigenvectors)

    d_eigenvalues = []
    d_eigenvectors = pd.DataFrame()

    for col in xrange(len(eigengvalues)):
        max_eigenvalue = max(eigengvalues)
        location = eigengvalues.index(max_eigenvalue)
        d_eigenvalues.append(max_eigenvalue)
        eigengvalues[location] = None
        d_eigenvectors[col] = eigenvectors.iloc[:, location]

    return d_eigenvalues, d_eigenvectors


def first_columns(df, n):
    if n > len(df.columns):
        raise ValueError('Can fetch up to {} columns for DataFrame'.format(len(df.columns)))

    return df.iloc[:, 0:n]


def outer_product(first, second):
    return np.dot(first, second)
