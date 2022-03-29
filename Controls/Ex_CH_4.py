#Example CH4

import control
import numpy as np
import matplotlib.pyplot as plt

plt.close()

# Define the output time range
t = np.arange(0,30,.01)

# sys = G/(1+GDc)
# G = 1/(s^2+z*s+wn^2)
# Dc = KI/s
z = 0.707
wn = 1 
KI = .5

G = control.tf(1,(1,2*z*wn,wn**2))
Dc = control.tf(KI, (1,0))
sysIW = G/(1+G*Dc)
y0=control.step_response(sysIW,t)

# plt.plot(t,yIW[1])
# plt.grid('on')
# plt.ylim(-.5, 1.5)
# sys = GDc/(1+GDc)
# G=1/(s^2+z*s+wn^2)
# Dc = KI/s

KI = 0.5
sysI = G*Dc/(1+G*Dc)
yI = control.step_response(sysI,t)
plt.plot(t,yI[1],'b')
plt.grid()
plt.ylim(-.5, 1.5)

# sys = GDc/(1+GDc)
# G = 1/(s^2+z*s+wn^2)
# Dc = Kp = 1.5

Kp = 1.5
Dc = Kp 
sysP = G*Dc/(1+G*Dc)
yP=control.step_response(sysP,t)
plt.plot(t,yP[1],'g')

# Dc = Kp = 6
Kp = 6; Dc = Kp;
sysP2 = G*Dc/(1+G*Dc)
yP2=control.step_response(sysP2,t)

# Plot step-responses with P and I contrllrs
plt.plot(t,yP[1],'g')
plt.plot(t,yP2[1],'r')
plt.xlabel('time (s)')
plt.xlabel('y(t)')
plt.legend(['Kp = 1.5','Kp = 1.5','Kp = 6.0'])


plt.show()