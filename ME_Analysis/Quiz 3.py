#Aaron Godfrey
#4/6/2021
#Quiz 3

import numpy as np
import matplotlib.pyplot as plt

def run_kut4(F,x,y,h): #run_kut4 code
    K0 = h*F(x,y) 
    K1 = h*F(x+h/2,y+K0/2) 
    K2 = h*F(x+h/2, y+K1/2)
    K3 = h*F(x+h,y+K2)
    return (K0 + 2*K1 + 2*K2 + K3)/6

#integration for RK method
#Input: x(initials), y(initials), xStop(stopping x value), h(step)
def integrate(F,x,y,xStop,h):
    X=[]; Y=[] #integration arrays
    X.append(x)
    Y.append(y)
    while x < xStop:
        h = min(h,xStop-x) #determine step size
        y = y + run_kut4(F,x,y,h) #evaluate next y 
        x = x+h
        X.append(x)
        Y.append(y)
    return np.array(X), np.array(Y)

#solve ode: y'=sin(xy) , y(0)=2.5,3.5,4.5 
y = 4.5 #initial y ---- change this value for each intial condition we were given for a new graph and Y values
h = 0.1 #step size variable ---- note the value here directly effects the values of y(10) at x=10 for questions 2-4
x = 0 #initial x
xStop = 10 #final x
def F4(x,y): 
    F= np.sin(x*y) #y' ode defined
    return F
X,Y=integrate(F4,x,y,xStop,h) #integral of the F4
print('X=',X); print('Y=',Y)

#plotting the function
plt.figure(1)
plt.plot(X,Y,'o') 
plt.xlabel('x')
plt.ylabel('y')

