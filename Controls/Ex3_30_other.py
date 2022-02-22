#Example 3.30 other

import control
import control.matlab
import numpy as np
import matplotlib.pyplot as plt

plt.close()

#aircraft response sys = -30(s-6)/(s^3 + 4s^2 + 13s)
# expand the bottom to (s(s^2 + 4s +13)) and then (s(s^2 + 4s + 4 + 9)) and then s[(s+2)^2 + 9]
# such that poles are
# s = 0
# s = -2 + j3
# s = -2 - j3

u = -1
legend = []
for i in range (0, -11, -1):
    sys = u*30*control.tf((1,i), (1,4,13,0))
    t = np.arange(0,6,0.01)
    
    y0 = control.impulse_response(sys,t)
    legend.append('zero =' + str(round(i,1)))
    plt.plot(y0[0], y0[1])
    
plt.xlabel('time (s)')
plt.ylabel('altitude (ft)')
plt.grid()
plt.legend(list(legend), loc = 'upper right')

plt.show()