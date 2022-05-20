import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for k in range(0,50):
    ax.scatter(k+1,k-1, k*k)
    plt.draw()
    plt.pause(0.02)
    #ax.cla()