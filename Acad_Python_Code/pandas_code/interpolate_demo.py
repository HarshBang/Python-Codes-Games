import pandas as pd
import numpy as np
a=pd.Series([0,1,np.nan,3,4,5,7,np.nan,9])
print(a)
print("------------")
b=a.interpolate() # Linear Interpolation
print(b)
