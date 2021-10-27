#Aaron Godfrey
#ME328-101
#1/19/2021
#Homework 1

import numpy as np
         
#Problem 1

P = 10000 #Principal amount of money
i = 0.066 #Interest rate

#empty array to store yearly totals
F = []

for n in range(0,8):
    #F=P(1+i)^^n
    F.append(P*(1+i)**n)
print("F=",F) 

#------------------------------------------------------------------
#Problem 2

def dydt(QA,t): return 3*QA*(np.sin(t))**2-QA #given equation

QA = 0.5 #meter/hr
y0 = 10 #meters
t = 0 #hour/starting time
ts = 11 #hours
dT = 1 #timestep
T = [] #time array
Y = [] #height array

while t < ts: 
    T.append(t)
    Y.append(y0)
    t = t + 1  #timestep function
    y0 = y0 + dydt(QA,t)*dT #given hint
print("T=",T)
print("Y=",Y)
