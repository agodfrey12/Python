# Delta V to our Moon
import numpy as np
import matplotlib.pyplot as plt

plt.close()

G = 6.67408e-11 #SI unitss
Mearth = 5.97219e24 #kg
Rearth = 6378.1*1000 #m
Alt_earth = 10*1000 #m
Dearth_moon = 384472282 #m
Mmoon = 7.34767309e22 #kg
Rmoon = 1737.4*1000 #m
Alt_moon = 50*1000 #m

mu_earth = G*Mearth
v_cs = np.sqrt((mu_earth)/(Rearth+Alt_earth))
print('Velocity to get to earth Orbit =',v_cs, 'm/s')

### Trans Lunar Insertion Orbit
rp = Rearth + Alt_earth #radius of trans lunar perigee
ra = Dearth_moon + Alt_moon + Rmoon #radius of trans lunar apogee

a = (ra+rp)/2 #semi major axis
print('Semi Major axis a =', a, 'm')

e = (ra-rp)/(ra+rp) #eccentricty
print('Eccentricity e =', e)

p = a*(1-e**2) #parameter
print('Paramater p =', p)

h = np.sqrt(p*mu_earth) #angular momentum
print('Angular Momentum h =', h, 'm^s/s')

vp = h/rp #velocity at perigee of elicptical orbit (earth side)
print('Velocity of the Perigee =', vp, 'm/s')

va = h/ra #velocity at apogee of elliptical orbit (moon side)
print('Velocity at apogee =', va, 'm/s')

v_2 = vp - v_cs #trans lunar insertion
print('Velocity to leave earth Orbit v2=', v_2, 'm/s')

v_moon = np.sqrt((mu_earth)/Dearth_moon)
print('Velocity of the moon =', v_moon, 'm/s')

v_cs_moon = np.sqrt((G*Mmoon)/(Rmoon+Alt_moon))
print('Moon parking orbit v =', v_cs_moon, 'm/s')

#v_3 = v_moon - va #catch up with the moon - 
#print('Catch up with moon v =', v_3, 'm/s')

v_4 = v_cs_moon
print('In moon parking orbit v =', v_4, 'm/s')

v_5 = v_4 #deltaV to land
print('Delta V to land v =', v_5, 'm/s')

v_6 = v_5  #takeoff of moon
print('Takeoff from moon v =', v_6, 'm/s')

v_7 = v_2 #return to earth
print('Return to earth v =', v_7, 'm/s')

deltaV = v_cs + v_2 + v_4 + v_5 + v_6 + v_7 #+ v_3
print('Delta V required to get to the moon and back', deltaV, 'm/s')

''' # below here needs to be updated for this code
########### Plots ###############
v = np.linspace(0, 2*np.pi,1000) #true anomoly

### earth
xp = np.cos(v)*Rearth 
yp = np.sin(v)*Rearth 
xo = np.cos(v)*(Alt_earth + Rearth) 
yo = np.sin(v)*(Alt_earth + Rearth) 

### moon
xm = np.cos(v)*Rmoon + Dearth_moon
ym = np.sin(v)*Rmoon
xom = np.cos(v)*(Alt_moon + Rmoon) + Dearth_moon
yom = np.sin(v)*(Alt_moon + Rmoon)

### Elliptical Orbit
a1 = a #edit for this code
b = p #edit for this code
u = 0.6e7 #edit for this code
q = 0.0 #edit for this code
re = p/(1-e*np.cos(v)) #edit for this code

# Ellipse parametric equations
xe = re*np.cos(v)
ye = re*np.sin(v)


plt.figure()
plt.plot(0,0, 'b*') #plot a circle the same size as the surface of earth
plt.plot(xo,yo, 'r-') #plot the orbit around earth
plt.plot(Dearth_moon,0, 'g*') #plot moon
plt.plot(xom,yom, 'y-') #plot moon orbit
plt.plot(xe,ye, 'b-')
plt.title('Tranfer from earth to moon')
plt.xlabel('Distance in m')
plt.ylabel('Distance in m')

plt.show()
'''