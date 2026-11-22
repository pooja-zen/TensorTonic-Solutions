import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transpose as a float64 array.
    """
    B = np.zeros((len(A[0]),len(A)), dtype = float)
    for i in range (0,len(A)):
        for j in range (0,len(A[0])):
            B[j,i] = float(A[i][j])
    return B