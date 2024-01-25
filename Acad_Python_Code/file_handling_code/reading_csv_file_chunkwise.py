import pandas as pd

result = pd.read_csv('ch06/ex6.csv')
print(result)
#if you want to read small number of rows nrows is used
result1=pd.read_csv('ch06/ex6.csv',nrows=10)
print(result1)

# To read out a file in pieces, specify a chunksize as a number of rows:

chunker = pd.read_csv('ch06/ex6.csv', chunksize=1000)
print(chunker)