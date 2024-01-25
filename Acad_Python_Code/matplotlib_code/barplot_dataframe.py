import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.random import randn
df = pd.DataFrame(np.random.rand(6, 4),index=['one', 'two', 'three', 'four', 'five', 'six'],columns=pd.Index(['A', 'B', 'C', 'D'], name='Genus'))
#print(df)
df.plot(kind='bar')
plt.show()