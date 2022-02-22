import control
import control.matlab
import math
import numpy as np
import matplotlib.pyplot as plt

# LTI for given H(s) = s^2 + 100 and u(t) = exp^(-kt)

den = [1,0,100]                 # define TF denominator
sys = control.tf([10], den)     # define system by its transfer function
t = np.arange(0,20,0.01)
u1 = np.zeros((len(t)))         # define pulse input

for i in range(1, len(t)):
    u1[i] = math.exp(-1*i*0.01) #pulse input

y0 = control.matlab.lsim(sys,u1,t) #linear simulation

y = np.asarray(y0[0])
x = np.asarray(y0[1])

plt.figure()
plt.plot(x,y)
plt.xlabel('time (s)')
plt.ylabel('output')    
plt.grid()

plt.show()