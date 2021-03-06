# modified heavily from http://www.bogotobogo.com/python/python_graph_data_structures.php
class Vertex:
    def __init__(self, node, X=1, Y=1, Z=1):
        self.id = node
        self.adjacent = {}
        self.coord = [X, Y, Z]

    def __str__(self):
        return str(self.id) + 'adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=10, length=1):
        self.adjacent[neighbor] = [weight, length]
        # self.adjacent[neighbor] = length

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor][0]

    def get_length(self, neighbor):
        return self.adjacent[neighbor][1]

    def get_coord(self):
        return self.coord

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

def getcoord(oblist):
    xdata = []
    ydata = []
    zdata = []
    for ob in oblist:
        xdata.append(ob.get_coord()[0])
        ydata.append(ob.get_coord()[1])
        zdata.append(ob.get_coord()[2])
    return [xdata, ydata, zdata]

