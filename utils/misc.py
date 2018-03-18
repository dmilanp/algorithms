import numpy as np


def point_distance(first, second):
    return np.linalg.norm(first - second)


def random_color():
    return np.random.rand(3,)