import pandas as pd
import numpy as np
frame = pd.DataFrame(np.arange(12.).reshape((4, 3)),
                     columns=list('bde'),index=['Utah', 'Ohio', 'Texas', 'Oregon'])
series = frame.iloc[1]
print(frame,"\n",series)
