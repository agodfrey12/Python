#console steps for Bracketing
from Bracketing import *
def f2(x): return x**3 -3.23*x**2 - 5.54*x +9.84
bracket(f2,3.5,4.5)

from matplotlib.pyplot import *
import numpy as np
xr = np.arange(-5,5,0.1) # define x range
yr = f2(xr) #define y range
plot(xr,yr,'r')
grid(True)
xlabel('x')
ylabel('y')
title('PLot of polynomial')

