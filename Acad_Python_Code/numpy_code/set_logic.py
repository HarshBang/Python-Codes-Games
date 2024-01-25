import numpy as np
names = np.array(['Bob','Will', 'Joe', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
uni_names=np.unique(names)
print(uni_names)
print("alternative way",sorted(set(names)))
ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
print(np.unique(ints))
values = np.array([6, 0, 0, 3, 2, 5, 6])
print(np.in1d(values, [2, 3, 6]))
