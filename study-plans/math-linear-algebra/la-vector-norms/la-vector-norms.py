import numpy as np

def vector_norms(v: list) -> np.ndarray:
    """
    Returns a float64 array containing the L1, L2, and infinity norms.
    """
    return  np.array([ float(sum( np.abs(v) )), float(np.sqrt( np.dot(v,v))), float(np.max(np.abs(v))) ])
   