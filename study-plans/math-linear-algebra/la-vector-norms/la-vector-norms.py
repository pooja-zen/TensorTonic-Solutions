import numpy as np

def vector_norms(v: list) -> np.ndarray:
    """
    Returns a float64 array containing the L1, L2, and infinity norms.
    """
    return np.array([np.sum(np.abs(v)), np.sqrt(np.dot(v,v)), np.max(np.abs(v))])