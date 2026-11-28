import numpy as np

def feature_scale(X: list, method: str = "minmax") -> list:
    """
    Returns the independently scaled feature columns.
    """
    m = len(X)
    X_scaled = np.zeros((m, len(X[0])))
    for j in range (0, len(X[0])):
        for i in range (0, len(X)):
            if method == "minmax":
                denom  = (max(X[n][j] for n in range (0,m)) - min(X[n][j] for n in range (0,m)))
                if denom != 0 :
                    X_scaled[i,j] = round ( (X[i][j] - min(X[n][j] for n in range (0,m)))/ denom  , 4)
                else:
                    X_scaled[i,j] =0
                    
            elif method == "standard":   
                mean = sum(X[n][j] for n in range (0,m))/len(X)
                sd = (1/m * sum( (X[n][j] - mean) ** 2 for n in range (0,m)))**0.5
                if sd != 0:
                    X_scaled[i,j] = round((X[i][j] - mean)/sd , 4)
                else:
                    X_scaled[i,j] = 0
                    
                    
    return X_scaled
