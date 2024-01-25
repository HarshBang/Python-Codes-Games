import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.random import randn
df = pd.DataFrame(np.random.randn(10, 4).cumsum(0),columns=['A', 'B', 'C', 'D'],index=np.arange(0, 100, 10))
df.plot()
plt.show()

