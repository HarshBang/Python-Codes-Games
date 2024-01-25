import pandas as pd
import numpy as np
ind = pd.Index(np.arange(3))
obj1 = pd.Series([1.5, -2.5, 0], index=ind)
ind1 = pd.Index(np.arange(5))
obj2 = pd.Series([2.5, -2.5,1,-1,0], index=ind1)
ind2=obj1.append(obj2)
print(ind2)
