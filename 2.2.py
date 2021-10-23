# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 12:47:01 2021

@author: 翟君伟
"""


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
%matplotlib inline

df = pd.read_csv("2281305.csv")
df['direction angle'] = df['WND'].apply(lambda x: x.split(',')[0])  
df[' direction quality code'] = df['WND'].apply(lambda x: x.split(',')[1]) 
df[' type code'] = df['WND'].apply(lambda x: x.split(',')[2]) 
df['speed rate'] = df['WND'].apply(lambda x: x.split(',')[3]).astype(int)
df['speed quality code'] = df['WND'].apply(lambda x: x.split(',')[4]).astype(int)

df['Year-Month'] = df['DATE'].apply(lambda x: x.split('-')[0]+x.split('-')[1])
a = df.loc[df['speed quality code'] < 2].groupby('Year-Month')['speed rate'].count()
b = df.loc[df['speed quality code'] < 2].groupby('Year-Month')['speed rate'].sum()
df2 = (b/a) 
df2 = pd.DataFrame(df2)
df2
df2.plot()












