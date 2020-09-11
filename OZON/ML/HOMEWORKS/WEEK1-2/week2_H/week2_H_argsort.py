import numpy as np


def get_best_indices(ranks, top, axis=1):
    indexes = np.argpartition(-ranks, top - 1, axis=axis).take(indices=range(0, top), axis=axis)
    values = np.take_along_axis(-ranks, indexes, axis=axis)
    cuttedSortedIndexes = np.argsort(values, axis=axis)
    return np.take_along_axis(indexes, cuttedSortedIndexes, axis=axis)


if __name__ == "__main__":
    with open('input.bin', 'rb') as f_data:
        ranks = np.load(f_data)

    indicies = get_best_indices(ranks, 5)

    with open('output.bin', 'wb') as f_data:
        np.save(f_data, indicies)
