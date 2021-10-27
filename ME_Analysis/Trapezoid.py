#Recursive Trapezoid Rule

import numpy as np
def trapezoid(f,a,b,Iold,k): #define recursive variables
    if k == 0: #no panels
        return 0;
    elif k == 1: #1 panel integral
        Inew = (f(a)+f(b))*(b-a)/2 #basic 1 panel trapezoid
    else: #k>1 and multiple panels
        n_new = 2**(k-2) #new points
        h = (b-a)/n_new #new spacing
        x = a = h/2 #starting point
        Isum = 0
        for i in range(n_new):
            Isum = Isum + f(x) #adding the newest point
            x = x + h  #next point
        Inew = Iold/2 + Isum*h/2
    return Inew

#lets integrate sin(x) between 0 and pi

def fT(x): return np.sin(x)
Iold = 0 
for k in range(1,21): #range over 20 interations for convergence
    Inew = trapezoid(fT,0,np.pi,Iold,k)
    if (k>1) and abs(Inew-Iold) < 1.e-6: break #error check w/ tolerance
    Iold = Inew
print(Inew) #print new integral
n = 2**(k-1) #actual number of panels used to find integral value
print ('number of panels',n)        
