import numpy as np

def impute(X: list, method: str = "mean") -> list:
    """
    Returns a new matrix with missing entries filled.
    """
    X = np.array(X, dtype=float)
    X1 = np.zeros((len(X),len(X[0])))
    
    for i in range (0,len(X)):
        for j in range (0,len(X[0])):
            if np.isnan(X[i][j]):
                if np.sum(~np.isnan(X[:,j])) == 0:
                    X1[i,j] =0 
                    
                elif method == "mean":
                    X1[i,j] = np.nanmean(X[:,j] )
                else:
                    X1[i,j] = np.nanmedian(X[:,j] )
            else:
                X1[i,j] = X[i][j]
                
    return X1