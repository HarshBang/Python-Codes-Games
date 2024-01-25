import pandas as pd

chunker = pd.read_csv('ch06/ex6.csv', chunksize=1000)
tot=pd.Series([])
for piece in chunker:
	tot=tot.add(piece['key'].value_counts(), fill_value=0)
print(tot)
