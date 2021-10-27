import numpy as np
import matplotlib.pyplot as plt

plt.close()

Ve = 11.2 
beta = 0.1354 
LD = 0.3
S = 12.0
m = 5600.0

gammae = np.linspace(-15,-0.01,1000)*np.pi/180.0
Vexit = Ve*np.exp(2*gammae/LD)

plt.figure()
plt.plot(gammae*180.0/np.pi,Vexit)
plt.title('Velocity vs Flight Path Angle')
plt.xlabel('Flight Path Angle (deg)')
plt.ylabel('Exit Velocity (km/s)')
plt.grid()

apullup = np.sqrt(1+1/(LD**2))*(1-np.cos(gammae))*beta*Ve**2*np.exp(2*gammae/LD)*1000.0/9.81

plt.figure()
plt.plot(gammae*180.0/np.pi,apullup)
plt.title('Acceleration vs Flight Path Angle')
plt.xlabel('Flight Path Angle (deg)')
plt.ylabel('Max Acceleration Load (g)')
plt.grid()

plt.show()