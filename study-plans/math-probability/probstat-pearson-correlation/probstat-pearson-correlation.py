import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the float64 feature-correlation matrix.
    """
    corr = np.zeros((len(X[0]),len(X[0])))

    for i in range (0, len(X[0])):
        for j in range (0, len(X[0])):
            mean_i = sum(X[n][i] for n in range (0,len(X)))/len(X)
            mean_j = sum(X[n][j] for n in range (0,len(X)))/len(X)
            sd_i = sum((X[n][i]-mean_i) ** 2 for n in range (0,len(X)))
            sd_j = sum((X[n][j]-mean_j) ** 2 for n in range (0,len(X)))
    
            if sd_i ==0 or sd_j == 0:
               corr[i,j] = "Nan"
            else:       
               corr[i,j] = sum((X[n][i] - mean_i) * (X[n][j] - mean_j) for n in range (0,len(X))) / (sd_i *sd_j) ** 0.5

    return corr