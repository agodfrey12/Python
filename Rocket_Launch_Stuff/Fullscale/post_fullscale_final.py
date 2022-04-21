#FULL SCALE DATA 

import numpy as np
import matplotlib.pyplot as plt

plt.close('all')


def filter(vec,tau):
    outvec = 0*vec
    outvec[0] = vec[0]
    for x in range(1,len(vec)-1):
        outvec[x] = (1-tau)*outvec[x-1] + tau*vec[x]
    return outvec


files = ['concatenated1.txt','concatenated2.txt','concatenated3.txt','concatenated4.txt']

px_list = []
py_list = []

for file in files:
    data = np.loadtxt(file)
    time = data[:,0]
    x = data[:,1] #CPB
    y = data[:,2] #CPB
    z = data[:,3] #CPB
    Ax = data[:,4]  #IMU
    Ay = data[:,5]  #IMU
    Az = -data[:,6] #IMU
    gx = data[:,7] 
    gy = data[:,8]
    gz = data[:,9]
    time = time[119783:]
    x = x[119783:]
    y = y[119783:]
    z = z[119783:]
    Ax = Ax[119783:]
    Ay = Ay[119783:]
    Az = Az[119783:]
    gx = gx[119783:]
    gy = gy[119783:]
    gz = gz[119783:]
    Ax_combo = (x + Ax)/2
    Ay_combo = (y + Ay)/2
    Az_combo = (z + Az)/2
    #A = np.sqrt(Ax_ai**2 + Ay_ai**2 + Az_ai**2)
    #A = np.sqrt(Ax**2 + Ay**2 + Az**2)
    #G = np.sqrt(gx**2 + gy**2 + gz**2)
    
    #plt.figure()
    #plt.plot(time,Ax_combo, label='x')
    #plt.plot(time,Ay_combo, label='y')
    #plt.plot(time,Az_combo, label='z')
    #plt.grid()
    #plt.legend()
    #plt.title('Acceleration')
    #plt.xlabel('Time (sec)')
    #plt.ylabel('Acceleration (m/s^2)')
    
    ########################## filter #####################################
    
    tau = 0.7 
    Ax_f = filter(Ax_combo,tau)
    Ay_f = filter(Ay_combo,tau)
    Az_f = filter(Az_combo,tau)
    gx_f = filter(gx,tau)
    gy_f = filter(gy,tau)
    gz_f = filter(gz,tau)
    
    #plt.figure()
    #plt.title('Filtered Acceleration Data')
    #plt.plot(time,Ax_f,label='Ax_tf',color='k')
    #plt.plot(time,Ay_f,label='Ay_tf',color='y')
    #plt.plot(time,Az_f,label='Az_tf',color='r')
    #plt.legend()
    
    ############### starting here only use filtered data ##################
    q0 = 0*Ax_f
    q1 = 0*Ax_f
    q2 = 0*Ax_f
    q3 = 0*Ax_f
    q0[0] = 1.0
    GEARTH = 9.81
    for i in range(0,len(Ax_f)-1):
        # Extract Ax,Ay,Az
        ax = Ax_f[i]
        ay = Ay_f[i]
        az = Az_f[i]
        # Convert to Gs
        ax /= GEARTH
        ay /= GEARTH
        az /= GEARTH

        # Normalise accelerometer measurement
        recipNorm = np.sqrt(ax * ax + ay * ay + az * az)
        ax /= recipNorm
        ay /= recipNorm
        az /= recipNorm

        # Estimated direction of gravity and vector perpendicular to magnetic flux
        halfvx = q1[i] * q3[i] - q0[i] * q2[i]
        halfvy = q0[i] * q1[i] + q2[i] * q3[i]
        halfvz = q0[i] * q0[i] - 0.5 + q3[i] * q3[i]

        # Error is sum of cross product between estimated and measured direction of gravity
        halfex = (ay * halfvz - az * halfvy);
        halfey = (az * halfvx - ax * halfvz);
        halfez = (ax * halfvy - ay * halfvx);

        # Apply proportional feedback
        gxi = gx_f[i]
        gyi = gy_f[i]
        gzi = gz_f[i]
        twoKp = 2.0
        gxi += twoKp * halfex
        gyi += twoKp * halfey
        gzi += twoKp * halfez

        # Integrate rate of change of quaternion
        elapsedTime = time[i+1] - time[i]
        gxi *= (0.5 * elapsedTime);		# pre-multiply common factors
        gyi *= (0.5 * elapsedTime);
        gzi *= (0.5 * elapsedTime);
        qa = q0[i]
        qb = q1[i]
        qc = q2[i]
        q0[i+1] = q0[i] + (-qb * gxi - qc * gyi - q3[i] * gzi)
        q1[i+1] = q1[i] + (qa * gxi + qc * gzi - q3[i] * gyi)
        q2[i+1] = q2[i] + (qa * gyi - qb * gzi + q3[i] * gxi)
        q3[i+1] = q3[i] + (qa * gzi + qb * gyi - qc * gxi);

        # Normalise quaternion
        Norm = np.sqrt(q0[i+1] * q0[i+1] + q1[i+1] * q1[i+1] + q2[i+1] * q2[i+1] + q3[i+1] * q3[i+1])
        q0[i+1] /= Norm
        q1[i+1] /= Norm
        q2[i+1] /= Norm
        q3[i+1] /= Norm

    roll = np.arctan2(2.*(q0*q1 + q2*q3),1-2*(q1**2 + q2**2))
    pitch = np.arcsin(2.*(q0*q2-q3*q1)) 
    yaw = np.arctan2(2.*(q0*q3 + q1*q2),1-2.*(q2**2 + q3**2))
    
    #plt.figure()
    #plt.grid()
    #plt.title('Roll, Pitch, Yaw')
    #plt.xlabel('Time (sec)')
    #plt.ylabel('Euler Angles (rad)')
    #plt.plot(time,roll,label='Roll')
    #plt.plot(time,pitch,label='Pitch')
    #plt.plot(time,yaw,label='Yaw')
    #plt.legend()
    

######################### body frame to inertial ##########################

    Ax_I = 0*Ax_f
    Ay_I = 0*Ay_f
    Az_I = 0*Az_f
    for i in range(0,len(Ax_f)):
        ax = Ax_f[i]
        ay = Ay_f[i]
        az = Az_f[i]
        ab = np.array([ax,ay,az])
        phi = roll[i]
        theta = pitch[i]
        psi = yaw[i]
        ctheta = np.cos(theta)
        cpsi = np.cos(psi)
        sphi = np.sin(phi)
        stheta = np.sin(theta)
        cphi = np.cos(phi)
        spsi = np.sin(psi)
        ttheta = np.tan(theta)
        TIB = np.asarray([[ctheta*cpsi,sphi*stheta*cpsi-cphi*spsi,cphi*stheta*cpsi+sphi*spsi],[ctheta*spsi,sphi*stheta*spsi+cphi*cpsi,cphi*stheta*spsi-sphi*cpsi],[-stheta,sphi*ctheta,cphi*ctheta]])
        aI = np.matmul(TIB,ab)
        Ax_I[i] = aI[0]
        Ay_I[i] = aI[1]
        Az_I[i] = aI[2] - GEARTH #Substract Gravity inertia
        
    #plt.figure()
    #plt.grid()
    #plt.title('Inertial Acceleration')
    #plt.xlabel('Time (sec)')
    #plt.ylabel('Acceleration Inertial (m/s^2)')
    #plt.plot(time,Ax_I,label='Ax')
    #plt.plot(time,Ay_I,label='Ay')
    #plt.plot(time,Az_I,label='Az')
    
####################### double integrate to get position ###################

    vx = 0*Ax_I
    vy = 0*Ay_I
    vz = 0*Az_I
    
    for i in range(0,len(Ax_I)-1):
        elapsedTime = time[i+1]-time[i]
        vx[i+1] = vx[i] + Ax_I[i]*elapsedTime
        vy[i+1] = vy[i] + Ay_I[i]*elapsedTime
        vz[i+1] = vz[i] + Az_I[i]*elapsedTime
        
    #plt.figure()
    #plt.grid()
    #plt.title('Inertial Velocity vs Time')
    #plt.xlabel('Time (sec)')
    #plt.ylabel('Velocity Inertial (m/s)')
    #plt.plot(time,vx,label='Vx')
    #plt.plot(time,vy,label='Vy')
    #plt.plot(time,vz,label='Vz')
    
    px = 0*Ax_I
    py = 0*Ay_I
    pz = 0*Az_I
    
    for i in range(0,len(Ax_I)-1):
        elapsedTime = time[i+1]-time[i]
        px[i+1] = px[i] + vx[i]*elapsedTime
        py[i+1] = py[i] + vy[i]*elapsedTime
        pz[i+1] = pz[i] + vz[i]*elapsedTime
    
    #plt.figure()
    #plt.grid()
    #plt.title('Inertial Position Estimation')
    #plt.xlabel('Time (sec)')
    #plt.ylabel('Position Inertial (m)')
    #plt.plot(time,px,label='x')
    #plt.plot(time,py,label='y')
    #plt.plot(time,pz,label='z')
    #plt.legend()

##################### store x and y values at "landing" ###################

    px_list.append(px[-1])
    #print(px_list)
    py_list.append(py[-1])
    #print(py_list)
    
#print('X values for landing =', px_list)
#print('Y values for landing =', py_list)

finalx = np.sum(px_list)/len(px_list)
finaly = np.sum(py_list)/len(py_list)
print('The Final Predicted Coordinates:[',finalx,',',finaly,']')

result = np.sqrt(finalx**2 + finaly**2)
print('Final Straight Line Distance is:',result,'(m)')

plt.figure()
plt.grid()
plt.scatter(px_list,py_list,s=100,label='Landing Prediction per IMU')
plt.plot(0,0,'r*',markersize=18,label='Launchpad')
plt.plot(finalx,finaly,'g*',markersize=18,label='Final Landing Prediction')
plt.title('Landing Coordinates')
plt.xlabel('X distance (m)')
plt.ylabel('Y distance (m)')
plt.legend()


    
plt.show()