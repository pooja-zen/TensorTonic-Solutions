import numpy as np

def outer_product(u: list, v: list) -> np.ndarray:
    """
    Returns the float64 outer-product matrix.
    """
  
    uv = np.zeros((len(u), len(v)), dtype=float)
   
    for i in range(len(u)):
        for j in range(len(v)):
            uv[i,j] = float(u[i] * v[j])
           
    return uv