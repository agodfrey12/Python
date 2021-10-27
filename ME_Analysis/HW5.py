#Aaron Godfrey
#3/23/2021
#HW5

import numpy as np
import matplotlib.pyplot as plt

def run_kut4(F,x,y,h):
    K0 = h*F(x,y) #1st order term
    K1 = h*(F(x+h/2,y+K0/2)) #2nd order
    K2 = h*F(x+h/2, y+K1/2) #3rd term
    K3 = h*F(x+h,y+K2) #4th term
    return (K0 + 2*K1 + 2*K2 + K3)/6

#integration for RK method
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

def F(x,y):
    g=9.81 #gravity
    c=0.203 #drag
    m=80 #mass
    F = np.zeros(2)
    F[0]=y[1] 
    F[1]=g-c/m*y[1]**2 #given function
    return F

x = 0.0 #integration start
xS = 20.0 #integration stop
y = np.array([0.0,0.0])
h = 0.1 #step size
f = 1 #frequency
X,Y = integrate(F,x,y,xS,h)
#print('X=',X); print('Y=',Y)
Q=np.stack((X,Y[:,0],Y[:,1]))
print(Q)

plt.figure(1) #plot of the function and integral
plt.plot(X,Y[:,0],'b') #displacement
plt.plot(X,Y[:,1],'g') #velocity
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Flight Path')
plt.legend(['Displacement','Velocity'])