import pandas as pd
import sys
data = pd.read_csv('ch06/ex5.csv')
data.to_csv('ch06/out1.csv',na_rep='NULL')
data.to_csv(sys.stdout,na_rep='NULL')