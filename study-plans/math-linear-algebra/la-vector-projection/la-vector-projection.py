import numpy as np

def vector_projection(u: list, v: list) -> np.ndarray:
    """
    Returns the float64 projection of u onto v.
    """
    p = np.zeros((len(u)),dtype=float)
    for i in range (0,len(u)):
        p[i] = float(np.dot(u,v)/np.dot(v,v) * v[i])
        
    return p