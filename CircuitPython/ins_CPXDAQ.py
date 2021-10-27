import numpy as np
import matplotlib.pyplot as plt

plt.close("all")

data = np.loadtxt('C:/Users/Aaron Godfrey/Desktop/School/Senior Year/Fall 2021/Instrumentation/CPX DAQ/CPXDAQ.txt')

t = data[:,0]
buttonA = data[:,1]
buttonB = data[:,2]

plt.figure()
plt.plot(t,buttonA)
plt.plot(t,buttonB)
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Button Values')
plt.title('Buttons vs Time')

plt.figure()
plt.plot(t,buttonA)
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('ButtonA Value')
plt.title('Button A vs Time')

plt.figure()
plt.plot(t,buttonA)
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('ButtonB Value')
plt.title('Button B vs Time')