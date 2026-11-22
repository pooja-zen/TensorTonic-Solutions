import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a Python float.
    """
    t=0
    for i in range (0,len(A)):
        for j in range (0,len(A[0])):
            if i==j:
                t=t+A[i][j]
    return float(t)