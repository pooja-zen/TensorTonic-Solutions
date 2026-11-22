import numpy as np

def matrix_vector_multiply(A: list, x: list) -> np.ndarray:
    """
    Returns the matrix-vector product as a float64 array.
    """
    y = np.zeros((len(A)), dtype=float)
    for i in range (0,len(A)):                 
        y[i] = float(sum(A[i][j] * x[j] for j in range (0,len(A[0]))))
    return y