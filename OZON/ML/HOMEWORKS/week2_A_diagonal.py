import numpy as np


def get_nonzero_diag_product(x):
    diags = x.diagonal()
    diagsGreaterThanZero = diags[diags > 0]
    if diagsGreaterThanZero.size == 0:
        return None
    else:
        return np.prod(diagsGreaterThanZero)
