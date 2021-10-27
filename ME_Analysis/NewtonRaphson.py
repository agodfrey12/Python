#NewtonRaphson Method

import numpy as np
import matplotlib.pyplot as plt

def fn(x): return x**4 - 6.4*x**3 + 6.45*x**2 + 20.538*x - 31.752
def dfn(x): return 4*x**3 - 19.2*x**2 + 12.9*x + 20.538

def NewtonRaphson(f, df, x, tol = 1e-7):
    for i in range(50): #use a short loop
        fx = f(x)
        if fx == 0 :
            return x #found root
        try: #use try exception to prevent division by 0
            dfx = df(x) #dereivative of fn
            dx = -fx/dfx #increment in x
        except ZeroDivisionError:
            print("division by 0"); return None
        x = x + dx #new x
        if abs(dx) < tol: #reached convergence
            return x
    return None

xr = np.arange(-2,5.1,0.1)
yr = fn(xr)
dyr = dfn(xr) #calculate the derivatives for the plot

plt.plot(xr,yr,'r')
plt.grid(True)
#trying roots se get from graph
root = NewtonRaphson(fn, dfn, 2.2)
print(root)

plt.plot(xr,dyr,'b')
plt.xlabel("x")
plt.ylabel("y")
plt.legend(['fn','derivative'])