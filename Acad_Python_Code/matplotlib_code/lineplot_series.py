import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.random import randn
s = pd.Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
s.plot()
plt.show()

# Method 2 for line plot
'''
plt.plot(pd.Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10)))
plt.show()
'''