import math
import numpy as np

def distance_metric(x: list, y: list, metric: str, p: float = 2) -> float:
    """
    Returns the selected distance as a rounded float.
    """
    for i in range (0,len(x)):
       
        if metric == "euclidean":
            dis =  round( (sum((x[i]-y[i])**2 for i in range (0,len(x))))**0.5,4)
        elif metric == "manhattan":
            dis = round(sum(abs(x[i]-y[i]) for i in range (0,len(x))) , 4)
        elif metric == "cosine":
            if (sum(x[i] ** 2 for i in range (0,len(x))) * sum(y[i] ** 2 for i in range (0,len(x)))) ** 0.5 == 0:
                dis = 0
            else:
                dis = round(1 - np.dot(x,y) / (sum(x[i] ** 2 for i in range (0,len(x))) * sum(y[i] ** 2 for i in range (0,len(x)))) ** 0.5,4)
        elif metric == "chebyshev":
            dis = round(max(abs(x[i]-y[i]) for i in range (0,len(x))),4)
        else:
            dis = round( (sum(abs(x[i]-y[i]) ** p for i in range (0,len(x)))) ** (1/p), 4) 
            
    return dis
