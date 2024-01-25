import numpy as np
arr = np.random.randn(8)
print(arr)
arr.sort()
print(arr)
arr = np.random.randint(-5,80,size=(5, 3))
print(arr)
arr.sort()
#print(arr)

arr.sort(0)
print(arr)
arr.sort(1)
#print(arr) 