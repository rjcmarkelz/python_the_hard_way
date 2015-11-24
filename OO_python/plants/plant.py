#plant.py
class Plant(object):
    '''
    '''
    # X
    # Y
    # age
    # development

class Organ(object):
    '''
    '''
    def __init__(self, name):
        self.name = name
    # shape
    # size
    # X
    # Y
    # Z
    # C
    # N

class Leaf(Organ):
    '''
    '''
    def __init__(self, area, rate):
        self.area = area
        self.rate = rate
    def photo(self):
        return print(area*rate)
    def resp(self):
        return area*rate/2

class Stem(Organ):
    '''
    '''
    def photo():
        pass
    def resp():
        pass

class Root(Organ):
    '''
    '''
    def sink():
        pass
    def NFinder():
        pass
    def PFinder():
        pass

class Point:
    def move(self, x, y):
        self.x = x
        self.y = y
    def reset(self):
        self.move(0, 0)

