# Example 3.7

import  control
import control.matlab
import math
import numpy as np
import matplotlib.pyplot as plt

plt.close()

# LTI for given H(s) = s^2+100 and u(t) = exp^(-kt)
den = [1, 0, 100]            # define TF denominator
sys = control.TransferFunction(10,den)  # define system by its transfer function
t=np.arange(0,20,0.01)
SS=control.tf2ss(sys)         # convert to SS
u1=np.zeros(len(t),float)       # define pulse input

for i in range(0, len(t)):  
    u1[i]=math.exp(-1*i*.01);# pulse input
    
y0 = control.matlab.lsim(SS,U=u1,T=t) # linear simulation
y = np.asarray(y0[0])
x = np.asarray(y0[1])

plt.figure(1)
plt.plot(x,y)
plt.xlabel('time (s)')
plt.ylabel('output')
plt.grid()

plt.show()