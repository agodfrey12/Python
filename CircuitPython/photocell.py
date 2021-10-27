import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('C:/Users/Aaron Godfrey/Desktop/School/Senior Year/Fall 2021/Instrumentation/Photocell/Photocell_data.txt',delimiter=',')

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