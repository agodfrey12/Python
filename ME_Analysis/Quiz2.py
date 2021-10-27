#Aaron Godfrey
#Quiz 2
#3/11/2021

#Problems 1-3

import numpy as np
import matplotlib.pyplot as plt

def fn(x): return np.sin(x**2) #function given
def dfn(x): return 2*x*np.cos(x**2) #derivative of that function

def NewtonRaphson(f, df, x, tol = 1e-7): #define newtonRaph and give it a tolerance
    for i in range(50): #short loop
        fx = f(x)
        if fx == 0 :
            return x #if x=0 then we have root
        try: #use try exception to prevent division by 0
            dfx = df(x) #dereivative of fn
            dx = -fx/dfx #increment in x
        except ZeroDivisionError:
            print("division by 0"); return None
        x = x + dx #new x
        if abs(dx) < tol: #reached convergence
            return x
    return None

root = NewtonRaphson(fn, dfn, 0.1) #finding roots from the given values
print("root=",root)

xr = np.arange(0,1.78,0.1)
yr = fn(xr)
dyr = dfn(xr) #calculate the derivatives for the plot

plt.plot(xr,yr,'r')
plt.grid(True)

'''
plt.plot(xr,dyr,'b')
plt.xlabel("x")
plt.ylabel("y")
plt.legend(['fn','derivative'])
'''