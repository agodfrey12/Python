import numpy as np
import matplotlib.pyplot as plt

xL = np.linspace(1e-10,1,100)
R2 = xL*1000.0
R1 = 1000-R2
RL = 5000.0
Rp = (1/R2 + 1/RL)**(-1)

Vs = 90.0
i = Vs/(R1+Rp)
Vo = i*Rp

plt.figure()
plt.plot(xL,Vo)
plt.grid()
plt.xlabel('x/L')
plt.ylabel('Voltage')
plt.title('Voltage vs x/L')