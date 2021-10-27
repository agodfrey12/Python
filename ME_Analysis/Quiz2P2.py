#Gauss Quad

import numpy as np
import math

#returns the polynomials and its derivatives
def legendre(t,m): #input the initial point and the number of points
    p0 = 1.0; p1 = t
    for k in range(1,m): #loop over the number of points 
        p = ((2.0*k + 1.0)*t*p1 - k*p0)/(1.0 + k ) #evaluate the ploy
        p0 = p1; p1 = p #update recursively
    dp = m*(p0 - t*p1)/(1.0 - t**2)  #calculate the poly derivatives
    return p,dp 

#function to obtain the quad points and weights
def gaussNodes(m):
    A = np.zeros(m) #weight wi
    x = np.zeros(m) #points xi
    tol = 1.e-6
    nroots = int((m+1)/2) #evaluate only the positive roots
    for i in range(nroots):
        t = math.cos(math.pi*(i+0.75)/(m+0.5)) #appoximate point
        for j in range(30):
            p,dp = legendre(t,m)
            dt = -p/dp #improvement on the Newt. Raph
            t = t+dt
            x[i] = -t; x[m-i-1] = t; #define both neg and pos roots
            A[i] = 2/(1-t**2)/dp**2 #weight for both pos and neg points
            A[m-i-1] = A[i]
            if abs(dt) < tol:
                break
    return x,A 

#function to evaluate any continuous function
def gaussQuad(f,a,b,m):
    c1 = (b+a)/2 #scaling actual limits
    c2 = (b-a)/2
    x,A = gaussNodes(m) #get all gauss points and weights
    Isum = 0 #integrate over all panels
    for i in range(len(x)):
        Isum = Isum + A[i]*(f(c1+c2*x[i]))
    I = c2*Isum
    return I

def pf(x): return np.sin(x**2) #given function
I = gaussQuad(pf,0,1,7) #evaluating the integral
print('I=',I)

#find the integral of the function 
#between 0<x<1.77
#plot the function and integral
import matplotlib.pyplot as plt
xp=np.arange(0,1.80,0.01) #defining the range of x values for the plot
yp=pf(xp)
plt.plot(xp,yp,'r') #ploting the function
plt.grid(True)
IY=[] #integral array
for i in xp:
    I = gaussQuad(pf,0,i,7)
    IY.append(I)
len(xp)
len(IY)
IY=np.array(IY)
plt.plot(xp,IY,'g') #ploting the integral
plt.title('sin(x^2) and its integral')
plt.legend(['function','integral'])
plt.plot(0,0,'b*') #showing roots
plt.plot(1.7725,0,'b*') #showing roots
plt.xlabel('x')
plt.ylabel('y')
