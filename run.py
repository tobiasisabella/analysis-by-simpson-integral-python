#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 17:50:23 2020

@author: isabellatobias
"""
#Code for data analysis using the Simpson rule

#Imports the required libraries
from __future__ import division
import pandas as pd
import matplotlib.pyplot as plt
from scipy import integrate

#Files with default values
data = pd.read_excel('default_values.xlsx', names=['TIME', 'Default'])
data.head()

#File with the tested samples
data2 = pd.read_excel('tested_values.xlsx', names=['TIME', 'Tested'])
data2.head()

#Values chosen from the files [lines,columns]
#We divided our values for 1000 ou 10000 because they were too big 
Time = data.iloc[46:, 0].values/1000
Default = data.iloc[46:, 2].values/100000
Tested = data2.iloc[11:, 1].values/100000

#Now we use the Simpson's Rule
#We are interested in the diference between the integrals
Integral = integrate.simps(Tested, Time)-integrate.simps(Default, Time)

#Figure size
#Plot the integral
plt.figure(figsize = (15,10))
plt.scatter(Time,Integral, color='b', label='Primeiro Momento')

#Name the x axis
#Name the y-axis
#Positions subtitles
#Place the title
#Place grid
plt.xlabel('Date')
plt.ylabel('Integral')
plt.legend(loc='best')
plt.title("Cicle")
plt.grid(True)

#Displays the graph
plt.show()
