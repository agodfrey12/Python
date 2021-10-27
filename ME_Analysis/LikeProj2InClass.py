#Aaron Godfrey
#In Class Like Project 2
#4/20/2021

import numpy as np
import matplotlib.pyplot as plt

#Define Variables
L= 10 #meters
ns = 6 #number of divisions
dx = L/(ns-1) #element length
sc = 1/dx #stiffness maxtric coeff
d1 = 0 #deflection boundary coeff
dr = 0 #deflections boundary coeff
ar = 0.1 #area
Y = 200E9 #Young's Modulus
DLC = -1000 #distributed load

def f1(x): return 1-x/dx
def f2(x): return x/dx

#evaluate the BC due to the distributed load
h = 0.001 #panel width
x = np.arange(h,dx,h)
f1_int = h*f1(0)/2 + h*np.sum(f1(x)) + h*f1(dx)/2 #LHS
f2_int = h*f2(0)/2 + h*np.sum(f2(x)) + h*f2(dx)/2 #RHS
f1_int = f1_int*DLC
f2_int = f2_int*DLC
print('f1_int=',f1_int)
print('f2_int=',f2_int)

#stiffness matrix
K = np.zeros((ns,ns),float)
for i in range(1,ns):
    K[i-1:i+1,i-1:i+1] = K[i-1:i+1,i-1:i+1] + [[sc,-sc],[-sc,sc]]
K[:,0] = 0; K[:,ns-1] = 0
K[0,0]= 1; K[ns-1,ns-1] = -1
K = K*Y*ar
print('K=',K)

#define the RHS
r = np.zeros((ns,1),float)
for i in range(0,ns-1): 
    r[i] = r[i]+f1_int
    r[i+1] = r[i+1]+f2_int
#modify r to add deflections
r[0] = r[0] - sc*d1
r[1] = r[1] + sc*d1
r[ns-1] = r[ns-1] - sc*dr
r[ns-2] = r[ns-2] + sc*dr
print('r=',r)
'''
#solve for u using linear algebra
u_du = np.dot(np.linalg.inv(K),r)
u = np.array(u_du)
u[0] = 0 
u[ns-1] = 0

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
LU = LUD(K)
u_du = LUS(LU,r)
'''