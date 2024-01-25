import pandas as pd
pop = {'Nevada': {2001: 2.4, 2002: 2.9},'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = pd.DataFrame(pop)
print(frame3)
#transpose of given dataframe
print(frame3.T)
#The keys in the inner dicts are unioned and sorted to form the index in the result.
#This isn’t true if an explicit index is specified
f=pd.DataFrame(pop, index=[2001, 2002, 2003])
print(f)