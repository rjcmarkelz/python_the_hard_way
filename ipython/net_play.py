from network import Vertex
from network import Graph
from network import getcoord
from mpl_toolkits import mplot3d
import numpy as np 
import matplotlib.pyplot as plt
%matplotlib inline

# define the structure as nodes
n0 = Vertex('n1', 0, 0, 0)
s1 = Vertex('s1', 0, 0, 1)
p1 = Vertex('p1', 0, 0.25, 1)
l1 = Vertex('l1', 0, 0.5, 1.25)

s2 = Vertex('s2', 0, 0, 2)
p2 = Vertex('p2', 0, 0.25, 3)
l2 = Vertex('l2', 0, 0.5, 3.25)

s3 = Vertex('s3', 0, 0, 3)
p3 = Vertex('p3', 0, 0.25, 4)
l3 = Vertex('l3', 0, 0.5, 4.25)

r1 = Vertex('l3', 0, 0, -1)

oblist = [n0, s1, p1, l1, s2, p2, l2, s3, p3, l3, r1]
oblist

zdata = ob.get_coord()[2]
data = getcoord(oblist)
xdata = np.asarray(data[0])
ydata = np.asarray(data[1])
zdata = np.asarray(data[2])
xdata
ydata

c = ('b', 'b', 'r', 'g', 'b', 'r', 'g', 'b', 'r', 'g', 'k')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(xdata, ydata, zdata, c = c , marker = 'o', s = 400)




plt.show()

g = Graph()
g.add_vertex(n0)
g.add_vertex(s1)
g.add_vertex(p1)
g.add_vertex(l1)

g.add_edge(n0, s1)
g.add_edge(s1, p1)
g.add_edge(p1, l1)
g.get_vertices()



