import matplotlib.pyplot as plt
plt.axes()

circle = plt.Circle((0,0), radius=0.75, fc = 'y')
plt.gca().add_patch(circle)
plt.axis('scaled')

points = [[1,1], [2,1], [4,4]]
line = plt.Polygon(points, closed=None, fill=None, edgecolor='r')
polygon


plt.gca().add_patch(line)
plt.show()
plt.gca().add_patch(circle)
figure()
plt.plot(line)

from pylab import *

points = []
points.append((-0.25, -1.0))
points.append((0.7, -0.7))
points.append((1,0))
points.append((0.7,1))
points.append((-0.25,1.2))
points.append((-1,0.5))
points.append((-1,-0.5))
points.append((-0.25, -1.0))

a_line = plot(*zip(*points))[0]
a_line.set_color('g')
a_line.set_marker('o')
a_line.set_markerfacecolor('b')
a_line.set_markersize(10)
axis([-1.5,1.5,-1.5,1.5])

show()

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x =[1,2,3,4,5,6,7,8,9,10]
y =[5,6,2,3,13,4,1,2,4,8]
z =[1,1,1,1,1,1,1,1,1,1]



ax.scatter(x, y, z, c='r', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()



