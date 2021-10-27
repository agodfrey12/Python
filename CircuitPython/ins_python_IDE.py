#Aaron Godfrey
#Instrumentation
#Python IDE
#8/24/2021

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,100)
y = 60*(1-np.exp(-5*(x)))+30 #given T(t)=60(1-e^(-5t))+30

plt.plot(x,y)
plt.xlabel("Time (s)")
plt.ylabel("Temperature (F)")
plt.grid(True)
plt.title("Temperature vs Time")
plt.savefig('python_ide.png')