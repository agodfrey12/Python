#Chapter 4
#Graphing and Root Finding

import matplotlib.pyplot as plt
import numpy as np

#define a range of x values for plotting
xp = np.arange(0,10,0.1) #arrau from 0-10 in increments of 0.1
def f0(x): return(x-4)*(x-6)
yp = f0(xp)
plt.plot(xp,yp,'b') #plot w/ blue line
plt.grid(True)
plt.xlabel('X')
plt.ylabel('y=(x-4)(x-6)')

xp2=np.array([3.5,4.5])
yp2=f0(xp2)
plt.plot(xp2,yp2,'r*')

xp2=np.array([3.75,4.25])
yp2=f0(xp2)
plt.plot(xp2,yp2,'g*')

xp2=np.array([3.9,4.1])
yp2=f0(xp2)
plt.plot(xp2,yp2,'k*')

