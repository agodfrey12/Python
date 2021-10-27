#Bracketing Function
#root = bracket(f,x1,x2,tol=1.e-7)

from numpy import sign
from math import ceil,log
def f1(x): return x**3 - 10*x**2 +5
def f2(x): return x**3 -3.23*x**2 - 5.54*x +9.84

def bracket(f,x1,x2,tol=1.e-7):
    f1 = f(x1) #evaluating f(x1)
    f2 = f(x2) #evaluating f(x2)
    if f1 == 0: 
        return x1
    if f2 == 0:
        return x2
    #evaluation the number of iterations 2*k = lo/tol
    n = int(ceil(log(abs(x1-x2)/tol)/log(2)))
    for i in range(n):
        if sign(f1) == sign(f2):
            return None #We are not in the range of root 
        x3 = (x1+x2)/2 #Estimate a new x
        #Evaluate the function at x3
        f3 = f(x3)
        if f3 == 0:
            return x3 #found the root
        #condition if f2 and f3 are opposite signs - root lies inbetween them
        if sign(f2) != sign(f3): #root between x2 and x3
            x1 = x3; f1 = f3
        else: 
            x2 = x3; f2 = f3
    return (x1+x2)/2
