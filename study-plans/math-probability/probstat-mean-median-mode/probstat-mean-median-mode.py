import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns mean, median, and mode as Python floats in a dictionary.
    """
    if x:
        y = x #input sorted
        for i in range (0,len(x)):
            for i in range (0,len(x)-i-1):
                if y[i] > y[i+1]:
                    y[i], y[i+1] = y[i+1], y[i]
        
        n = len(y)
        mean = sum(y[:])/n
        median = y[int((n+1)/2-1)] if n%2!=0 else (y[int(n/2)-1] + y[int(n/2)])/2


        values, counts = np.unique(y, return_counts=True)
        mode = values[np.argmax(counts)]
           
        output ={"mean": mean, "median":median, "mode":mode}
        
        return output
    else:
        pass
        