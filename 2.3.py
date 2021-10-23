# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 09:58:16 2021

@author: 翟君伟
"""


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
%matplotlib inline

met = pd.read_csv("Marine_CSV_sample.csv")
met= met[['Time of Observation','Sea Level Pressure','Air Temperature','Wind Speed']].dropna(axis=0)
met
met.head()
#查找最大海平面气压
number1 = met['Sea Level Pressure'].max()
number1
#查找海平面气压大于10并且大气温度小于70的数组
met2 = met.loc[ (met['Sea Level Pressure'] >10) & (met['Air Temperature'] <70)]
met2
#查找大气温度最大值
number2 =met[Air Temperature'].max()
number2
#查找风速最大值
number3 =  met['Wind Speed'].max()
number3
#计算风速的总和
number4 = met['Wind Speed'].sum()
number4
