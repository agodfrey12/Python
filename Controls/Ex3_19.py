#Example 3.19

import control.matlab
import numpy as np
import matplotlib.pyplot as plt

plt.close()

#sys = 100/(s^2+10.1s+101) this is G(s)

sys = control.tf([100], [1,10.1,101])
t = np.arange(0,5,0.01) #time range

y = control.step_response(sys, t) #this is y_out ## can also be an impulse_response
x = np.asarray(y[0])
y1 = np.asarray(y[1])

plt.figure()
plt.plot(x,y1)
plt.grid()
plt.xlabel('time (s)')
plt.ylabel('Angle (rad/s)')

plt.show()