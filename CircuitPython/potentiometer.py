import numpy as np
import matplotlib.pyplot as plt

plt.close("all")

data = np.loadtxt('C:/Users/Aaron Godfrey/Desktop/School/Senior Year/Fall 2021/Instrumentation/Potentiometer/Val vs Time.txt', delimiter=",")

t = data[:,0]
val = data[:,1]


plt.figure()
plt.plot(t,val)
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('Voltage vs Time')