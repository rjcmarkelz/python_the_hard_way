import networkx as nx
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

H=nx.cycle_graph(20)
G=nx.convert_node_labels_to_integers(H)
G
pos=nx.spring_layout(G,dim=3)
pos
xyz=np.array([pos[v] for v in sorted(G)])
xyz
scalars=np.array(G.nodes())+5
edgeZ = np.array(G.edges())

scalars
xyz[0]

for i,j in zip(dates,zaxisvalues0,lows,highs):
    ax.plot([1,1], color = 'g')


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xyz[:,0], xyz[:,1], xyz[:,2])
ax.plot([1,1], color = 'g')
plt.show()