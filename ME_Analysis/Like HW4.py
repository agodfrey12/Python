import numpy as np
import math

def pf(x): return ((1-x**2))**1.5
def qf(x): return np.sqrt(x)*np.cos(x)

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


I = gaussQuad(qf,0,np.pi,5)
print('I=', I)

#Problem 2
import matplotlib.pyplot as mp
def erf(x): return np.exp(-x**2)*np.sqrt(4/np.pi)
X = []; Y=[]
for x in np.arange(-5,5,.01):
    X.append(x)
    I=gaussQuad(erf,0,x,5)
    Y.append(I)
X=np.array(X); Y=np.array(Y) #end of block
mp.plot(X,Y,'m') #plot the function in magenta
mp.plot(X,erf(X),'g') 
mp.grid(True)
mp.title('erf(x)')
mp.legend(['erf(x)','e^(-t^2)*/sqrt(pi)'])
'''
#Problem 3-4
import matplotlib.pyplot as mp
def erfA(x): return np.exp(-x**2)*2/np.sqrt(np.pi)
X = []; Y=[]
for x in np.arange(-2,2,.01):
    X.append(x)
    I=gaussQuad(erfA,-2,x,2)
    Y.append(I)
X=np.array(X); Y=np.array(Y) #end of block
mp.plot(X,Y,'m')
mp.plot(X,erfA(X),'g')
mp.grid(True)
mp.title('erfA(x)')
mp.legend(['erfA(x)','e^(-t^2)*2/sqrt(pi)'])
'''
