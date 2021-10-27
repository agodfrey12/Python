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

def pf(x): return ((1-x**2))**1.5
I = gaussQuad(pf,-1,1,7)
print('I=',I)


'''
In class shenanigans on 2/9/21
#find the integral of the function (1-x**2)**1.5
#between -1<x<1
#plot the function and integral
#use 7 GQ points
import matplotlib.pyplot as plt
def polyf(x): return (1-x**2)**1.5
xp=np.arange(-1,1.0,0.1)
yp=polyf(xp)
plt.plot(xp,yp,'r')
plt.grid(True)
IY=[] #integral array
for i in xp:
    I = gaussQuad(polyf,-1,1,7)
    IY.append(I)
len(xp)
len(IY)
IY=np.array[IY]
plt.plot(xp,IY,'g')
plt.title('integral of ...')
plt.legend(['function','integral'])


def pf2(x): return(1/3)/(1+x**(4/3))
# integrate range 0<x<1
I = gaussQuad(pf2,0,1,7)
print(I)

'''