import pandas as pd
import numpy as np
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
print(obj)
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print(obj2)
obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=5)
print(obj)
print(obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0))
obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4]); print(obj3)
obj4 = obj3.reindex(range(6), method='ffill')
print(obj4)