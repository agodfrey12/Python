#Implicit Method

import numpy as np
import matplotlib.pyplot as plt

L = 10 #length of rod
ns = 6 #number of spacial grid points
dx = L/(ns-1) #spacial interval
k = 0.835 #heat transfer coef
tf = 5 #final time
tp = 0.1 #time interval
h = tp #time step
nt = np.int16(tf/h+1) #total number of time steps
lambd = k*h/dx**2
tePr = np.zeros((nt,ns),float) #grid of points in time and space
Te = np.zeros((ns,1),float) #the temp array at each time point
coefm = np.zeros((ns,ns),float) #stiffness matrix
Te[0]=100 
Te[ns-1] = 50 
nth = 0 #nth time point
tend = 0 #timout index
tol = 1e-6 #endpoint tol

#apply boundary conditions to the 2D array of time/space
tePr[:,0]=Te[0]
tePr[:,ns-1]=Te[ns-1]

#evaluate stiffness matrix
for i in range(ns):
    if i > 0 :
        coefm[i,i-1] = -lambd
    if i < ns-1:
        coefm[i,i+1] = -lambd
    coefm[i,i] = 1+2*lambd 
print(np.round(coefm,3))

#create the main time loop
while(1):
    tend = tend + tp
    #RHS with known values
    r = np.zeros((ns,1),float)
    #loop through spatial tips 
    for ii in range(1,ns-1):
        if ii == 1:
            r[ii] = tePr[nth+1,ii-1]*lambd + tePr[nth,ii] 
        elif ii == ns-2:
            r[ii] = tePr[nth+1,ii+1]*lambd + tePr[nth,ii]
        else:
            r[ii] = tePr[nth,ii] #middle value
    #solve for the new time point with [A]{t} = {r}
    Te[1:ns-1] = np.dot(np.linalg.inv(coefm[1:ns-1,1:ns-1]),r[1:ns-1])
    nth = nth +1
    tePr[nth,:] = Te[:,0]
    if tend + tol > tf:
        break 
#print the matrix of temp
print(np.round(tePr,4))
#create a grid of time based temperatures to contour
X = np.arange(0,L+tol,L/(ns-1))
Y = np.arange(0,tf+tol,tp)
X2,Y2 = np.meshgrid(X,Y)
fig,axs = plt.subplots(1,sharex=True,sharey=True) #for contour plots
cf = axs.contourf(X2,Y2,tePr)
#anotate the plot with temp range
fig.colorbar(cf,ax=axs)
plt.xlabel('space')
plt.ylabel('time')

