import numpy as np
import sys
from knn.distances import euclidean_distance, cosine_distance


def get_best_ranks(ranks, top, axis=1, return_ranks=False):
    raise NotImplementedError()


class NearestNeighborsFinder:
    def __init__(self, n_neighbors, metric="euclidean"):
        self.n_neighbors = n_neighbors

        if metric == "euclidean":
            self._metric_func = euclidean_distance
        elif metric == "cosine":
            self._metric_func = cosine_distance
        else:
            raise ValueError("Metric is not supported", metric)
        self.metric = metric

    def fit(self, X, y=None):
        self._X = X
        return self

    def kneighbors(self, X, return_distance=False):
        axis = 1
        top = self.n_neighbors
        m = X.shape[0]

        distanceMatrix = self._metric_func(X, self._X)
        indexes = np.argpartition(distanceMatrix, top - 1, axis=axis) \
                    .take(indices=range(0, top), axis=axis)
        values = np.take_along_axis(distanceMatrix, indexes, axis=axis)
        cuttedSortedIndexes = np.argsort(values, axis=axis)

        resultDistances = np.take_along_axis(values, cuttedSortedIndexes, axis=axis)
        resulIndicies = np.take_along_axis(indexes, cuttedSortedIndexes, axis=axis)
        resultIndicies = np.tile(resulIndicies[:, 0].reshape(-1, 1), top)
        assert(resultDistances.shape == (m, top))

        if return_distance:
            return (resultDistances, resulIndicies)
        else:
            return resulIndicies
