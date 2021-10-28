import numpy as np


Vi = np.linspace(0,20.0,1000) 
Vistar = 10.0
rho_inf = 1.1 

dP = 0.5*rho_inf*Vi**2
dPstar = 0.5*rho_inf*Vistar**2
print('Pressure Drop (Pa) = ',dPstar)

