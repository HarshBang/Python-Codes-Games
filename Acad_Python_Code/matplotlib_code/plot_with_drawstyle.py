import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn
data = randn(30).cumsum()
plt.plot(data, 'k--', label='Default')
plt.plot(data, 'k-', drawstyle='steps-post', label='steps-post')
plt.show()
 