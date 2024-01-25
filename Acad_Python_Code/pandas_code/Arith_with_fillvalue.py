import pandas as pd
import numpy as np
df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))
print(df1,"\n",df2)
print(df1 + df2)

print(df1.add(df2, fill_value=0))
print(df1)
print(df1.reindex(columns=['a','b','f','d','e'], fill_value=0))