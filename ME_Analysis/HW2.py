#Aaron Godfrey
#2/2/2021
#HW2

import numpy as np
a=np.array([[2,-3,-1],[3,2,-5],[2,4,-1]]) #A matrix
b=np.array([3,-9,-5]) #b vector

#1
def LUD(amat): #Defining the LU Decomposition function
    a=np.array(amat,float) #decleare amat as float array
    n=len(a)
    #Elimination Phase
    for k in range(0,n-1): #pivot over n-1 rows
        for i in range(k+1,n): #rows being reduced
            if a [i,k] !=0.0: #cannot divide by 0
                #pivoting factor of lambda
                lam = a[i,k]/a[k,k]
                #Eliminate first non-zero entry in current row
                a[i,k:n]=a[i,k:n]-lam*a[k,k:n] #upper matrix
                a[i,k]=lam #lower matrix
    print("The L/U Matrix",a)
    return(a)

#2  
def LUS(aumat,bmat): #Defining the LU Solve Function
    a=np.array(aumat,float) #declare augmented amat as float array
    b=np.array(bmat,float) #declare b matrix as float array
    n=len(a)
    
    #Forward substitution [L]{y}={b}
    y=np.zeros((len(b),1),float) #find {y}
    for k in range(0,n): #designating the start
        y[k]=(b[k]-np.dot(a[k,0:k],y[0:k]))
    
    #Backward Substitution [U]{x}={y}
    print("y=",y)
    x=np.zeros((len(b),1),float) #find {x}
    for k in range (n-1,-1,-1): #designating the start 
        x[k]=(y[k] -np.dot(a[k,k+1:n],x[k+1:n]))/a[k,k]
    #print("The LU Matrix is=",x) here is another place in which you can show the final LU matrix for problem #3
    return(x) #solving for {x} where [A]{x}=[b]

#3
Q = LUS(LUD(a),b)
print("The LU matrix is",Q)
