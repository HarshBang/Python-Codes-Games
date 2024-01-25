import pandas as pd
import numpy as np
from numpy import nan as NA
df = pd.DataFrame(np.random.randn(7, 3))
print(df)
print("---------------")
'''df.iloc[:4, 1] = NA 
df.iloc[:2, 2] = NA 
print(df)
print("---------------")
df1=df.fillna(0)
print(df1)
print("---------------")
df2=df.fillna({1: 0.5, 3: -1})
print(df2)
print("---------------")
df3=df.fillna(method='bfill')
print(df3)
print("---------------")
df4=df.fillna(method='bfill', limit=2)
print(df4)
print("---------------")
data = pd.Series([1., NA, 3.5, NA, 7])   
print(data.fillna(data.mean()))
'''
df.iloc[2:4]=NA
df1=df.fillna(25)
print(df)
print(df1)
