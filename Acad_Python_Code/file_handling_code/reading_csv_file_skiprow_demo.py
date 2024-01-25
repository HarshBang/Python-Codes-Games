import pandas as pd
r=pd.read_csv('ch06/ex4.csv')
result = pd.read_csv('ch06/ex4.csv', skiprows=[0,2,3])
print(result) 