import numpy as np
import pandas as pd
arr = np.array([[4, 7], [15,18],[18,21], [13,19],[10,15], [7,12],
                [4,6], [5,9], [8,10], [9,14], [13,15], [11,12], [12,17]])
arr_tp = arr.transpose()
df = pd.DataFrame({'col1': arr_tp[0], 'col2': arr_tp[1]})
print(df) 