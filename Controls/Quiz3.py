# Quiz 3

import numpy as np
import control 
import control.matlab as matlab
import matplotlib.pyplot as plt

plt.close()

# For plant Dc1

G = control.tf([10],[1,11,10])      # Define the plant G = 10/(s+1)(s+10)
Dc1 = 10.0                          # Define Dc1 = 10
S = 1-G*Dc1/(1+G*Dc1)               # Define sensitivity  ### sytemt tf = (Dc*G)/(1+Dc*G)
S = control.minreal(S)              # Remove common factors from S
print('Sensitivity =',S)

zeros = control.zero(S)                     # Find the zeros of the sensitivity
num0s = np.size(np.where(zeros == 0),1)     # Find number of zeros of S at ORIGIN
print('System Type =', num0s)               # System Type

sysInp_den = np.zeros(num0s + 1)
sysInp_den[0] = 1                                   # Find 1/s^k for system input
sysInp = control.tf(1,sysInp_den)                   # TF for 1/s^k
ess = control.evalfr(control.minreal(S*sysInp),0)   # System error
print('ess =', np.round(ess,2))

t = np.arange(0,10,0.01)
r = t**0                        # Create time reference input
y01 = matlab.lsim(1-S,r,t)      # Call lsim

print('####################################')

# For Dc2
G2 = control.tf([10],[1,11,10])       # Define the plant G = 10/(s+1)(s+10)
Dc2 = control.tf([10,10],[1,0])       # Define Dc2 = (10s+10)/s
S2 = 1-G2*Dc2/(1+G2*Dc2)              # Define sensitivity
S2 = control.minreal(S2)              # Remove common factors from S
print('Sensitivity 2 =',S2)

zeros2 = control.zero(S2)                     # Find the zeros of the sensitivity
num0s2 = np.size(np.where(zeros2 == 0),1)     # Find number of zeros of S at ORIGIN
print('System Type =', num0s2)                # System Type

sysInp_den2 = np.zeros(num0s2 + 1)
sysInp_den2[0] = 1                                    # Find 1/s^k for system input
sysInp2 = control.tf(1,sysInp_den2)                   # TF for 1/s^k
ess = control.evalfr(control.minreal(S2*sysInp2),0)   # System error
print('ess =', np.round(ess,2))

t = np.arange(0,10,0.01)
r = t**0*np.heaviside(t,[1])                  # Create time reference input
y02 = matlab.lsim(1-S2,r,t)                   # Call lsim

plt.figure()
plt.title('Quiz 4')
plt.grid()
plt.xlabel('time (s)')
plt.ylabel('y(t)')
plt.plot(t,r)
plt.plot(t,y01[0], label='Dc1')
plt.plot(t,y02[0], label='Dc2')
plt.legend()

plt.show()