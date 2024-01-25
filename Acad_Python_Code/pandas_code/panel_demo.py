import pandas as pd
import numpy as np

data = np.random.rand(2,4,5)
p = pd.Panel(data)
print(p)

# from dictionary of DataFrame objects
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
   'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
#print p