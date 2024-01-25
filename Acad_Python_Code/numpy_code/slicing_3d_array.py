import numpy as np
a3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(a3d)
print("==================")
print(a3d[0])
print("==================")
print(a3d[1])
print("==================")
#Both scalar values and arrays can be assigned to a3d[0]
old_v=a3d[0].copy()
a3d[0]=789
print(a3d)
print("==================")
a3d[0]=old_v
print(a3d)
print("==================")
print(a3d[1,0]) #give all the values whose indices start with (1,0)
print("==================")
print(a3d[1,0,1]) #give single element at specified location