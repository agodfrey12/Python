##Example 2.1

import control
import numpy as np
import matplotlib.pyplot as plt

#system = 1/m/(s+b/m)
m = 1000 #mass
b = 50 #friction coefficient
u = 500 #applied force in N

### tf = numerator / denominator = (1/m)/(s+b/m)
num = [1/m]
den = [1,b/m]
sys = u*control.tf(num,den) #transfer function
t = np.arange(0,100,0.1)
y0 = control.step_response(sys,t) #step response and time domain
x = np.asarray(y0[0])
y = np.asarray(y0[1])

plt.plot(x,y)
plt.title("Car Speed")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()

plt.show()