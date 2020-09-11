import numpy as np
import numpy.ma as ma


def replace_nan_to_means(X):
    mask = ma.array(X, mask=np.isnan(X)).mean(axis=0)
    return np.where(np.isnan(X), ma.array(X, mask=np.isnan(X)).mean(axis=0), X)
