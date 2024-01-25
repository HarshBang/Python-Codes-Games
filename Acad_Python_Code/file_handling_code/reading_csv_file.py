import pandas as pd
import matplotlib.pyplot as plt
#fig=plt.figure()
df = pd.read_csv('ch06/ex1.csv')
print(df)
df.plot()
plt.show()

# we may also read this file using table with specifiying delimeter
df1=pd.read_table('ch06/ex1.csv', sep=',')
print(df1)
