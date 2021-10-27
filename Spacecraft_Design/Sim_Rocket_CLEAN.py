import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("C:/Users/Aaron Godfrey/Desktop/School/Senior Year/Fall 2021/Spacecraft Design/Sim_Rocket_CLEAN.csv",delimiter=',')

time = data[:,0]
altitude = data[:,1]

plt.plot(time,altitude)
plt.xlabel('Time (s)')
plt.ylabel('Altitude (ft)')
plt.title('Open Rocket Simulation Altitude vs Time')
plt.grid()
plt.show()
