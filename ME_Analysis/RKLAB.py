#RK LAB

import numpy as np

def RK2(F,x,y,h):
    K0 = h*F(x,y)
    K1 = h*F(x+h/2,y+K0/2)
    return K1

def integrate(F,x,y,xs,h):
    X=[]; Y=[] 
    X.append(x)
    Y.append(y)
    while x < xs:
        h = min(h,xs-x) 
        y = y + RK2(F,x,y,h) 
        print('y=',y)
        x = x+h
        X.append(x)
        Y.append(y)
    return np.array(X), np.array(Y)

xs = 0.5
x = 0.0
h = 0.1
y = 1
def F(x,y): return np.sin(y)

Q = integrate(F,x,y,xs,h)
print(Q)