import numpy as np
import random
def kmeans(X: list, k: int, max_iters: int = 100, seed: int = 42) -> tuple:
    """
    Returns cluster labels and the final centroid matrix.
    """

    rng = np.random.RandomState(seed) 
    indices = rng.choice(len(X), size=k, replace=False) 
      
    mu = [list(map(float, X[i])) for i in indices] #Array of centroids - initialization

    print(mu)
    for t in range (0, max_iters): #No. of iterations     
        dis_p = np.zeros((len(X), k))
        b =  np.zeros((len(X), k))
        cust =  np.zeros((len(X)))
        
        for i in range (0,len(X)): # No. of data points
            for j in range (0,k): # No. of centroids
                dis_p[i,j] = sum((mu[j][c] - X[i][c]) ** 2 for c in range (0,len(X[0])))
        
        for i in range (0,len(X)): # No. of data points
            j = np.argmin(dis_p[i,:])
            b[i,j] = 1
                    
 
        J = sum(min(dis_p[i,j] for j in range (0,k)) for i in range (0,len(X)))
        
        for j in range (0,k):
            for c in range (0,len(X[0])):
                if sum(b[i,j] for i in range (0, len(X))) != 0:
                    mu[j][c] = sum( b[i,j] * X[i][c] for i in range (0,len(X))) / sum(b[i,j] for i in range (0, len(X)))
                else:
                    pass

        for i in range (0,len(X)): # Recomputing cluster labels
            for j in range (0,k): # No. of centroids
                dis_p[i,j] = sum((mu[j][c] - X[i][c]) ** 2 for c in range (0,len(X[0])))
        
        for i in range (0,len(X)): # No. of data points
            cust[i] = np.argmin(dis_p[i,:])
             
    return cust, mu
