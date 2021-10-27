#Aaron Godfrey
#2/2/2021
# ME 328 Lab LUDECOMP Example

import numpy as np

a=np.array([[5,6,-7],[4,9,-10],[8,52,-1]])
b=np.array([3,-12,-3])

def LUD(amat): #LUDecomposition
    a=np.array(amat,float)
    n=len(a)
    #Elimination Phase
    for k in range(0,n-1): #pivot over n-1 rows
        for i in range(k+1,n):
            if a [i,k] !=0.0:
                #pivoting factor of lambda
                lam = a[i,k]/a[k,k]
                #Eliminate first non-zero entry in current row
                a[i,k:n]=a[i,k:n]-lam*a[k,k:n]
                a[i,k]=lam 
            print(a)
    return(a)

def LUS(aumat,bmat): #LUSolve
    a=np.array(aumat,float)
    b=np.array(bmat,float)
    n=len(a)
    #Forward substitution [L]{y}={b}
    y=np.zeros((len(b),1),float)
    for k in range(0,n):
        y[k]=(b[k]-np.dot(a[k,0:k],y[0:k]))
    #Solve [U]{x}={y} back sub
    print(y)
    x=np.zeros((len(b),1),float)
    for k in range (n-1,-1,-1):
        x[k]=(y[k]-np.dot(a[k,k+1:n],x[k+1:n]))/a[k,k]
    return(x)

Q = (LUS(LUD(a),b))
print("Here is my answer")
print(Q)

'''
#simple loop to fill the L and U
lum=Q
n=len(a)
lmat=np.zeros((n),n)
umat=np.zeros((n),n)
for i in range(n):
    umat[i,i:n]=lum[i,i:n]
    lmat[i,0:i]=lum[0:i]
    lmat[i,i]=1
print(lmat);print(umat)
b_chk=np.dot(a,b)
 '''   