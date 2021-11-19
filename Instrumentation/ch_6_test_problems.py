import numpy as np
import matplotlib.pyplot as plt

plt.close() 

################### grad student problem ###########################
data = np.loadtxt('Load_Cell_Calibration.csv', delimiter = ',', skiprows = 3)

#raw data and plot
voltage = data[:,0]
mass = data[:,1]

plt.figure()
plt.plot(voltage, mass, 'bs', label='Raw Data')

#trendline and plot
coeff = np.polyfit(voltage, mass, 1)
print('Coeff =', coeff)
m = coeff[0]
b = coeff[1]

vtrend = np.linspace(voltage[0], voltage[-1], 1000)
mtrend = np.polyval(coeff, vtrend)
mfit = np.polyval(coeff, voltage)

plt.plot(vtrend, mtrend, 'r-', label='Trendline')
plt.plot(voltage, mfit, 'gd', label='Fitted @ Trendline')
plt.legend()
plt.grid()

#Equation of trendline Mass = 10.38461227 * Voltage - 6.49985826
Voltage = 45 #mV
Mass = m * Voltage + b
print('Estimated mass =', Mass)

plt.title('Mass = 10.38461227 * Voltage - 6.49985826')
plt.xlabel('Voltage (mV)')
plt.ylabel('Mass (g)')

#compute residuals and plot
residuals = mass - mfit
print('Residuals = ',np.sum(residuals**2))
plt.figure()
plt.title('Residuals')
plt.plot(mass, residuals, 'k*')
plt.grid()

#compute r^2
res = np.sum(residuals**2)
mean = np.sum((mass-np.mean(mass))**2)
rsqrd = 1 - res/mean
print('Correlation Values =',rsqrd)
print('')

##################### undergrad problem ##################################
dossier = np.loadtxt('Experiment 8.csv', delimiter=',', skiprows=1)

magx = dossier[:,0]
magy = dossier[:,1]
magz = dossier[:,2]

dev_x = np.std(magx)
mean_x = np.mean(magx)
dev_y = np.std(magy)
mean_y = np.mean(magy)
dev_z = np.std(magz)
mean_z = np.mean(magz)

z = 0.95 #confidence level
n = int(len(dossier)) #sample size
CI_x1 = mean_x + (z * (dev_x/np.sqrt(n)))
CI_x2 = mean_x - (z * (dev_x/np.sqrt(n)))
CI_y1 = mean_y + (z * (dev_y/np.sqrt(n)))
CI_y2 = mean_y - (z * (dev_y/np.sqrt(n)))                  
CI_z1 = mean_z + (z * (dev_z/np.sqrt(n)))
CI_z2 = mean_z - (z * (dev_z/np.sqrt(n)))
                      
print('Mean of magx =', mean_x)
print('Standard Deviation of magx =', dev_x)
print('Mean of magy =', mean_y)
print('Standard Deviation of magy =', dev_y)
print('Mean of magz =', mean_z)
print('Standard Deviation of magz =', dev_z)
print('Confidence interval in the X = [',CI_x1, CI_x2,']')
print('Confidence interval in the Y = [',CI_y1, CI_y2,']')
print('Confidence interval in the Z = [',CI_z1, CI_z2,']')

bins = 1 + 3.322 * np.log(len(magx))

plt.figure()
plt.hist(magx, bins=int(bins))
plt.grid()
plt.title('Mag X')
plt.xlabel('Number of Occurences')
plt.ylabel('Magetic Field (uT)')

plt.figure()
plt.hist(magy, bins=int(bins))
plt.grid()
plt.title('Mag Y')
plt.xlabel('Number of Occurences')
plt.ylabel('Magetic Field (uT)')

plt.figure()
plt.hist(magz, bins=int(bins))
plt.grid()
plt.title('Mag Z')
plt.xlabel('Number of Occurences')
plt.ylabel('Magetic Field (uT)')

plt.show()