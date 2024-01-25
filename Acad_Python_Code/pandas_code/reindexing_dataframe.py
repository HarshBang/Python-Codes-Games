import pandas as pd
import numpy as np
frame1 = pd.DataFrame(np.arange(9).reshape((3, 3)),
                      index=['a', 'c', 'd'],
                      columns=['Ohio', 'Texas', 'California'])
print(frame1)
frame2 = frame1.reindex(['a', 'b', 'c', 'd'])
print(frame2)
states = ['Texas', 'Utah', 'California']
frame3=frame2.reindex(columns=states)
print(frame3)
frame4=frame3.reindex(index=['a', 'b', 'c', 'd','e'], method='bfill',
                      columns=states)
print(frame4) 