#Aaron Godfrey
#Quiz 1
#2/11/2021

#Problem 1 - Divisibility

def div(x): #defining the divisibility function
    if x % 3 == 0: #"==0" means if condition is met, skip other steps (checking for divisiblity of x by 3)
        print("x is divisible by 3")
    elif x % 7 == 0: #checking to see if x is divisible by 7
        print("is divisible by 7")
    else: #if divisible by neither print this statement
        print("x is not divisible by 3 or 7")
        
#--------------------------------------------------------------
#Problems 2-5

import numpy as np

a=np.array([[4,-3,6],[8,-3,10],[-4,12,-10]]) #the numpy array of my a matrix
b=np.array([0,1,0]) #numpy array of b vector

def LUD(amat): #LUDecomposition
    a=np.array(amat,float) #declaring the amat as a float array
    n=len(a)
    #Elimination Phase
    for k in range(0,n-1): #pivot over n-1 rows
        for i in range(k+1,n): #loop for rows being reduced
            if a [i,k] !=0.0: #stops division of zero
                #pivoting factor of lambda
                lam = a[i,k]/a[k,k]
                #Eliminate first non-zero entry in current row
                a[i,k:n]=a[i,k:n]-lam*a[k,k:n]
                a[i,k]=lam 
    print("The LUD of [A] is",a) #printing the a matrix after it has been LUD
    return(a)

def LUS(aumat,bmat): #LUSolve
    a=np.array(aumat,float) #declaring the augmented a matrix as a float
    b=np.array(bmat,float) #declaring b matrix as a float
    n=len(a)
    #Forward substitution [L]{y}={b}
    y=np.zeros((len(b),1),float) #how to find y
    for k in range(0,n):
        y[k]=(b[k]-np.dot(a[k,0:k],y[0:k]))
    #Solve [U]{x}={y} back sub
    x=np.zeros((len(b),1),float) #how to find x
    for k in range (n-1,-1,-1):
        x[k]=(y[k]-np.dot(a[k,k+1:n],x[k+1:n]))/a[k,k]
    print("x=",x)
    return(x)

Q = (LUS(LUD(a),b)) #taking LUD of [A] and {b} then LUS that
b=np.dot(a,Q) #{b} = [A]{x}
print("b=",b)
print("Here is my answer:")
print(Q)

