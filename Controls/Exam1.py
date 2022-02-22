# Exam 1

import control
import control.matlab
import numpy as np
import matplotlib.pyplot as plt

plt.close()

#sys = b/(s^2+as+b)

a = 0.0333
b = 0.0007

t = np.arange(0,400,0.01)

sys = control.tf([b],[1.0,a,b])
y0= control.step_response(sys,t)
x = np.asarray(y0[0])
y = np.asarray(y0[1])

id1 = np.min(np.where(y0[1] > 0.1))
id2 = np.min(np.where(y0[1] > 0.9))

print('id1 =', id1)
print('id2 =', id2)

tr = t[id2] - t[id1]
print('tr =', tr)

ts = control.step_info(sys).get('SettlingTime')
print('ts =', ts)

ans = control.step_info(sys)
print('Loads of info', ans)

plt.figure()
plt.plot(x,y)
plt.grid()
plt.ylabel('y(t)')
plt.xlabel('time (s)')
plt.title('Exam 1 Problem 1')


