#Example 3.30

import matplotlib.pyplot as plt
import control
import numpy as np

plt.close()

#Aircraft response sys = 30(s-6)/s^3+4s^2+13s
u = -1 #delta function
sys = u*30*control.tf((1,-6),(1,4,13,0)) #transfer function
t = np.arange(0,6,.01) #time range for output
Y0 = control.impulse_response(sys,t) #model impulse-response

plt.figure()
plt.plot(Y0[0],Y0[1])
plt.xlabel('time (s)')
plt.ylabel('Altitude (ft)')
plt.grid()

plt.show()