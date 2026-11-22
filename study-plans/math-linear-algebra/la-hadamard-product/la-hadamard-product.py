import numpy as np

def hadamard_product(A: list, B: list) -> np.ndarray:
    """
    Returns the element-wise product as a float64 array.
    """
    C = np.zeros((len(A),len(A[0])), dtype=float)
    for i in range (0,len(A)):
        for j in range (0,len(A[0])):            
            C[i,j] = A[i][j] * B[i][j] 
    return C