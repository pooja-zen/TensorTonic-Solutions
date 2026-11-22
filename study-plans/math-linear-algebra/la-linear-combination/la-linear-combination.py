import numpy as np

def linear_combination(vectors: list, coefficients: list) -> np.ndarray:
    """
    Returns the weighted sum as a float64 vector.
    """
    w = np.zeros(len(vectors[0]), dtype = float)
    for j in range (0,len(vectors[0])): 
        w[j] = float(sum(coefficients[i] * vectors[i][j] for i in range (0,len(vectors))))

    return w