# Exam 1 Routh Array

import numpy.linalg as linalg
import numpy as np

a = np.array([1,5,10,10,5,3])
n = len(a) 
m = int(np.ceil(n/2)) 

ra = np.zeros((n,m))

ra[0] = a[0:n:2]
ra[1][0:len(a[1:n:2])] = a[1:n:2]
 
for i in range(2,n):
    for j in range(0,np.size(ra,1)-1):
        top_row = [ra[i-2][0],ra[i-2][j+1]]
        bot_row = [ra[i-1][0],ra[i-1][j+1]]
        detmat = np.array([top_row,bot_row])
        if ra[i-1][0] != 0:
            ra[i][j] = -linalg.det(detmat)/ra[i-1][0]
        else:
            ra[i][j] = --ra[i-2][j+1] 
            
stability = True
for i in range(0,np.size(ra,0)):
    if ra[i][0] < 0:
        stability = False
print('Rouths Array:', ra)
print('Stability: ', stability)
