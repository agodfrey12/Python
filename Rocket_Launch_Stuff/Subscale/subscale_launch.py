import numpy as np
import matplotlib.pyplot as plt

plt.close()

data = np.loadtxt('launch_data.txt')

t = data[:,0]
ax = data[:,1]
ay = data[:,2]
az = data[:,3]
bx = data[:,4]
by = data[:,5]
bz = data[:,6]

plt.figure()
plt.plot(t,ax, 'b*')

plt.figure()
plt.plot(t,ay, 'r*')

plt.figure()
plt.plot(t,az, 'g*')

plt.figure()
plt.plot(t,bx, 'k*')

plt.figure()
plt.plot(t,by, 'y*')

plt.figure()
plt.plot(t,bz, 'c*')

plt.show()