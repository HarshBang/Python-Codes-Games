import numpy as np
import pandas as pd
string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'])
print(string_data)
print(string_data.isnull())
string_data[0] = None 
#Python None value is also treated as NA
print(string_data.isnull())
