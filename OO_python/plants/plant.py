#plant.py
# class Plant(object):
#     '''
#     doc tests are up next
#     '''
#     # X
#     # Y
#     # age
#     # development

class Organ(object):
    '''
    doc tests are up next
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
        return self.area*self.rate
    
    def resp(self):
        return (self.area*self.rate)/2

class Stem(Organ):
    '''
    doc tests are up next
    '''
    def __init__(self, length, width, rate):
        self.length = length
        self.width = width
        self.rate = rate
    
    def photo(self):
        return self.length*self.width*self.rate
    
    def resp(self):
        return (self.length*self.width*self.rate)/2

class Root(Organ):
    '''
    '''
    def __init__(self, mass):
        self.mass = mass
    
    def resp(self):
        return self.mass ** (0.75)
    
    def NFinder():
        pass
    
    def PFinder():
        pass

def photo(area = 1, rate = 1):
    return area*rate

def carbon_gain():
    return 


















































