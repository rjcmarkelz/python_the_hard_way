# plant.py
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
        return self.area * self.rate

    def resp(self):
        return (self.area * self.rate) / 2


class Stem(Organ):
    '''
    doc tests are up next
    '''

    def __init__(self, length, width, rate):
        self.length = length
        self.width = width
        self.rate = rate

    def photo(self):
        return self.length * self.width * self.rate

    def resp(self):
        return (self.length * self.width * self.rate) / 2


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


class CarbView:

    def update(self, organ):
        print('Organ %s has %x carbon' % (organ.name, organ.data))
# ##### Functions #####


def photo(area=1, rate=1):
    return area * rate


def carbon_gain():
    pass

# observer pattern


class Plant(object):

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


class Data(Plant):

    def __init__(self, name=''):
        Plant.__init__(self)
        self.name = name
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()

class CarbView:

    def update(self, plant):
        print('%s has %x carbon' % (plant.name, plant.data))
