import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.random import randn
fig=plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
#indicate figure of 2x2 and we are working on first figure out of four
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
plt.plot(randn(50).cumsum(), 'k--') #k-- is style option try 'g-o'
ax1.hist(randn(100), bins=20, color='r', alpha=0.3)
ax2.scatter(np.arange(30), np.arange(30) + 3 * randn(30))
plt.show()
