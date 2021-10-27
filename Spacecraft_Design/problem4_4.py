import numpy as np

mmars = 6.39e23
rmars = 3396200
G = 6.67e-11

mu = G*mmars

v = np.sqrt(mu/(500000+rmars))
print('Velocity =',v, 'm/s')

deltaV = 2*v*np.sin(np.pi/36)
print('Delta V =',deltaV, 'm/s')