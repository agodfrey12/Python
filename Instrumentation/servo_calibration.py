import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('servo_calibration_data.txt',delimiter=',')

pulse = data[:,0]
angle = data[:,1]

plt.figure()
plt.xlabel('Angle (ms)')
plt.ylabel('Pulse (ms)')
plt.grid()
plt.title('Measured Data w/ Line')
plt.plot(angle, pulse, 'b*')

coeff = np.polyfit(angle, pulse, 1)
print('Coefficients =', coeff)

angle_fit = np.linspace(angle[0], angle[-1], 1000)
pulse_fit = np.polyval(coeff, angle_fit)
plt.plot(angle_fit, pulse_fit, 'r-')

'''
#length_vals = np.polyval(coeff,voltage)

#residuals = length - length_vals

#plt.plot(voltage,length,'b*')
#plt.plot(voltage_fit,length_fit,'r-')
#plt.xlabel('Voltage (V)')
#plt.ylabel('Length (cm)')
#plt.grid()


plt.figure()
plt.plot(residuals,'b*')
plt.grid()
'''

plt.show()