import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a float.
    """
    return float(np.sqrt(np.dot(x,x) + np.dot(y,y) - 2 * np.dot(x,y) ))