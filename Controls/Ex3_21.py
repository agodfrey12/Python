#Example 3.21

import matplotlib.pyplot as plt
import control
import control.matlab
import numpy as np

plt.close()

# define satellite system by its TF sys = 0.0002/s^2 

sys = 0.0002*control.tf([1],[1,0,0])  #control.tf(numerator,denominator)
SS = control.tf2ss(sys) #transform to state-space
t = np.arange(0,10,.01)

u1 = np.zeros(len(t)) #define the input

for i in range(500,511):  
    u1[i] = 25; #pulse input
for i in range(600,611):  
    u1[i] = -25; #pulse input

y0 = control.matlab.lsim(SS,u1,t); #linear simulation
ff = 180/np.pi; # conversion factor from radians to degrees
y = np.asarray(y0[0])*ff
x = np.asarray(y0[1])

plt.figure()
plt.plot(x,u1)
plt.xlabel('time')
plt.ylabel('thrust (N)')
plt.grid()
    
plt.figure()
plt.plot(x,y)   # plot output response
plt.xlabel('time (s)')
plt.ylabel('angle (deg)')
plt.grid()

plt.show()