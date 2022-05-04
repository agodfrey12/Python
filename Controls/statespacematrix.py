# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 10:16:51 2022

@author: Aaron Godfrey
"""

import control

A = [[0,0,0,1/2],[1,0,0,0],[0,1,0,1],[0,0,-1,-4]]
B = [[0],[0],[0],[1]]
C=[1,1,0,1]
D=[0]
sys = control.ss(A, B,C,D)
tf=control.ss2tf(sys)
ss=control.tf2ss(tf)
ss, T=control.canonical_form(sys)
print(ss)
