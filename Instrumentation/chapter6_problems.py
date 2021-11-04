## Chapter 6 Problems

import numpy as np
import matplotlib.pyplot as plt
import statistics as st
from scipy import stats

plt.close()

############### Problem 6.1 & 6.5 ###################
data = np.asarray([49.3,50.1,48.9,49.2,49.3,50.5,49.9,49.2,49.8,50.2])

mean = np.mean(data)
median = np.median(data)
stddev = np.std(data)
#mode = st.mode(data)
mode = stats.mode(data)
print('Mean =',mean)
print('Median =',median)
print('Stdev =',stddev)
print('Mode =', mode)
print('Number of Readings = ',len(data))

# Histogram
plt.figure()
plt.hist(data,bins=10)
plt.title('Histogram')
plt.xlabel('Distance (cm)')
plt.ylabel('Count')
plt.grid()
plt.show()

############# Problem 6.79 & 6.80 ####################
T = np.array([20,30,40,50,60,75,100])
V = np.array([1.02,1.53,2.05,2.55,3.07,3.56,4.05])

coeff1 = np.polyfit(V,T,2)
print('Linear Correl Coeff1 =',coeff1)

plt.figure()
plt.plot(V,T,'b*')
plt.title('Temp vs Volts')


Vtrend = np.linspace(V[0],V[-1],100)

###THIS BELOW ONLY WORKS IF YOU ARE FITTING A LINEAR TREND LINE
#Ttrend = coeff1[0]*Vtrend + coeff1[1]
Ttrend = np.polyval(coeff1,Vtrend)

###Residuals
Tatdatapts = np.polyval(coeff1,V)
residuals = (Tatdatapts - T)**2

plt.plot(Vtrend,Ttrend,'r-')
plt.plot(V,Tatdatapts,'r*')

plt.xlabel('V(mV)')
plt.ylabel('T(C)')
plt.grid()

plt.figure()
plt.plot(V,residuals,'b*')
plt.title('Residuals')
plt.grid()

mean1 = np.mean(Tatdatapts)
r2 = 1 - np.sum(residuals)/np.sum((Tatdatapts-mean1)**2)
print('r^2 =',r2)
plt.show()

############## Problem 6.82 ###################
P = np.array([0,5,10,15,20,25,30])
R = np.array([-1.50,4.34,9.52,14.64,19.20,26.60,29.55])

coeff2 = np.polyfit(P,R,2)
print('Linear Correl Coeff2 =',coeff2)

plt.figure()
plt.plot(P,R,'b*')
plt.title('Pound vs Reading')

Rtrend = np.linspace(R[0],R[-1],100)
Ptrend = np.polyval(coeff2,Rtrend)

plt.plot(Rtrend,Ptrend, 'r-')
plt.show()

############### Problem 6.90 ############
x = np.asarray([0.01,0.115,0.29,0.48,0.59,0.81,0.88,1.02,1.12,1.325,1.4])
y = np.asarray([0.07,0.08,0.11,0.135,0.145,0.185,0.19,0.22,0.24,0.285,0.295])

coeff3 = np.polyfit(x,y,2)
print('Linear Correl Coeff3 =', coeff3)

x_fit = np.linspace(np.min(x),np.max(x),100)
y_fit = np.polyval(coeff3,x_fit)
y_fit_at_readings = np.polyval(coeff3,x)

plt.figure()
plt.plot(x,y,'b*',label='Experimental Data')
plt.xlabel('Voltage (V)') 
plt.ylabel('Velocity (ft/s')
plt.grid()
plt.plot(x_fit,y_fit,'r-',label='Fitted Data')
plt.plot(x,y_fit_at_readings,'rs',label='Fitted Data at Readings')
plt.legend()

residuals = y-y_fit_at_readings
print('Residuals = ',np.sum(residuals**2))

res = np.sum(residuals**2)
mean = np.sum((y-np.mean(y))**2)
rsquared = 1-res/mean
print('Correlation Values = ',rsquared)