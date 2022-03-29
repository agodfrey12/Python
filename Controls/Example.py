# Eaxmple

import control
import numpy as np
import matplotlib.pyplot as plt

plt.close()

# sys = G
# Dc = Kp
# TF = G*Dc/(1+G*Dc

z = 0.707 #damping
wn = 1 #natural frequency
Kp = 1.5 #proportional controller

G = control.tf(1, (1,2*z*wn, wn**2))
Dc = Kp

sysp = G*Dc/(1+G*Dc)

t = np.arange(0,30,0.01)
yP = control.step_response(sysp,t)

plt.figure()
plt.plot(yP[0], yP[1])
plt.grid()

plt.figure()
Dc = 6
sysp2 = G*Dc/(1+G*Dc)
yP2 = control.step_response(sysp2,t)
plt.plot(yP2[0], yP2[1])
plt.grid()


plt.show()