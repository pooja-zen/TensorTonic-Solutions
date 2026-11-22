import numpy as np

def matrix_multiply(A: list, B: list) -> np.ndarray:
    """
    Returns the matrix product as a float64 array.
    """
    C = np.zeros((len(A),len(B[0])), dtype=float)
    for i in range (0,len(A)):
        for j in range (0,len(B[0])):            
            C[i,j] = float(sum(A[i][J] * B[J][j] for J in range (0,len(A[0]))))
    return C