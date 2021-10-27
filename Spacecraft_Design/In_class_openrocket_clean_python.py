# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 10:34:01 2021

@author: Aaron Godfrey
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('',delimiter=',')

time = data[:,0]
altitude = data[:,1]
aoa = data[:,4]

plt.plot(time,altitude)
plt.plot(time,aoa)

plt.show()
