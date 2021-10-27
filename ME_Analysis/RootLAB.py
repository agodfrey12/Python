#Aaron Godfrey
#ROOT LAB PART 1

import numpy as np
import math 
from math import ceil,log
from numpy import sign
import matplotlib.pyplot as mp

x=np.arange(-4.0,4.4,0.2)

def f1(x): return np.sin(x)
def f2(x): return np.cos(x**2)

def bracket(f,x1,x2,tol=1.e-7):
    f1 = f(x1) 
    f2 = f(x2) 
    x1 = -4.0
    x2=4.4

    if f1 == 0: 
        return x1
    if f2 == 0:
        return x2
    n = int(ceil(log(abs(x1-x2)/tol)/log(2)))
    for i in range(n):
        if sign(f1) == sign(f2):
            print("retunring none as root found")
            return None 
        x3 = (x1+x2)/2 
        f3 = f(x3)
        if f3 == 0:
            return x3 
        if sign(f2) != sign(f3): 
            x1 = x3; f1 = f3
        else: 
            x2 = x3; f2 = f3
    return (x1+x2)/2

y=f1(x)
q=np.stack((x,y),axis=1)

mp.plot(x,y,'r')
mp.title("y=sin(x)")
mp.xlabel("x")
mp.ylabel("y")
mp.grid(True)

x_root=bracket(f1,-4.0,4.4)