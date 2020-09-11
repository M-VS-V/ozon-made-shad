import numpy as np


def calc_expectations(h, w, X, Q):
    sums = np.cumsum(np.cumsum(Q, axis=0), axis=1)

    left = np.roll(sums, w, axis=1)
    left[:, 0:w] = 0

    up = np.roll(sums, h, axis=0)
    up[0:h, :] = 0

    leftUp = np.roll(np.roll(sums, w, axis=1), h, axis=0)
    leftUp[:, 0:w] = 0
    leftUp[0:h, :] = 0

    prob = sums - left - up + leftUp
    return prob * X
