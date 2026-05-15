import numpy as np
import matplotlib.pyplot as plt
from math import sin,cos, pi
import random as r

N = 500
v0 = 0.03
R=0.1
eta = [0,0.05,0.1,pi/2,pi,2*pi]

fish = {}

for i in range(N):
    x = r.random()
    y = r.random()
    angle = r.randrange(0, 2*pi)
    fish[i] = {(x,y,angle)}


