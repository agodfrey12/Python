#Example 3.18
import numpy as np
import matplotlib.pyplot as plt
import control

#sys = (1/m)/(s^2+b/ms)

#zeros = []
#pole = [0, -b/m]

m = 1000 # mass of vehicle
b = 50 # damping coeff

sys = control.tf([1/m], [1,b/m,0])
z = control.zero(sys) #zeros
p = control.pole(sys)

print("Zeros =", z)
print("Poles =", p)