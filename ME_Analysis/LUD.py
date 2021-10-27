#solving for LE decomp
#followed by [A]{x}={b}
#LU - LUDecomp(A,b)
#x = LUSolve(LU)
#A=[[3,0,-3],[2,1,3],[1,3,0]]
#b=[15,-8,7]
import numpy as np

#Gauss Elimination augmentation function
def LUDecomp(amat):
    a = np.array(amat,float) #declare A as numpy array
    n = len(a)
    #Elimination phase
    for k in range(0,n-1): #loop for pivot row
        for i in range(k+1,n): #rows being reduced
            if a[k,k] !=0: #to stop division of 0
                lam = a[i,k]/a[k,k]; #lamda multiplier
                #reduce current tow in augmented matrix
                a[i,k:n] = a[i,k:n] - lam*a[k,k:n] #for upper matrix
                a[i,k] = lam #for lower
    return a

#Solving with LU matrix and forward/back propagation
def LUSolve(lu,bvec):
    #back substitution for x
    a = np.array(lu,float) #declare A as numpy array
    b = np.array(bvec,float) #declare b as numpy array
    n = len(a)
    y = np.zeros((n,1),float) #find {y} with [L]{y}={b}
    x = np.zeros((n,1),float) #find {x} with [U]{x}={y}
    #first do forward sub for {y}
    for k in range(0,n,1): #start from the bottom row
        y[k] = (b[k] -np.dot(a[k,0:k],y[0:k]))
    #then back sub for {x}
    for k in range(n-1,-1,-1): #start from the bottom row
        x[k] = (y[k] -np.dot(a[k,k+1:n],x[k+1:n]))/a[k,k]
    return x
