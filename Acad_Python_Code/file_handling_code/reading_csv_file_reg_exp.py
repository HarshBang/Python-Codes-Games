import pandas as pd

print(list(open('ch06/ex3.txt')))
result = pd.read_table('ch06/ex3.txt', sep='\s+')
print(result)