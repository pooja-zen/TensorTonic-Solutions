import numpy as np
def categorical_encode(data: list, method: str = "label"):
    """
    Returns label-encoded metadata or one-hot rows.
    """

    if method == "label":
        data_encoded = np.zeros(len(data))
        data_alph = sorted(data)
        labels = (np.unique(data_alph))
        for j in range (0,len(data)):
            for i in range (0,len(labels)):
                if data[j] == labels[i]:
                    data_encoded[j] = i
        dict = {"classes":labels,"encoded":data_encoded}
    
    if method == "onehot":
        
        labels = (np.unique(data))
        data_encoded = np.zeros((len(data),len(labels)))
        for j in range (0,len(data)):
            for i in range (0,len(labels)):
                if data[j] == labels[i]:
                
                    data_encoded[j][i] = 1 
        dict = data_encoded
    
    return dict
