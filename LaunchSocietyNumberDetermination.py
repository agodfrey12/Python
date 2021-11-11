import numpy as np
import matplotlib.pyplot as plt

nsims = 20 #number of independently random simulated rocket launches
nsensors = 15 #number of accelerometers used in the payload (maximum 30)
s = 0.1 #measurements are made once every ___ seconds
f = 10**4 #scale factor to scale the maximum height to a realistic number (~1.5 - 2km)
k = 0.00002 #drag constants

sigmax = 1.5*9.81*(22*10**-6)*np.sqrt(1/s) #bias information found on the LIS3DH datasheet
sigmay = 1.5*9.81*(22*10**-6)*np.sqrt(1/s)
sigmaz = 1.5*9.81*(22*10**-6)*np.sqrt(1/s)

######################################################################

data = np.loadtxt('..\MATLAB\TrueAccelerometerData.csv',delimiter=',') #true accelerations experienced by rocket
axtrue = data[:,0]
aytrue = data[:,1]
aztrue = data[:,2]
