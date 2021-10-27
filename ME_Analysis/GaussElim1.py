#1-26-2021 Lecture
#Gauss Elim

#x = GaussElim(A,b)
#pass in variables A and b
#output is vector x
#A=[[3,0,-3],[2,1,3],[1,3,0]]
#b=[15,-8,7]
import numpy as np

#Gauss Elimination function
def GaussElim(amat,bvec):
    a = np.array(amat,float) #declare A as numpy array
    b = np.array(bvec,float) #declare b as numpy array
    n = len(b)
    #Elimination phase
    for k in range(0,n-1): #loop for pivot row
        for i in range(k+1,n): #rows being reduced
            if a[k,k] !=0: #to stop division of 0
                lam = a[i,k]/a[k,k]; #lamda multiplier
                #reduce current tow in augmented matrix
                a[i,k:n] = a[i,k:n] - lam*a[k,k:n]
                b[i] = b[i] - lam*b[k]

    #back substitution for x
    x = np.zeros((n,1),float)
    for k in range(n-1,-1,-1): #start from the bottom row
        x[k] = (b[k] -np.dot(a[k,k+1:n],x[k+1:n]))/a[k,k]
    return x 