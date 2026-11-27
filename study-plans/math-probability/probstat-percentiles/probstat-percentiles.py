import numpy as np

def percentiles(x: list, q: list) -> np.ndarray:
    """
    Returns the requested percentiles as a float64 array.
    """
    y = x #input sorted
    for i in range (0,len(x)):
        for i in range (0,len(x)-i-1):
            if y[i] > y[i+1]:
                y[i], y[i+1] = y[i+1], y[i]
    
    output = np.zeros(len(q))
    for i in range (0, len(q)):
        estimate = q[i] / 100 * (len(y)-1)
        integer = int(np.floor(estimate))
        frac = estimate - integer
        if estimate != integer:
            output[i] = y[integer] + frac * (y[integer+1]-y[integer])
        else:
            output[i] = y[integer]
    return output