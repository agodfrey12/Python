import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('accel_data_to_vel1.txt', delimiter = ',')
#Grab raw data
t = data[:,0]
x = data[:,1]
y = data[:,2]
z = data[:,3]

##Clip Data
xc = x[t>0.1]
yc = y[t>0.1]
zc = z[t>0.1]
tc = t[t>0.1]

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
plt.title('Acceleration (m/s^2)')

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
plt.title('Velocity (mph)')

##integrate again
position = 0*velocity
for ctr in range(0,len(velocity)-1):
    position[ctr+1] = position[ctr] + velocity[ctr]*deltat
    
plt.figure()
plt.plot(tc,position*3.28)
plt.title('Position (ft)')
plt.xlabel('Time (sec)')
plt.ylabel('Position (ft)')
plt.grid()

plt.show()