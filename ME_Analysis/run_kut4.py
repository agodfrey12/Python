#4th order RK polys
#Input: x(initials), y(initials), h, y'=f(x)
import numpy as np
import matplotlib.pyplot as mp

def run_kut4(F,x,y,h):
    K0 = h*F(x,y) #1st order term
    K1 = h*(F(x+h/2,y+K0/2)) #2nd order
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

#solve ode: y'' = -0.1y'-x , y(0)=0, y'(0)=1, Xstop=2
y = [0,1]
h = 0.2
x = 0
xStop = 2
def F4(x,y): 
    F = np.zeros(2)
    F[0]=y[1]
    F[1]=-0.1*y[1]-x #y''
    return F
X,Y=integrate(F4,0,[0,1],xStop,h)
print('X=',X); print('Y=',Y)
yEX = 100*X-5*X**2+990*(np.exp(-0.1*X)-1) #exact solution
print('yEX=',yEX)

mp.figure(2)
mp.plot(X,Y[:,0],'o') #from Y take its 1st column
mp.plot(X,yEX,'r')
mp.xlabel('x')
mp.ylabel('y')
mp.legend(['Numerical', 'Exact'])