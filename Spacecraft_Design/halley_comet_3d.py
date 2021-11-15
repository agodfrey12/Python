import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

##Sun Parameters
G = 6.6742*10**-11; #Gravitational constant
Msun = 1.989*10**30 #mass of sun
musun = G*Msun
Rsun = 696347055.0 #meters

##True Anamoly
nu = np.linspace(0,2*np.pi,1000)

##Semi Major Axis
a = 17.94*1.496e11

##Eccentricity
e = 0.967

##inclination
i = 162.2*np.pi/180.0

##Longitude of the Ascending Node
W = 57.987*np.pi/180.0

#Argument of the periaps
w = 110.9135*np.pi/180.0

##plot in the orbital plane
###Phat and Qhat
p = a*(1-e**2)
r = p/(1+e*np.cos(nu))
xp = r*np.cos(nu)
yq = r*np.sin(nu)

plt.plot(xp,yq,'r-')
plt.plot(xp[0],yq[0],'r*',markersize=15)
theta = np.linspace(0,2*np.pi,1000)
xsun = Rsun*np.cos(theta)
ysun = Rsun*np.sin(theta)
plt.plot(xsun,ysun,'b-')
plt.axis('equal')
plt.title('Orbital Plane')
plt.xlabel('X-axis (m)')
plt.ylabel('Y-axis (m)')

###Rotate to Sun Centered Inertial Frame (KCI)
zr = 0*xp

TPI = np.asarray([[np.cos(W)*np.cos(w)-np.sin(W)*np.sin(w)*np.cos(i),-np.cos(W)*np.sin(w)-np.sin(W)*np.cos(w)*np.cos(i),np.sin(W)*np.sin(i)],
                 [np.sin(W)*np.cos(w)+np.cos(W)*np.sin(w)*np.cos(i),-np.sin(W)*np.sin(w)+np.cos(W)*np.cos(w)*np.cos(i),-np.cos(W)*np.sin(i)],
                 [np.sin(w)*np.sin(i),np.cos(w)*np.sin(i),np.cos(i)]])

xi = 0*xp
yj = 0*yq
zk = 0*zr
for x in range(0,len(xp)):
  xyzO = np.asarray([xp[x],yq[x],zr[x]]) ##3x1 vector
  xyzi = np.matmul((TPI),xyzO)
  xi[x] = xyzi[0]
  yj[x] = xyzi[1]
  zk[x] = xyzi[2]
  
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title('3d Orbit of Halley Comet')
ax.set_xlabel('X-axis (m)')
ax.set_ylabel('Y-axis (m)')
ax.set_zlabel('Z-axis (m)')
ax.plot(xi,yj,zk,'r-')
ax.scatter(xi[0],yj[0],zk[0],'r*',s=20)
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
xsph = np.cos(u)*np.sin(v)
ysph = np.sin(u)*np.sin(v)
zsph = np.cos(v)
ax.plot_wireframe(Rsun*xsph,Rsun*ysph,Rsun*zsph,color='blue')

plt.show()