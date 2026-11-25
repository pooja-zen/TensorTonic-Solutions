import numpy as np

def linear_regression_from_scratch(X: list, y: list, lr: float, epochs: int) -> tuple:
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
    y_tilde = np.zeros(len(X))
   
    for e in range (0,epochs): # No. of evaluations 
        for i in range (0,len(X)): #Predicted value for each sample
            y_tilde[i] = sum(X[i][j] * p[j]  for j in range (0,len(X[0]))) + b 
        for j in range (0, len(X[0])): # weight derivative
            d1[j] = 2 / n * sum( XT[j,i] * (y_tilde[i] - y[i]) for i in range (0,len(X)) )
            p[j] = p[j] - lr * d1[j] #Update
        
        d2 = 2 / n * sum((y_tilde[i] - y[i]) for i in range (0,len(X)) ) #bias derivative 
            
        b = b - lr * d2 #Update
   
    return p, b
