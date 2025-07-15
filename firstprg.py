#Install and set up Python and essential libraries like NumPy and pandas.

import pandas as pd
import numpy as np

print('version of numpy',np.__version__)
print('version of pandas',pd.__version__)

#numpy operations
a=[1,2,3,4]
print(a)
print('type of a',type(a))
b=np.array([1,2,3,4])
print(b)
print('type of b',type(b))
print('dimension of b is',b.ndim)
c=np.array([[1,2,3,4],[5,6,7,8]])
print(c)
print('type of c is',type(c))
print('dimension of c is',c.ndim)
d=np.array([[[1,2,3,4],[5,6,7,8]],[[11,22,33,44],[55,66,77,88]]])
print(d)
print('type of c is',type(d))
print('dimension of c is',d.ndim)

#pandas operation
data={'name':['alice','bob','charlie'],'sec':['A','B','C']}
df=pd.DataFrame(data)
print(df)
print('columns in dataframe',df.columns)
