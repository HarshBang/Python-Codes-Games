import numpy as np
import matplotlib.pyplot as plt

points = np.arange(-5, 5, 0.01) # 1000 equally spaced points
#print(points)
xs, ys = np.meshgrid(points, points)
z = np.sqrt(xs ** 2 + ys ** 2)
print(z)
im=plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
plt.show()