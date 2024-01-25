import pandas as pd
l1=['a','b','c','d','message']
df = pd.read_csv('ch06/ex2.csv')
print(df)
print('\n')
df = pd.read_csv('ch06/ex2.csv', names=l1)
print(df)
print('\n')
df = pd.read_csv('ch06/ex2.csv',names=l1,index_col='message')
print(df)
