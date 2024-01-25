import numpy as np
a=np.arange(0,17,2)
print(a)
print(a[4])
print(a[5:9])
a[5:9]=1010
print(a)
a_slice=a[5:9]
a_slice[2]=2020
print(a)
print(a_slice[:])
a_slice[:]=3030
print(a)
