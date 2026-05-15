import numpy as np
import matplotlib.pyplot as plt
from math import sin,cos, pi
import random as r

N = 500
v0 = 0.03
R = 0.1


x = np.random.rand(N)
y = np.random.rand(N)

angu = np.cos(np.linspace(0, 2*np.pi, N))
angv = np.sin(np.linspace(0, 2*np.pi, N))



plt.quiver(x,y,angu,angv)
plt.xlim(0,1)
plt.ylim(0,1)


plt.gca().set_aspect('equal')

plt.show()
