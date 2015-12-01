from network import Vertex
from network import Graph
from mpl_toolkits import mplot3d
import numpy as np 
import matplotlib.pyplot as plt
%matplotlib inline

# define the structure as nodes
n0 = Vertex('n1', 0, 0, 0)
s1 = Vertex('s1', 0, 0, 1)
p1 = Vertex('p1', 0, 0.25, 1)
l1 = Vertex('l1', 0, 0.5, 1.25)

oblist = [n0, s1, p1, l1]
oblist

def getcoord(oblist):
    xdata = []
    ydata = []
    zdata = []
    for ob in oblist:
        xdata.append(ob.get_coord()[0])
        ydata.append(ob.get_coord()[1])
        zdata.append(ob.get_coord()[2])
    return [xdata, ydata, zdata]

zdata = ob.get_coord()[2]
data = getcoord(oblist)
xdata = np.asarray(data[0])
ydata = np.asarray(data[1])
zdata = np.asarray(data[2])

axe = plt.axes(projection='3d')
axe.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');

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



