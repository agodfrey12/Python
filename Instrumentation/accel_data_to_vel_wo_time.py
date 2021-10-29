import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('accel_data_to_vel.txt', delimiter = ',')
#Grab raw data
dt = 0.01
x = data[:,0]
y = data[:,1]
z = data[:,2]
t = np.arange(0,len(x)*dt,dt)

##Clip Data
tclip = 0.0
xc = x[t>tclip]
yc = y[t>tclip]
zc = z[t>tclip]
tc = t[t>tclip]

##Shift Data
tc-=tc[0]
xc-=xc[0]
yc-=yc[0]
zc-=zc[0]

##Filter x-axis
xcf = 0*xc
s = 0.1
for ctr in range(0,len(xc)-1):
    xcf[ctr+1] = (1-s)*xcf[ctr] + s*xc[ctr]

plt.plot(tc,xc,label='X')
plt.plot(tc,yc,label='Y')
plt.plot(tc,zc,label='Z')
plt.plot(tc,xcf,label='X_Filtered')
plt.grid()
plt.legend()
plt.xlabel('Time (sec)')
plt.ylabel('Acceleration (m/s^2)')


##Get proper acceleration
acceleration = -xcf

###Integrate
velocity = 0*acceleration
deltat = tc[1]-tc[0]
ctr = 0
for ctr in range(0,len(acceleration)-1):
    velocity[ctr+1] = velocity[ctr] + acceleration[ctr]*deltat
    
#Plot
plt.figure()
plt.plot(tc,velocity*2.23694)
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Velocity (mph)')

plt.show()