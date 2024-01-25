import pandas as pd
import numpy as np
from numpy import nan as NA
data = pd.Series([1, NA, 3.5, NA, 7]) 
print(data)
print("---------------")
print(data.dropna()) 
print("---------------")
df1 = pd.DataFrame([[1., 6.5, 3.], [1., NA, NA], [NA, NA, NA], [NA, 6.5, 3.]])
cleaned_df = df1.dropna()
print(df1)
print("---------------")
print(cleaned_df)
print("---------------")
print(df1.dropna(how='all'))
print("---------------")
df1[4] = NA
print(df1)
print('')
#print("---------------")
print(df1.dropna(axis=0,how='all'))
print('')
print(df1.dropna(axis=1,how='all'))
