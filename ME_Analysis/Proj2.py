#Aaron Godfrey
#Project 2
#4/13/2021

import numpy as np
import matplotlib.pyplot as plt

#Define Variables
L = 10 #meters
ns = 6 #number of divisions
dx = L/(ns-1) #element length
sc = 1/dx #stiffness maxtric coeff
d1 = 0 #deflection boundary coeff
dr = 0 #deflections boundary coeff
ar = 0.1 #area
Y = 200E9 #Young's Modulus
DLC = -1000 #distributed load

#shape functions
def f1(x): return 1-x/dx
def f2(x): return x/dx

#evaluate the BC due to the distributed load applied
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
    K[i-1:i+1,i-1:i+1] = K[i-1:i+1,i-1:i+1] +[[sc,-sc],[-sc,sc]]
K[:,0] = 0; K[:,ns-1] = 0
K[0,0]= 1; K[ns-1,ns-1] = -1
K = K*Y*ar

#define the RHS
r = np.zeros((ns,1),float)
for i in range(0,ns-1): 
    r[i] = r[i]+f1_int
    r[i+1] = r[i+1]+f2_int
print('r=',r)

#solve for deflection using linear algebra
u_du = np.dot(np.linalg.inv(K),r)
u = np.array(u_du)
u[0] = 0 
u[ns-1] = 0
De = u_du
print('u_du=',u_du)
#plotting deflection in the bar
plt.plot(np.arange(0,L+0.000001,dx),u,'g*-')
plt.xlabel('Distance Along Bar')
plt.ylabel('Deflection')
plt.title('Bar Deflection')