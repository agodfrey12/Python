import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sci

plt.close()

# 5*ydbldot + ydot + 1000y = 25 

def Derivatives(z,t):
    y = z[0]
    ydot = z[1]
    ydbldot = 5 - 1000*y - ydot
    
    zdot = np.asarray([ydot,ydbldot])
    return zdot

tout = np.linspace(0,10,10000)
yinitial = np.asarray([0,0])
yout = sci.odeint(Derivatives,yinitial,tout)

plt.plot(tout,yout)


plt.show()