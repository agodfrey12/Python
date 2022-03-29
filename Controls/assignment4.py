# Assignment 4

import control
import numpy as np
import matplotlib.pyplot as plt
import control.matlab as matlab
from systemtype import *

plt.close()
'''
# Problem 4.16d
# sys type = 1
# PI Controller
t = np.arange(0,10,0.01)
KP = 160
KIn = -26*160
KId = 30
KD = 0
num = 1
den = np.convolve([1], ([1,2,0]))
r = t**0*np.heaviside(t,[1])/1

stype,err = systemtype(num,den,KP,KIn,KId,KD,[20],[1,20],r,t)

plt.figure()
plt.plot(t,r)
plt.grid()
'''
### Some other stuff
t = np.arange(1,10,0.01)
KP = 10
KD = 1
KIn = 0
KId = 0
num = 1
den = np.convolve([1],[1,0,0])
r = t**2*np.heaviside(t,1)/2

stype,err = systemtype(num,den,KP,KIn,KId,KD,1,1,r,t)

plt.figure()
plt.plot(t,r)
plt.grid()



plt.show()