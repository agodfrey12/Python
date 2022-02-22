#Controls Chapter 2 Quiz

import numpy as np
import matplotlib.pyplot as plt
import control
import control.matlab

wn = 1.695 #rads^-1
A = wn**2
zeta = 0.59 #damping ratio

#sys = A/(s^2+2*zeta*wn+A)

sys = control.tf([A],[1,(2*zeta*wn),A])
t = np.arange(0,20,0.01) #time range

y = control.step_response(sys, t) 
x = np.asarray(y[0])
y1 = np.asarray(y[1])

plt.figure()
plt.plot(x,y1)
plt.title('Step Response to the Given Transfer Function')
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')

plt.show()