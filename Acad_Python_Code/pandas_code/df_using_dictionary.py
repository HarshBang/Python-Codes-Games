import pandas as pd
import numpy as np
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
'year': [2000, 2001, 2002, 2001, 2002],
'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = pd.DataFrame(data)
print(frame)
frame = pd.DataFrame(data, columns=['year', 'state', 'pop'])
print(frame)
#if you pass a column that isn’t contained in data, 
#it will appear with NA values in the result:
frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five'])
print(frame2)
print(frame2.columns) #gives name of all columns
#individual columns can be accessed like dictionary or like attribute
print(frame2['state'])
print(frame2.state)
#Rows can also be retrieved by position or name by a couple of methods(ix(0.20)deprecated)
print(frame2.iloc[:2,])
print(frame2.iloc[4:,])
#Columns can be modified by assignment
frame2['debt'] = 16.5
print(frame2)
frame2['debt'] = np.arange(5)
print(frame2)
'''
When assigning lists or arrays to a column, 
the value’s length must match the lengthof the DataFrame. 
If you assign a Series, 
it will be instead conformed exactly to the DataFrame’s index, 
inserting missing values in any holes
'''
val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
print(frame2)

'''
Assigning a column that doesn’t exist will create a new column. 
The del keyword will delete columns as with a dict
'''
frame2['eastern'] = frame2.state == 'Ohio'
print(frame2)
del frame2['eastern']
print(frame2)