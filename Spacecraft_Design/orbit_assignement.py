import numpy as np
import matplotlib.pyplot as plt

plt.close()

Rkerbin = 600000 #radius of kerbin
ro = Rkerbin + 80*1000.0 #radius of orbit
v = np.linspace(0, 2*np.pi,1000) #true anomoly

xp = np.cos(v)*Rkerbin
yp = np.sin(v)*Rkerbin
xo = np.cos(v)*ro
yo = np.sin(v)*ro

plt.figure()
plt.title("Kerbin 80 km Orbit")
plt.plot(xp,yp, '-b') #plot a circle the same size as the surface of kerbin
plt.plot(xo,yo, 'r-') #plot the orbit around kerbin
plt.show()

rcs = ro
G = 6.67408e-11 #grav constant
Mkerbin = 5.29e22 #mass of kerbin
mu = G*Mkerbin
VCS = np.sqrt(mu/rcs)
print('VCS kerbin = ', VCS)

############## Mun below here ##############

Rmun = 200000
rm = Rmun + 6*1000
vm = np.linspace(0, 2*np.pi, 1000)

xm = np.cos(vm)*Rmun
ym = np.sin(vm)*Rmun
xo = np.cos(vm)*rm
yo = np.sin(vm)*rm

plt.figure()
plt.title("Mun 6km Orbit")
plt.plot(xm,ym, 'g-')
plt.plot(xo,yo, 'r-')
plt.show()


rcs = rm
G = 6.67408e-11
Mmun = 9.76e20
mu = G*Mmun
VCS = np.sqrt(mu/rcs)
print('VCS mun = ', VCS)