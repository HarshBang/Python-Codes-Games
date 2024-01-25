'''
Suppose you had a matrix of randomly generated data
and you wanted to replace all positive values with 2 
and all negative values with -2. 
This is very easy to do with np.where:
'''
import numpy as np
arr = np.arange(16)
arr2=arr.reshape(4,4)
print(arr)
print(arr2)
arr1=np.where(arr2 > 2, 2, -2)
print(arr1)
arr2=np.where(arr2 > 2, 2, arr2)
print(arr2)