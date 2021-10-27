#Aaron Godfrey

import numpy as np
import matplotlib.pyplot as plt

L = 10 #bar length
ns = 5 #number of grid points
dx = L/(ns-1) #element length
stiffc = 1/dx #stiffness matrix coeff
T_l = 40 #temp boundary
T_r = 200 #temp boundary
HS = 10 #heat source

#define shape function integrals
def f1(x): return 1-x/dx #LHS
def f2(x): return x/dx #RHS

#Find element-wise heat source boundary conditions
#Use trapezoid rule
h = 0.001 #panel width
x = np.arange(h,dx,h)
f1_int = f1(0)*h/2 + h*np.sum(f1(x)) + f1(dx)*h/2 #LHS
f2_int = f2(0)*h/2 + h*np.sum(f2(x)) + f2(dx)*h/2 #RHS
f1_int = f1_int*HS
f2_int = f2_int*HS

#Stiffness Matrix
K = np.zeros((ns,ns),float)
for i in range(1,ns):
    K[i-1:i+1,i-1:i+1] = K[i-1:i+1,i-1:i+1] +\
        [[stiffc,-stiffc],[-stiffc,stiffc]]
K[:,0] = 0; K[:,ns-1] = 0
K[0,0] = 1; K[ns-1,ns-1] = -1
print('K=', K)

#RHS Known conditions - 1D array
r = np.zeros((ns,1),float)
r[0] = f1_int - stiffc*T_l
r[1] = f1_int + f2_int + stiffc*T_l
r[2] = f1_int + f2_int
r[3] = f1_int + f2_int + stiffc*T_r
r[4] = f2_int - stiffc*T_r
print(r)

#Solve LA problem
#For unknown T and dT/dx
u = np.dot(np.linalg.inv(K),r)
Te = u
Te[0] = T_l
Te[4] = T_r
print('Te(bar temperatures)=',Te)
print('u=',u)

plt.plot(np.arange(0,L+0.000001,dx),Te)
plt.title('Temperature across bar')
plt.xlabel('Distance(m)')
plt.ylabel('Temp(C)')