# Exam 1 Practice

import numpy as np
import control
import control.matlab
import matplotlib.pyplot as plt

plt.close()

'''
#Number one part B
t = np.arange(0,150,0.01)
Mp = 100
K = 0.1

while Mp > 20:
    K = K - 0.005
    sys = control.tf([0.2*K],[1.0,0.104,0.2*K])
    y0 = control.step_response(sys,t)
    ymax = np.max(y0[1])    #max peak
    Mp = (ymax-1)*100        #new Mp estimate

print('K =',K)
print('Mp =',Mp)

plt.figure()
plt.plot(t,y0[1])
plt.grid()
plt.ylabel('y(t)')
plt.xlabel('time (s)')
plt.title('Number 1 Part B')
'''

#Number 2 part B
z = 0.5
wn = 1
t = np.arange(0,15,0.01)
p = 20

denp = [1,20] #extra pole
den = [1, 2*z*wn, wn**2]
sys = control.tf([20],(np.convolve(denp,den)))
y0 = control.step_response(sys, t)

id1 = np.min(np.where(y0[1] > 0.1))
id2 = np.min(np.where(y0[1] > 0.9)) #index at Mp - 0.1 and 0.9

print('id1 =', id1)
print('id2 =', id2)

tr = t[id2] - t[id1]
print('tr =', tr)

ts = -1/wn/z*np.log(0.01/p*np.sqrt((1-z**2)*(p**2-2*p*1+1)))
ts2 = control.step_info(sys).get('SettlingTime')
print('ts =', ts)
print('ts2 =', ts2)

plt.figure()
plt.plot(y0[0],y0[1])
plt.grid()
plt.xlabel('y(t)')
plt.ylabel('time (s)')
plt.title('Number 2 Part B')





plt.show()