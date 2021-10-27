import numpy as np


G = 6.67e-11
ro = 6600 #km
mu_earth = 398600 #km^3/s^2
AU = 1.496e8 #km
mu_sun = 1.327e11 #km^3/s^2
rper = 6600 + AU #km
rap = 9.539*AU #km


Vcs = np.sqrt(mu_earth/ro)
print('Velocity Sat about Earth =',Vcs, 'km/s')

Ve = np.sqrt(mu_sun/AU)
print('Velocity Earth about Sun =',Ve, 'km/s')

Vt = Ve + Vcs
print('Velocity of Sat about Sun', Vt, 'km/s')

e = (rap-rper)/(rap+rper)
print('Eccentricty =', e)

a = (rap+rper)/2
print('Semi Major axis =', a, 'km')

P = a*(1-e**2)
print('Parameter =',P, 'km')

h = np.sqrt(P*mu_sun)
print('Angular Momentum =', h, 'km^2/s')

Vper = h/rper
print('Velocity at perigee =', Vper, 'km/s')

delV = Vper - Vt
print('Delta V for Sat to leave Earth and flyby Saturn =',delV*1000,'m')

Vap = h/rap
print('Velocity at Apogee =',Vap,'km/s')

Vsaturn = np.sqrt(mu_sun/rap)
print('Velocity of Saturn',Vsaturn, 'km/s')