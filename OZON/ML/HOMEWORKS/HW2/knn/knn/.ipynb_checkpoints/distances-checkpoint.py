import numpy as np


def euclidean_distance(x, y):
    n = x.shape[0]
    m = y.shape[0]

    xn2 = np.tile(np.apply_along_axis(lambda x: np.linalg.norm(x) ** 2, 1, x).reshape(1, n).T, m)
    yn2 = np.tile(np.apply_along_axis(lambda x: np.linalg.norm(x) ** 2, 1, y), (n, 1))
    xyProduct = x @ y.T

    assert(xn2.shape == (n, m))
    assert(yn2.shape == (n, m))
    assert(xyProduct.shape == (n, m))
    PRECISION = 8

    return np.round(xn2 + yn2 - 2 * xyProduct, PRECISION) ** 0.5


def cosine_distance(x, y):
    n = x.shape[0]
    m = y.shape[0]

    xNorms = np.tile(np.apply_along_axis(np.linalg.norm, 1, x).reshape(1, n).T, m)
    yNorms = np.tile(np.apply_along_axis(np.linalg.norm, 1, y), (n, 1))
    xyProduct = x @ y.T

    assert(xNorms.shape == (n, m))
    assert(yNorms.shape == (n, m))
    assert(xyProduct.shape == (n, m))

    return 1.0 - xyProduct / xNorms / yNorms
