import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a float.
    """
    if np.sqrt(np.dot(a,a)) * np.sqrt(np.dot(b,b)) != 0:
        return float(np.dot(a,b)/np.sqrt(np.dot(a,a)) / np.sqrt(np.dot(b,b)))
    else:
        return float(0)