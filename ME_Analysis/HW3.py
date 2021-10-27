#Aaron Godfrey
#3/2/2021
#HW 3

import numpy as np
from math import ceil,log
from numpy import sign
import matplotlib.pyplot as mp

x=np.arange(-5.0,5.5,0.5)

def f1(x): return np.cosh(x)*np.cos(x)-1
def bracket(f,x1,x2,tol=1.e-7):
    f1 = f(x1) 
    f2 = f(x2) 
    x1 = -4.5
    x2 = 5.5
    if f1 == 0: 
        return x1
    if f2 == 0:
        return x2
    n = int(ceil(log(abs(x1-x2)/tol)/log(2)))
    for i in range(n):
        if sign(f1) == sign(f2):
            print("No root found")
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
q=np.stack((x,y),axis=1) #Problem 1

#Problem 2
mp.plot(x,y,'r')
mp.title("y=cosh(x)cos(x)-1")
mp.xlabel("x")
mp.ylabel("y")
mp.grid(True)
#Problem 3 ----> Check problem 2 and 1 agaisnt each other
x_root=bracket(f1,-4.5,5.5)
print(x_root)