import numpy as np

def kmeans_plusplus(X: list, k: int, seed: int = 42) -> list:
    selected_indices = []
    #First data point
    rng = np.random.RandomState(seed) 
    indices = rng.randint(len(X), size=1) 
    selected_indices.append(indices)
      
    mu = [list(map(float, X[i])) for i in indices] #Array of centroids - initialization

    for t in  range (1, k): #Subsequent centroids
        dis_p = np.zeros((len(X), t))
        b =  np.zeros((len(X), t))
        
        
        for i in range (0,len(X)): # No. of data points
            for j in range (0,t): # No. of centroids
                dis_p[i,j] = sum((mu[j][c] - X[i][c]) ** 2 for c in range (0,len(X[0])))
        
        for i in range (0,len(X)): # No. of data points
            j = np.argmin(dis_p[i,:])
            b[i,j] = 1       
        

        P =  np.zeros((len(X)))
        for i in range (0,len(X)): #Probability            
            P[i] = min(dis_p[i,:]) / sum(min(dis_p[j,:])for j in range (0,len(X)))
               
        if max(P[:]) != 0:   
            indices = rng.choice(len(X), p=P) 
        else:
            indices = rng.choice(len(X)) 
        selected_indices.append(indices)
        
        mu.append(list(map(float, X[indices]))) #Subsequent centroids - initialization
        print(selected_indices)
 
    return mu
