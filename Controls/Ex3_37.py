# Example 3.37

import matplotlib.pyplot as plt
import  control
import numpy as np

plt.close()

A = [1,2,4,8,100]
z = 0.707  #damping coeff
t = np.arange(0,10,0.01) # time range for output
leg = []

for ai in A:
    denp = [1/ai/z, 1]; # extra pole
    den = [1, 2*z, 1] #denominator
    sysH = control.tf((1),(np.convolve(denp,den)))
    y0= control.step_response(sysH,t) #model step-response
    x = np.asarray(y0[0])
    y = np.asarray(y0[1])
    plt.plot(x,y)
    leg.append("alpha="+str(np.round(ai,1)))
    
plt.legend(list(leg) )
plt.title('Step-response')
plt.ylabel('y(t)')
plt.xlabel('time (s)')
plt.grid()
plt.ylim(-2, 2)

plt.show()