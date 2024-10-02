import pandas as pd
import numpy as np

s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([2.2,np.nan,3.0,1.5], index=['a', 'b', 'c', 'd'])
s3 = pd.Series(['q','q','z','z'], index=['a', 'b', 'c', 'd'])
df = pd.DataFrame({'s1':s1, 's2':s2, 's3':s3})
print(df.iloc[0:2,0:2])
grade = df.loc['c','s2']
print(grade)
qs = df.loc['a':'b','s3']
print(qs)
print(df.iloc[2:4:,2:4])