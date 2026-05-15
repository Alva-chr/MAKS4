import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from math import sin,cos, pi
import random as r
# Set the global font size for all plot elements
plt.rcParams.update({'font.size': 14})

N = 50
v0 = 0.03
R = 0.1
n = 1
eta = [0,0.05,0.1,pi/2,pi,2*pi]
eta_labels = ["0", "0.05", "0.1", "$\pi/2$", "$\pi$", "$2\pi$"]
time_average = []
T = 1000

t_plot = np.arange(0,T)
idx = 0
for e in eta:
    theta_list = []

    # Initial Conditions
    x = np.random.rand(N)
    y = np.random.rand(N)
    angle = np.random.rand(N)*2*np.pi
    angle_temp = np.zeros_like(angle)
    # plt.ion()
    # fig, ax = plt.subplots(figsize=(6,6))
    # q = ax.quiver(x,y,np.cos(angle),np.sin(angle))

    for step in range(0,T):
        sumx = np.zeros_like(x)
        sumy = np.zeros_like(y)
        for i in range(N):
            dx = x-x[i]
            dy = y-y[i]
            condlistX = [dx<-0.5, dx>=0.5]
            choicelistX = [dx+1, dx-1]

            dx = np.select(condlistX,choicelistX,default=dx)
            condlistY = [dy<-0.5, dy>=0.5]
            choicelistY = [dy+1, dy-1]

            dy = np.select(condlistY,choicelistY,default=dy)

            dist_squared = dx*dx+dy*dy

            mask = (dist_squared<R*R)

            sumx[i] = np.sum(np.cos(angle[mask]))
            sumy[i] = np.sum(np.sin(angle[mask]))

        angle = (np.arctan2(sumy, sumx) + e * (np.random.random(N) - 0.5) * 2) % (2 * np.pi)
        
        x = (x+v0*np.cos(angle))%1
        y = (y+v0*np.sin(angle))%1
        theta_list.append(abs(np.sqrt(np.sum(np.cos(angle))**2+np.sum(np.sin(angle))**2))/N)

        #q.remove()

        #q = ax.quiver(x, y, np.cos(angle), np.sin(angle))

        #plt.pause(0.001)

    plt.plot(t_plot, theta_list, label="$\eta = $"+eta_labels[idx])
    summis = sum(theta_list)/T
    time_average.append(summis)
    idx += 1

plt.xlabel("Time")
plt.ylabel("$\Phi(t)$")
plt.title("Order parameter for different values of $\eta$ over time")
plt.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0))
plt.tight_layout() 
plt.show()

plt.figure() 
plt.bar(eta_labels, time_average, color='skyblue', edgecolor='black', width=0.6)
plt.xlabel("$\eta$")
plt.ylabel("Time averaged $\Phi(t)$")
plt.title("Time-averaged order parameter as a function of $\eta$")
plt.ylim(0, 1.05) 
plt.show()