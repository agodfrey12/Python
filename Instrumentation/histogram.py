import numpy as np
import matplotlib.pyplot as plt
import statistics as st

data = np.loadtxt('Hist_data_dark.txt',delimiter=',') #change to include the appropriate light level data

t = data[:,0]
s = data[:,1]
v = s*3.3/2.0**16

print('Mean of Data Set =', np.mean(v))
print('Standard Deviation of Data Set =', np.std(v))
print('Median of Data Set =', np.median(v))
print('Mode of Data Set =', st.mode(v))

dev = np.std(v)
mean = np.mean(v)


x = np.linspace(mean-3*dev,mean+3*dev,1000) 
dx = x[1]-x[0] 
N = len(v) 
fx = (1/(np.sqrt(2*np.pi)*dev))*np.exp(-(x-mean)**2/(2*dev**2))*dx*N*100

plt.hist(v)
plt.plot(x,fx,'y-')
plt.xlabel('Bins')
plt.ylabel('Number of Vals in Bin')
plt.title('Dark Environment Histogram')
plt.grid()

#x = np.linspace(mean-3*dev, mean+3*dev, 1000)
#fx = (1/(np.sqrt(2*np.pi*dev))*np.exp(-(x-mean)**2/(2*dev**2)))
#plt.plot(x,fx,'g-')

plt.show()
