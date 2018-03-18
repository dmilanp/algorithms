import random

import numpy as np
from matplotlib import pyplot as plt

import pandas as pd


def random_point_of_dimension(dimension):
    return pd.DataFrame(np.random.randn(1, dimension))


def random_dataframe_rows(df, num):
    if num > len(df):
        raise ValueError('Cannot fetch more rows than the size of DataFrame')

    return pd.DataFrame(
        df.iloc[random.sample(df.index, num)],
    )


def basic_dataframe_plot(df):
    if len(df.columns)> 2:
        raise NotImplementedError('Cant project higher dimension points to 2D yet')

    df.plot(x=0, y=1, linestyle="", marker="o", c='b')
    plt.show()