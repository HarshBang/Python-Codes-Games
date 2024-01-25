import pandas as pd

df = pd.read_csv('ch06/csv_mindex.csv',index_col=['key1','key2'])
print(df)
