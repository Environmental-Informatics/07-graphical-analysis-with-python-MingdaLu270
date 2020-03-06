#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 13:28:37 2020

@author: lu270
"""

## import all useful packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import statsmodels.api as sm
import pylab as py

## read useful columns in csv file
data = pd.read_table('all_month.csv',sep=',',usecols=['time','latitude','longitude','mag','depth'])
data=data.dropna()

## hist for earthquake magnitudes
## bins=10 
plt.hist(magdata,bins=10,range=(0,10))
plt.xlabel('magitude')
plt.ylabel('appearance')
plt.title('Fig.1. Hist of Magnitude')
plt.show()


## KDE for earthquake magnitudes
KDE=stats.gaussian_kde(magdata) # gaussian kernel
KDE.covariance_factor=lambda:0.3 # width 
KDE._compute_covariance()

## plot KDE
x=np.sort(magdata)
y=KDE(np.sort(magdata))
plt.plot(x,y)
plt.xlabel('magnitude')
plt.ylabel('density')
plt.title('Fig.2. KDE')
plt.show()

## plot lat and long
lat=data['latitude']
long=data['longitude']
plt.scatter(long,lat) # long as x and lat as y
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.title('Fig.3. lat&long')
plt.show()


## normalized cumulative distribution plot
depdata=data['depth']
d=np.sort(depdata)
cd=np.linspace(0,1,len(d))
plt.plot(d,cd)
plt.xlabel('depth')
plt.ylabel('cumulative dist')
plt.title('Fig.4. cumulative distribution plot')
plt.show()


## magnitude vs depth plot
plt.scatter(magdata,depdata)
plt.xlabel('magnitude')
plt.ylabel('depth')
plt.title('Fig.5. magnitude vs depth')
plt.show()

## QQ plot for magnitude
sm.qqplot(magdata,line='45') # default normal distribution
plt.ylabel('earthquake data quantile')
plt.title('Fig.6. QQ plot')
py.show() # data not lie on the 45 degree line, which normal distribution may not be applied










