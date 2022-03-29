# Example 4.05

import control
import control.matlab as matlab
import numpy as np
import matplotlib.pyplot as plt

plt.close()

t = np.arange(0,30,.01)

# sys = GDc/(1+GDc)
# G = Ko/(Ts1*s+1)/(Ts2*s+1)
# Dc = Kp, Kp + KI/s

DcPI = 0.03 + 0.003*control.tf([1],[1,0])
DcP = 0.03
Ko = 1000 
T1 = 1 
T2 = 10
G = Ko*control.tf([1],[T1,1])*control.tf([1],[T2,1])
sysP = G*DcP/(1+DcP*G)
sysPI = G*DcPI/(1+DcPI*G)

# Simulate reference input u
n = len(t)

# steady-st signal
ref = 300*np.ones(n) 

# ramp function
ref[0:int(n/3)]=30*t[0:int(n/3)] 

# Declare the state-space system and
# call matlab.lsim for both P and PI
sys_ssP = control.tf2ss(sysP)
yP=matlab.lsim(sys_ssP,ref,t)
sys_ssPI = control.tf2ss(sysPI)
yPI=matlab.lsim(sys_ssPI,ref,t)

plt.figure()
plt.plot(t,ref, 'b')
plt.plot(t,yP[0],'r')
plt.plot(t,yPI[0], 'g')
plt.grid()
plt.xlabel('time (s)')
plt.ylabel('y(t)/r(t)')
plt.legend(['Ramp Input', 'P - controller', 'PI - controller'])

plt.show()