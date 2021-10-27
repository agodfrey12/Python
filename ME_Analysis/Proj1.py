#Aaron Godfrey
#Project 1/Lab 6
#3/30/2021

#Using the Crank-Nicholson Technique

import numpy as np
import matplotlib.pyplot as plt
L = 10 #length of rod in cm
ns = 6 #rod is divided into 5 equal sections in cm
dx = L/(ns-1) #spatial interval
k = 0.835 #heat transfer coeff in cm^2/s
tf = 0.5 #final time in seconds
tp = 0.1 #time interval in seconds
h = tp #time step
nt = np.int16(tf/h+1) #total number of time steps
lambd = k*h/dx**2 #heat conductivity (unit less) 
tePr = np.zeros((nt,ns),float) #grid of points in time/space
Te = np.zeros((ns,1),float) #The temperature array at each time point
coefm = np.zeros((ns,ns),float) #stiffness matrix
Te[0] = 100 #starting temperature on the RHS of rod in Celsius
Te[ns-1] = 50 #ending temperature on the LHS of rod in Celsius
nth = 0 #nth time point
tend = 0 #timeout index
tol = 1e-6 #endpoint tolerance
tePr[:,0]=Te[0] #boudnary condition on the RHS of rod
tePr[:,ns-1]=Te[ns-1] #boundary condition on the LHS of rod

#Stiffness matrix [A]
for i in range(ns): #evaluating the coeff around out poaints in time/space
    if i > 0:
        coefm[i,i-1] = -lambd #left side coeff
    if i < ns-1:
        coefm[i,i+1] = -lambd #right side coeff
    coefm[i,i] = 2*(1+lambd) #middle coeff
print(np.round(coefm,3)) #print the stiffness matrix

#Main Time Loop
while(1):
    tend = tend + tp
    #RHS with known values
    r = np.zeros((ns,1),float)
    #loop through spatial points to calculate the RHS
    for ii in range(1,ns-1): #evaluating around our point
        if ii == 1: #by left boundary
            r[ii] = tePr[nth+1,ii-1]*lambd + 2*(1-lambd)*tePr[nth,ii] \
                + tePr[nth,ii-1]*lambd +tePr[nth,ii+1]*lambd
        elif ii == ns-2: #by the right boundary
            r[ii] = tePr[nth+1,ii+1]*lambd + 2*(1-lambd)*tePr[nth,ii] \
                + tePr[nth,ii-1]*lambd + tePr[nth,ii+1]*lambd
        else: #previous temperature
            r[ii] = 2*(1-lambd)*tePr[nth,ii] \
                + tePr[nth,ii-1]*lambd + tePr[nth,ii+1]*lambd
    #Solve for the new time point with [A]{x} = {r} where x is unknown
    Te[1:ns-1] = np.dot(np.linalg.inv(coefm[1:ns-1,1:ns-1]),r[1:ns-1])
    nth = nth + 1 #time index increases by 1
    tePr[nth,:] = Te[:,0] #fill the temperature matrix for the new time
    if tend + tol > tf: #stop at final point
        break
#print the matrix of temperature
print('matrix=',np.round(tePr,4)) #Matrix of the temperature
#create a grid of time based temperatures to contour
X = np.arange(0,L+tol,L/(ns-1)) #distance
Y = np.arange(0,tf+tol,tp) #time
X2,Y2 = np.meshgrid(X,Y) #creating the mesh grid for the heat contour
fig,axs = plt.subplots(1,sharex=True,sharey=True) #for contour plots
cf = axs.contourf(X2,Y2,tePr)
#anotate the plot with temp range
fig.colorbar(cf,ax=axs) #color gradient
plt.xlabel('distance') #labeling horizontal axis - distance
plt.ylabel('time') #labeling the vertical axis - time
plt.title('Distance vs Time') #giving the plot a title
