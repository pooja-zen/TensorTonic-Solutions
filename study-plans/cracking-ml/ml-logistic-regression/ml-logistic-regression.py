import numpy as np

def logistic_regression(X: list, y: list, lr: float, n_iters: int) -> tuple:
    """
    Returns the fitted weight list and bias.
    """
    n = len(X) # No. of samples
    XT = np.zeros((len(X[0]),len(X))) #transpose
    for i in range (0, len(X[0])):
        for j in range (0, len(X)):
            XT[i,j] = X[j][i]
      
    p = np.zeros((len(X[0])))
    d1  = np.zeros((len(X[0])))
    b = 0
    z = np.zeros(len(X))
    z_c = np.zeros(len(X))
    pz = np.zeros(len(X))
   
    for e in range (0,n_iters): # No. of evaluations 
        for i in range (0,len(X)): #Predicted value for each sample
            z[i] = sum(X[i][j] * p[j]  for j in range (0,len(X[0]))) + b 
            z_c[i] = np.clip(z[i], a_min = -500, a_max = 500)
            pz[i] = 1/ (1+ np.exp(-z_c[i]))
        
        for j in range (0, len(X[0])): # weight derivative
            d1[j] = 1 / n * sum( XT[j,i] * (pz[i] - y[i]) for i in range (0,len(X)) )
            p[j] = p[j] - lr * d1[j] #Update
        
        d2 = 1 / n * sum((pz[i] - y[i]) for i in range (0,len(X)) ) #bias derivative 
            
        b = b - lr * d2 #Update
   
    return np.round(p,4), np.round(b,4)