import numpy as np

def outer_product(u: list, v: list) -> np.ndarray:
    """
    Returns the float64 outer-product matrix.
    """
    ut = np.transpose(u)
    v= np.array(v)
    
    uv = np.zeros((len(ut), len(v)), dtype=float)
   
    for i in range(len(ut)):
        for j in range(len(v)):
            uv[i,j] = float(ut[i] * v[j])
           
    return uv