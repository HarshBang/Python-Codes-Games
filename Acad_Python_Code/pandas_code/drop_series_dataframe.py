import pandas as pd
import numpy as np
obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
print(obj)
print("~~~~~~~~~~~~~~~~~~")
new_obj = obj.drop('c')
print(new_obj)
print("~~~~~~~~~~~~~~~~~~")
print(obj.drop(['d', 'c']))
print("~~~~~~~~~~~~~~~~~~")
print(obj)
print("~~~~~~~~~~~~~~~~~~")
df1 = pd.DataFrame(np.arange(16).reshape((4, 4)),
index=['Ohio', 'Colorado', 'Utah', 'New York'],
columns=['one', 'two', 'three', 'four'])
print(df1)
print("~~~~~~~~~~~~~~~~~~")
print(df1.drop(['Colorado', 'Ohio']))
print("~~~~~~~~~~~~~~~~~~")
print(df1.drop('two',axis=1))
print("~~~~~~~~~~~~~~~~~~")
print(df1.drop(['two', 'four'], axis=1))
print("~~~~~~~~~~~~~~~~~~")
print(df1)