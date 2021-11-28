import numpy as np
import matplotlib.pyplot as plt

plt.close()

data = np.loadtxt('macdata.txt')
data2 = np.loadtxt('hallway.txt')

t =  data[:,0]
ax =  data[:,1]
ay =  data[:,2]
az =  data[:,3]
wx =  data[:,4]
wy =  data[:,5]
wz =  data[:,6]
bx =  data[:,7]
by =  data[:,8]
bz =  data[:,9]

t2 =  data2[:,0]
ax2 =  data2[:,1]
ay2 =  data2[:,2]
az2 =  data2[:,3]
wx2 =  data2[:,4]
wy2 =  data2[:,5]
wz2 =  data2[:,6]
bx2 =  data2[:,7]
by2 =  data2[:,8]
bz2 =  data2[:,9]

plt.figure()
plt.grid()
plt.title("Acceleration for Mac's Throw")
plt.xlabel('Time (sec)')
plt.ylabel('Acceleration (m/s^2)')
plt.plot(t, ax, 'b-', label='Ax')
plt.plot(t, ay, 'r-', label='Ay')
plt.plot(t, az, 'g-', label='Az')
plt.legend()

plt.figure()
plt.grid()
plt.title("Acceleration for Hallway Throw")
plt.xlabel('Time (sec)')
plt.ylabel('Acceleration (m/s^2)')
plt.plot(t2, ax2, 'b-', label='Ax')
plt.plot(t2, ay2, 'r-', label='Ay')
plt.plot(t2, az2, 'g-', label='Az')
plt.legend()

plt.figure()
plt.grid()
plt.title("Angular Velocity for Mac's Throw")
plt.xlabel('Time (sec)')
plt.ylabel('Angular Velocity (rad/s)')
plt.plot(t, wx, 'b-', label='wx')
plt.plot(t, wy, 'r-', label='wy')
plt.plot(t, wz, 'g-', label='wz')
plt.legend()

plt.figure()
plt.grid()
plt.title("Angular Velocity for Hallway Throw")
plt.xlabel('Time (sec)')
plt.ylabel('Angular Velocity (rad/s)')
plt.plot(t2, wx2, 'b-', label='wx')
plt.plot(t2, wy2, 'r-', label='wy')
plt.plot(t2, wz2, 'g-', label='wz')
plt.legend()

plt.figure()
plt.grid()
plt.title("Magnetic Field for Mac's Throw")
plt.xlabel('Time (sec)')
plt.ylabel('Magnetic Field (uTesla)')
plt.plot(t, bx, 'b-', label='bx')
plt.plot(t, by, 'r-', label='by')
plt.plot(t, bz, 'g-', label='bz')
plt.legend()

plt.figure()
plt.grid()
plt.title("Magentic Field for Hallway Throw")
plt.xlabel('Time (sec)')
plt.ylabel('Magnetic Field (uTesla)')
plt.plot(t2, bx2, 'b-', label='bx')
plt.plot(t2, by2, 'r-', label='by')
plt.plot(t2, bz2, 'g-', label='bz')
plt.legend()









plt.show()