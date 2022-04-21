import numpy as np 
import control 
import matplotlib.pyplot as plt 
 
#Calculate the closed and open loop TFs 
num = [1,1]
den = [1,9,0,0]
num_dc = [1]
den_dc = [1] 
G = control.tf(num,den) 
Dc = control.tf(num_dc,den_dc) 
tf = G*Dc 
print(tf)
#Calculate the open-loop poles and zeros 
zeros = control.zero(tf)
poles = control.pole(tf) 
print('poles: ', poles) 
print ('zeros: ',zeros) 
 
# Calculate departures and arrivals 
n = len(poles)
p_angs=np.zeros(n) 
m = len(zeros)
z_angs=np.zeros(m) 
 
# Departure angles at poles 
for i in range(0,n): 
    ang = np.concatenate((np.angle(poles[i]-zeros), -np.angle(poles[i]-poles))) #concatenate 
    ang = np.sum(ang)*180/np.pi -180 -360*(i) #sum 
    ang = np.round(np.mod(ang,360),2) 
    p_angs[i] = ang

# Arrival angles at zeros 
for i in range(0,m): 
    ang = np.concatenate((np.angle(zeros[i]-poles), -np.angle(zeros[i]-zeros)))  #concatenate 
    ang = np.sum(ang)*180/np.pi +180 +360*(i) #sum 
    ang = np.round(np.mod(ang,360),2) 
    z_angs[i] = ang 
print('pole deps: ', p_angs) 
print ('zero arrivs: ',z_angs) 
 
# Calculate the n-m asymptotes  
# Location 
asym_loc = (np.sum(poles)-np.sum(zeros))/(n-m) #sum 
asym_loc = np.round(np.real( asym_loc),2) 
# Angles of n-m branches 
asym_angs = np.zeros(n-m) 
print('asymptote alpha: ', asym_loc) 
for i in range(0,n-m): 
    asym_angs[i] = (180 + 360*i)/(n-m) 
print('asymptote angles: ', asym_angs) 
 
# Calculate multiple roots 
num = np.squeeze(tf.num)
den = np.squeeze(tf.den)
num_df = np.polyder(num)
den_df = np.polyder(den) 
df = np.polyadd(np.convolve(num_df,den), -np.convolve(den_df,num)) #convolve 
mroots=np.round(np.roots(df),2) 
mroots=(mroots[~np.iscomplex(mroots)]) 
mroots = np.unique(mroots)
print('multiple roots:', mroots) 
 
#Root Locus plot 
plt.figure() 
control.rlocus(tf,plotstr=[]) 
 
plt.show()