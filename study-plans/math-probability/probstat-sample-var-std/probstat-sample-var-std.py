import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns sample variance and standard deviation as Python floats.
    """
    if len(x) >= 2:
        n = len(x)
        variance = 1/(n-1) * sum((x[i] - sum(x[:])/n)**2 for i in range (0,n))
        std_dev = variance ** (1/2)
        output = {"variance":variance, "std_dev":std_dev}
        return output
    else:           
        pass