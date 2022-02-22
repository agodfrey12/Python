# Example 3.32
# Routh Array

import numpy.linalg as linalg
import numpy as np

a = np.array([1,4,3,2,1,4,4]) #Characteristic Eqn.
n = len(a) #NUMBER OF ROWS IN THE ROUTH ARRAY
m = int(np.ceil(n/2)) #NUMBER OF COLUMNS IN THE ROUTH ARRAY

#Initialize the Routh Array
# NOTE: INITIALIZE BY CALLING np.zeros with OUTER PARENTHESIS FOR FUNCTION
# AND INNER PARENTHESIS FOR ARRAY SIZE
ra = np.zeros((n,m))

#Fill row 0 with the even pos coeffs m=[0,2,..,n] of the TF
#Fill row 1 with the odd pos coeffs m=[1,3,..,n] of the TF
ra[0] = a[0:n:2]
ra[1][0:len(a[1:n:2])] = a[1:n:2]

# To get the negative determinant for the current cell
# Take the above 2 rows, 1st column and the right column
# For cell c[n][m], det = c[n-2][0]*c[n-1][m+1]-c[n-2][m+1]*c[n-1][0]  
for i in range(2,n):
    for j in range(0,np.size(ra,1)-1):
        #Form the 2X2 matrix for the determinant
        #THE TOP AND BOTTOM ROWS MUST BE INSIDE [] TO CREATE A MATRIX
        top_row = [ra[i-2][0],ra[i-2][j+1]]
        bot_row = [ra[i-1][0],ra[i-1][j+1]]
        detmat = np.array([top_row,bot_row])
        #Divide by the negative of the cell above in the 1st column
        if ra[i-1][0] != 0: # Check for zero 
            ra[i][j] = -linalg.det(detmat)/ra[i-1][0]#Divide by c[n-1][0]
        else:
            ra[i][j] = --ra[i-2][j+1] #else c[n-2][m+1]
            
stability = True
for i in range(0,np.size(ra,0)):
    if ra[i][0] < 0:
        stability = False
print('Rouths Array:', ra)
print('Stability: ', stability)
