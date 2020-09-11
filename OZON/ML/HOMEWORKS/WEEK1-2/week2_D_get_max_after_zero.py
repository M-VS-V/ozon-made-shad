import numpy as np


def get_max_after_zero(x):
    zeroIndexies = np.where(x == 0)[0]
    zeroIndexies = zeroIndexies[zeroIndexies != x.size - 1]
    if zeroIndexies.size == 0:
        return None
    else:
        return x[zeroIndexies + 1].max()

