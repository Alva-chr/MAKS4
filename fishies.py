import numpy as np
import matplotlib.pyplot as plt
from math import sin,cos, pi
import random as r

N = 500
v0 = 0.03
R=0.1
n = 1
eta = [0,0.05,0.1,pi/2,pi,2*pi]
T = 10000

# Initial Conditions
x = np.random.rand(N)
y = np.random.rand(N)
angle = np.random.rand(N)*2*np.pi
angle_temp = np.zeros_like(angle)



#Update the angle
for step in range(0,T):
    for i in range(N):
        dx = x-x[i]
        dy = y-y[i]
        np.where((dx<0.5),dx+0.5,0)

    

    angle = (np.arctan2(sumx, sumy) + eta[0] * (np.random.random(N) - 0.5) * 2) % (2 * np.pi)

    
    x = (x+np.cos(angle))%1
    y = (y+np.sin(angle))%1


    print(x[0])
    print(y[0])



