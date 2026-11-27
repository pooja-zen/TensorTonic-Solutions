import numpy as np

def skewness_kurtosis(data: list) -> dict:
    """
    Returns adjusted statistics and their interpretations in a dictionary.
    """
    n=len(data)
    mean = sum(data[:])/(n)
    sd = (1/(n-1) * sum((data[i] - mean)**2 for i in range (0,n)))**0.5
    skewness = round(n/(n-1)/(n-2) *  sum(((data[i] - mean)/sd) ** 3 for i in range (0,n)),4)
    kurt = round(n*(n+1)/(n-1)/(n-2)/(n-3) *  sum(((data[i] - mean)/sd) ** 4 for i in range (0,n)) - 3 * (n-1)**2/(n-2)/(n-3),4)

    
    if skewness < 0.5 and skewness > -0.5:
        skew_inf = 'approximately symmetric'
    elif skewness < -0.5:
        skew_inf = 'left-skewed'
    elif skewness > 0.5:
        skew_inf = 'right-skewed'

    if kurt < -1:
        kurt_inf = 'platykurtic'
    elif kurt > 1:
        kurt_inf = 'leptokurtic'
    else:
        kurt_inf = 'mesokurtic'
    output = {"skewness":skewness, "kurtosis":kurt, "skew_interpretation":skew_inf, "kurtosis_interpretation":kurt_inf}
    
    return output