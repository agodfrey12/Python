#1/26/2021 Lecture
#Like HW1 #2

import numpy as np

#define a function for squaring a scalar
def f(x): return x**2
ans = f(2.)
print(ans)
print(f(5.))

#-----------------------------------------------------

#calculate pressure fluctuation in a tank (compressed methane)
#the tank volume is changing by 3*P*sin(t) t is measured in days
#let the pressure variable be y, and change by dy/dt

T=[]; Y=[]; #arrays for pressure and time
def dydt(P,t): return 3*P*np.sin(t)
y = 1500 #mmHg #initial pressure
t = 0 #start time in days
ts = 11 #stop time in days
dt = 1 #time increment
P = 250 #pressure constant

#use while loop to find the daily pressure changes

while t < ts: 
    T.append(t)
    Y.append(y)
    y = y + dydt(P,t)*dt #the Euler's method to calculate daily pressure
    t = t+1 #increment time
print(T,Y)