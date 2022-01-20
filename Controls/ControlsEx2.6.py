##Example 2.6

import matplotlib.pyplot as plt
import control
import numpy as np

m = 1;
L = 1; 
g = 9.81; 
R2D = 57.3
num = [1/m/L**2]
den = [1,0,g/L]
sys = control.tf(num,den)

t = np.arange(0,10,0.1)
y0 = control.step_response(sys,t) #linear
x = np.asarray(y0[0])
y = R2D*np.asarray(y0[1])

plt.plot(x,y);  #plot output response
plt.title("Step Response")
plt.xlabel('time(sec)')
plt.ylabel('Speed')
plt.grid()

plt.show()