import numpy as np
import matplotlib.pyplot as plt

plt.close("all")

accel = np.loadtxt('C:/Users/Aaron Godfrey/Desktop/School/Senior Year/Fall 2021/Instrumentation/CPB Modules/Acceleration.txt', delimiter=',')
light = np.loadtxt('C:/Users/Aaron Godfrey/Desktop/School/Senior Year/Fall 2021/Instrumentation/CPB Modules/Light.txt', delimiter=',')
sound = np.loadtxt('C:/Users/Aaron Godfrey/Desktop/School/Senior Year/Fall 2021/Instrumentation/CPB Modules/Sound.txt', delimiter=',')
temp = np.loadtxt('C:/Users/Aaron Godfrey/Desktop/School/Senior Year/Fall 2021/Instrumentation/CPB Modules/Temperature.txt', delimiter=',')

t1 = accel[:,0]
x = accel[:,1]
y = accel[:,2]
z = accel[:,3]

t2 = light[:,0]
light = light[:,1]

t3 = sound[:,0]
sound = sound[:,1]

t4 = temp[:,0]
temp = temp[:,1]

plt.figure()
plt.plot(t1,x)
plt.plot(t1,y)
plt.plot(t1,z)
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Acceleration')
plt.title('Acceleration vs Time')

plt.figure()
plt.plot(t2,light)
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Light')
plt.title('Light vs Time')

plt.figure()
plt.plot(t3,sound)
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Sound')
plt.title('Sound vs Time')

plt.figure()
plt.plot(t4,temp)
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Temperatiure (C)')
plt.title('Temperature vs Time')