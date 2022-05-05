import json
import pandas as pd
import numpy as np
with open('db.json', 'r') as file:
    file_dict = json.load(file)
    actual_data = file_dict["data"]
    array_2d = [[values for key, values in data.items()]
              for data in actual_data]
    
    df = pd.DataFrame(np.array(array_2d),  columns=['Blog Post Id', 'Date', 'Count'])
    
    print(df.head(10))
