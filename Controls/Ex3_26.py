# Example 3.26

import matplotlib.pyplot as plt
import  control
import numpy as np

plt.close()

#sys = 2s+1/s^2+2s+5
num = [2, 1] #numerator; 
den = [1, 2, 5] #denominator
sysH = control.tf(num,den)
t = np.arange(0,10,0.01) # time range for output
y0= control.impulse_response(sysH,t) #model impulse-response
x = np.asarray(y0[0])
y = np.asarray(y0[1])

plt.plot(x,y)
plt.title('Impulse-response')
plt.ylabel('y(t)')
plt.xlabel('time (s)')
plt.grid()

plt.show()