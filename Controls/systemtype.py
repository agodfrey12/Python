# Determine System Type

'''
num = plant numerator
den = plant denominator
KP = proportional constant
KIn = Integral Ctrl constant (num)
KIn = Integral Ctrl constant (den)
KD = Derivative Ctrl constant 
hnum = sensor numerator
hden = sensor denominator
ref = reference input
t = response time-range
'''

import control
import control.matlab as matlab
import matplotlib.pyplot as plt
import numpy as np

def systemtype(num=1, den=1, KP=1, KIn=1, KId=0, KD=1, hnum=1, hden=1, ref=0, t=np.arange(0,1,.01)):
    
    # Find the TF for the Controller Dc
    KD = np.array(KD) # D
    KPD = np.append(KD,KP) # PD
    Dc = control.tf(KIn,[1,KId]) + control.tf(KPD,1) #PID
    print('DC', Dc)
    
    G = control.tf(num,den) # Open loop TF
    H = control.tf(hnum,hden) # Sensor dyn
    sysTF = G*Dc/(1+Dc*G*H) # closed loop TF
    sysS = control.minreal(1-sysTF,None,False) # Sensitivity
    print('TF:', sysTF)
    print('Sensitivity:', sysS)
    
    # Find zeros of sensitivity
    zeros = control.zero(sysS)
    print('Zeros: ', zeros)
    # Find zeros at origin
    num0s = np.count_nonzero(( zeros == 0))
    # System type is given by zeros of S at (0,0)
    sysType = num0s
    # Find ess based on system type
    # R(s) by system type
    sysR = np.zeros(num0s+1)
    sysR[0] = 1
    sysR = control.tf(1,sysR) 
    # S(s)R(s) 
    sysErr = control.minreal(sysS*sysR,None,False)
    ess = control.evalfr(sysErr,0)
    print('System type:' ,sysType, '\nSystem type Err:', ess)
    
    # Find time domain response by given input r(t)
    sysSS = control.tf2ss(sysTF)
    yout = matlab.lsim(sysSS,ref,t)
    eRef = ref[-1] - yout[0][-1]
    print('Reference Err: ', eRef)
    plt.plot(t,yout[0])
    plt.grid()
    plt.xlabel('time (s)')
    plt.ylabel('y(t)')
    return sysType, eRef
    