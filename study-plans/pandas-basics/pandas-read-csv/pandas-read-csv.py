import pandas as pd

def create_dataframe(data: dict) -> dict:
    """
    Returns a dictionary with data, shape [rows, columns], and ordered column names.
    """
    data1 = pd.DataFrame(data)
    dict1 = {"data": data1.to_dict('list') , "shape":list(data1.shape), "columns":data1.columns.tolist()}
    print(type(dict(data1)))

    return dict1
