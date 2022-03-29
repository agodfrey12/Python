# Example 4.06

import control
import numpy as np
import matplotlib.pyplot as plt

plt.close()

t = np.arange(0,6,.01)
n = len(t)

# sys = GDc/(1+GDc)
# G = Kt/Ra/(Jm*s^2+(1*b+Kt*Ke/Ra)*s)
# Dc = Kp, Kp + KI/s, Kp + KI/s +Kd*s

Jm = 1.13e-2/8
b = 0.028/8
La = 0.10
Ra = 0.45
Kt = 0.067 
Ke = 0.067
Kp = 2
KI = 13.5 
Kd = 0.2

# System
den = np.convolve([1,0],([1*Jm, 1*b+Kt*Ke/Ra])) 
G = control.tf(Kt/Ra,den)

# System with P-controller
DcP = Kp  # controller
sysP = G*DcP/(1+G*DcP) # closed loop TR
yP = control.step_response(sysP,t) # step response

# System with PI-controller
DcPI = (Kp + KI*control.tf([1],[1,0])) # controller
sysPI = DcPI*G/(1+DcPI*G) # closed loop TR
yPI = control.step_response(sysPI,t) # step response

# System with PID-controller
DcPID= Kp + KI*control.tf([1],[1,0]) + Kd*control.tf([1,0],[1]) # controller
sysPID = DcPID*G/(1+DcPID*G) # closed loop TR
yPID = control.step_response(sysPID,t) # step response

# STEP-RESPONSEs with all controllers 
plt.figure()
plt.plot(t,yP[1],'red')
plt.plot(t,yPI[1], 'green')
plt.plot(t,yPID[1], 'blue')
plt.grid()
plt.xlabel('time (s)')
plt.ylabel('y(t)')
plt.xlim(0, 6); plt.ylim(0, 2)
plt.legend(['P-controller', 'PI-controller', 'PID-controller'])

plt.show()