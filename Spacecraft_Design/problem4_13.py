import numpy as np

mu_earth = 398600 #km^3/s^2
ro = 185 #km
rearth = 6378.1 #km
rearth_mun = 384400 #km
rap = rearth_mun + ro
rper = ro + rearth 

Vcs = np.sqrt(mu_earth/(rearth+ro))
print('Velocity of the Sat wrt Earth =',Vcs, 'km/s')

e = (rap-rper)/(rap+rper)
print('Eccentricty =', e)

a = (rap+rper)/2
print('Semi Major axis =', a, 'km')

P = a*(1-e**2)
print('Parameter =',P, 'km')

h = np.sqrt(P*mu_earth)
print('Angular momentum =', h, 'km^2/s')

Vper = h/rper
print('Velocity at perigee =', Vper, 'km/s')

delV = Vper - Vcs
print('Delta V to get the Moon from Earth Orbit =',delV, 'km/s')