import numpy as np
import matplotlib.pyplot as plt

plt.close()

data = np.loadtxt('8in_osc_10hz.txt', delimiter=',', skiprows=0)

time = data[:,0]
time -= time[373]
z = data[:,1] - 9.81


Td = 2.2 #period
Ts = 50.6279-37.9739 #settling time
z0 = -60.6 #initial z
s = 4.0/Ts
wd = 2*np.pi/Td
wn = np.sqrt(wd**2 + s**2)
tfit = np.linspace(0,Ts,10000)
zfit = z0*np.exp(-s*tfit)*np.cos(wd*tfit)

plt.plot(time, z, 'b-', label='Measured Data')
plt.plot(tfit, zfit, 'r--', label='Fitted Data')
plt.title('10 Hz Sampling Rate')
plt.legend()
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Acceleration (m/s)')
plt.xlim(-0.5,13.0)

plt.show()