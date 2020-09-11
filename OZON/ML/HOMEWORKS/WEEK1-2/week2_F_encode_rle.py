import numpy as np


def encode_rle(X):
    n = len(X)
    unequalsFlags = np.array(X[1:] != X[:-1])
    unequalsIndecies = np.append(np.where(unequalsFlags), n - 1)
    counts = np.diff(np.append(-1, unequalsIndecies))
    return (X[unequalsIndecies], counts)
