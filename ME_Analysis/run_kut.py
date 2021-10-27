#2nd order RK polys
#Input: x(initials), y(initials), h, y'=f(x)
import numpy as np
import matplotlib.pyplot as mp

def run_kut2(F,x,y,h):
    K0 = h*F(x,y) #1st order term
    K1 = h*(F(x+h/2,y+K0/2)) #2nd order
    return K1

#integration for RK method
#Input: x(initials), y(initials), xStop(stopping x value), h(step)
def integrate(F,x,y,xStop,h):
    X=[]; Y=[] #integration arrays
    X.append(x)
    Y.append(y)
    while x < xStop:
        h = min(h,xStop-x) #determine step size
        y = y + run_kut2(F,x,y,h) #evaluate next y 
        x = x+h
        X.append(x)
        Y.append(y)
    return np.array(X), np.array(Y)

#Console side ---- solve y'=siny, y(0)-1, h =0.1, xStop = 0.5
y = 1
h = 0.1
x = 1e-6
xStop = 0.5
def F2(x,y): return np.sin(y) #define derivative function
X,Y = integrate(F2,x,y,xStop,h)
print('X=',X); print('Y=',Y)

mp.figure(1)
mp.plot(X,Y,'o-')

X2 = np.log(1/np.sin(Y)-1/np.tan(Y))+0.604
mp.plot(X2,Y,'g-')
