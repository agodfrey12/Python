# Delta V to Mun
import numpy as np
import matplotlib.pyplot as plt

plt.close()

G = 6.67408e-11 #SI units
Mkerbin = 5.29e22 #kg
Rkerbin = 600000 #m
Alt_ker = 80*1000 #m
Dker_mun = 12000000 #m
Mmun = 9.75e20 #kg
Rmun = 200000 #m
Alt_mun = 6000 #m

mu_ker = G*Mkerbin
v_cs = np.sqrt((mu_ker)/(Rkerbin+Alt_ker))
print('Velocity to get to Kerbin Orbit =',v_cs, 'm/s')

### Trans Lunar Insertion Orbit
rp = Rkerbin + Alt_ker #radius of trans lunar perigee
ra = Dker_mun + Alt_mun + Rmun #radius of trans lunar apogee

a = (ra+rp)/2 #semi major axis
print('Semi Major axis a =', a, 'm')

e = (ra-rp)/(ra+rp) #eccentricty
print('Eccentricity e =', e)

p = a*(1-e**2) #parameter
print('Paramater p =', p)

h = np.sqrt(p*mu_ker) #angular momentum
print('Angular Momentum h =', h, 'm^s/s')

vp = h/rp #velocity at perigee of elicptical orbit (kerbin side)
print('Velocity of the Perigee =', vp, 'm/s')

va = h/ra #velocity at apogee of elliptical orbit (mun side)
print('Velocity at apogee =', va, 'm/s')

v_2 = vp - v_cs #trans lunar insertion
print('Velocity to leave Kerbin Orbit v2=', v_2, 'm/s')

v_mun = np.sqrt((mu_ker)/Dker_mun)
print('Velocity of the Mun =', v_mun, 'm/s')

v_cs_mun = np.sqrt((G*Mmun)/(Rmun+Alt_mun))
print('Mun parking orbit v =', v_cs_mun, 'm/s')

v_3 = v_mun - va #catch up with the mun - 
print('Catch up with mun v =', v_3, 'm/s')

v_4 = v_cs_mun
print('In Mun parking orbit v =', v_4, 'm/s')

v_5 = v_4 #deltaV to land
print('Delta V to land v =', v_5, 'm/s')

v_6 = v_5  #takeoff of mun
print('Takeoff from Mun v =', v_6, 'm/s')

v_7 = v_2 #return to kerbin
print('Return to Kerbin v =', v_7, 'm/s')

deltaV = 3000 + v_2 + v_3 + v_4 + v_5 + v_6 + v_7
print('Delta V required to get to the mun and back', deltaV, 'm/s')

########### Plots ###############
v = np.linspace(0, 2*np.pi,1000) #true anomoly

### Kerbin
xp = np.cos(v)*Rkerbin 
yp = np.sin(v)*Rkerbin 
xo = np.cos(v)*(Alt_ker + Rkerbin) 
yo = np.sin(v)*(Alt_ker + Rkerbin) 

### Mun
xm = np.cos(v)*Rmun + Dker_mun
ym = np.sin(v)*Rmun
xom = np.cos(v)*(Alt_mun + Rmun) + Dker_mun
yom = np.sin(v)*(Alt_mun + Rmun)

### Elliptical Orbit
a1 = a
b = p
u = 0.6e7
q = 0.0
re = p/(1-e*np.cos(v))

# Ellipse parametric equations
xe = re*np.cos(v)
ye = re*np.sin(v)


plt.figure()
plt.plot(0,0, 'b*') #plot a circle the same size as the surface of kerbin
plt.plot(xo,yo, 'r-') #plot the orbit around kerbin
plt.plot(Dker_mun,0, 'g*') #plot mun
plt.plot(xom,yom, 'y-') #plot mun orbit
plt.plot(xe,ye, 'b-')
plt.title('Tranfer from Kerbin to Mun')
plt.xlabel('Distance in m')
plt.ylabel('Distance in m')

plt.show()