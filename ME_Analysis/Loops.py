#1/21/2021 Lecture
#Aaron Godfrey

import numpy as np

# find out o f a > 4 and a < 6 using if statements
a=5 #any number
if a == 2: #check if a = 2
    print("a = 2")
elif (a > 4) and (a < 6): #check if a > 4 & < 6
    print("a > 4 and < 6")
else: #do nothing
    print ("unknown")
    
#------------------------------------------------------

#looking at loops: for, while

#for loop

#find the distance travelled by a falling object
#d = 0.5*gt^2

g=9.81; dist1=[] # empty distance array
t=0 #initial time

#use a for loop to calculate the distance at each second until 10s

for t in range (0,11):
    d = 0.5*g*t**2 #distance fallen due to gravity
    dist1.append(d)
print("dist1=",dist1)


#while loop

#use a while loop to calculate the distance at each second until 10s
t=0 #initial time
g=9.81; dist2=[] #empty distance array
ts=11 #time stop
while t < ts:
    d = 0.5*g*t**2 #distance fallen
    dist2.append(d) #input array
    t = t+1 #increment t at each iteration
print("dist2=",dist2)

#-----------------------------------------------------

#same loops but with the numpy library


t=0;ts=11
dist3=np.array([]) #declare dist and an empty numerical array
while t < ts:
    d = 0.5*g*t**2 #distance fallen
    dist3=np.append(dist3,[d]) #input array
    t = t+1 #increment t at each iteration
print("dist3=",dist3)

t=0;ts=11
dist4=np.array([])
for t in range (0,11):
    d = 0.5*g*t**2 #distance fallen due to gravity
    dist4=np.append(dist4,[d]) #input array
print("dist4",dist4)
