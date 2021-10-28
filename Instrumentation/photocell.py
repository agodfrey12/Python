import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('Photocell_data.txt',delimiter=',')

time = data [:,0]
time-=time[0]
light_digital = data[:,1]
v = 3.3*light_digital/2.0**16

plt.plot(time,v)
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("V vs T")
plt.grid()
plt.show()