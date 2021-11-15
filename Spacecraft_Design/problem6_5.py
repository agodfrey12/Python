import numpy as np
import matplotlib.pyplot as plt

he = 120000.0 # entry altitude in m
ha = np.linspace(0,he,100000) # vectorize
R = 6378000 # eadius of Earth in m
Ve = 7500.0 # m/s
beta = 0.1354/1000.0 # density constant in m^-1
rhos = 1.225 # kg/m^3
m = 2200.0 # kg
CD = 1.5 
S = 4.1 # m^2 
gammae = -2.0*np.pi/180.0 # entry angle
Va = Ve*np.exp((1.0/(2*beta))*(rhos/(np.sin(gammae)))*(S*CD/m)*np.exp(-beta*ha)) #eq 6.15

#Acceleration
drdt = Va*np.sin(gammae) # from figure 6.1
dhdt = drdt
dVdh = (Va[0:-2]-Va[1:-1])/(ha[0:-2]-ha[1:-1])
accela = -dVdh*dhdt[0:-2]
amax = -(beta*Ve**2)/(2*np.exp(1))*np.sin(gammae) #eq 6.16
print('Max acceleration = ',amax, 'm/s^2')
print('Max G = ',amax/9.81)

hmax = (1/beta)*np.log((-1/beta)*(S*CD/m)*(rhos/np.sin(gammae))) # eq 6.17
print('Max acceleration at', hmax, 'meters')

plt.figure()
plt.plot(ha[0:-2],accela)
plt.plot(hmax,amax,'r*',markersize=12)
plt.xlabel('Altitude (m)')
plt.ylabel('Acceleration (m/s^2)')
plt.grid()

plt.show()