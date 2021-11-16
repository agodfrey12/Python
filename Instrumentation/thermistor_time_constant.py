import numpy as np
import matplotlib.pyplot as plt

plt.close()

data = np.loadtxt('Temp_data.txt', delimiter=',')

time = data[:,0]
time -= time[0]
temp = data[:,1]

Ts = 500
s = 4.0/Ts
TA = 25.0
TH = 50.15
t = np.linspace(time[0], time[-1], 1000)
T = (TA-TH)*(1-np.exp(-s*t)) + TH

plt.plot(time, temp, 'b*')
plt.plot(t, T, 'r-')
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Temp (C)')
print('Time constant =', 1/s, 'sec')

plt.show()