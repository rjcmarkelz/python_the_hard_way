import networkx as nx
import matplotlib.pyplot as plt
from graphviz import *
G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2,3])
G.add_edge(1,2)
G.add_edge(2,3)

nx.draw(G)
nx.draw_random(G)
plt.show()

DG=nx.DiGraph()
DG.add_weighted_edges_from([(1,2,0.5), (3,1,0.75)])
DG

nx.draw(DG)
plt.show()

nx.draw_graphviz(G)

class Leaf(object):
    '''
    This class is a leaf. It has special methods to calculate photosynthesis
    and respiration. 
    '''
    class_counter = 0
    def __init__(self, name='', shape='rect', area=1, photo_dt=10, resp_dt=2):
        self.id = Leaf.class_counter
        Leaf.class_counter += 1
        self.area = area
        self.photo_dt = photo_dt
        self.resp_dt = resp_dt
        self.shape = shape

    def photosynthesis(self):
        return (self.area * self.photo_dt)

    def respiration(self):
        return (self.area * self.resp_dt) / 2

plant = nx.Graph()
leafin = Leaf('leafin')
stemin = Leaf('stemin')
petiolein = Leaf('petiolein')
rootin = Leaf('rootin')
leafin.photosynthesis()
# returns 10

plant.add_node('leafclass', data = leafin, color = 'green')

leafout = plant.node['leaf']['data']

leafout.photosynthesis()
# returns 10

leafout.respiration()
# returns 1.0

leafin == leafout
# returns TRUE

plant.add_node('stemclass', data = stemin)

plant.add_node('petioleclass', data = petiolein)

plant.add_node('rootclass', data = rootin)

plant.add_edge('stemclass', 'rootclass', weight = 5, color = 'red')

nx.draw(plant)
plt.show()








