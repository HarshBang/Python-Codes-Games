import pandas as pd


df = pd.read_csv('ch06/ex2.csv',header=None)
print(df)

#user may specify columns name
print("\n")
df1=pd.read_csv('ch06/ex2.csv', names=['a','b','c','d','message'])
print(df1)
