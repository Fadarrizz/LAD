class Building(object):
    """Class definition for a house construction"""
    # __metaclass__ = ABCMeta
    buildingsPlaced = []
    coords          = []
    neighbours       = []
    house_type      = 0
    width           = 0
    length          = 0
    mtr_clearance   = 0
    price           = 0
    percentage      = 0

    def __init__(self, name, x, y):
        self.name   = name
        self.x      = x
        self.y      = y
        self.LB     = x, y
        self.LT = (x, (y + self.length))
        self.RT = ((x + self.width), (y + self.length))
        self.RB = ((x + self.width), y)
        self.coordinates = [(x,y), (x, (y + self.length)), ((x + self.width),
                        (y + self.length)), ((x + self.width), y)]


class House(Building):
    """Class definition for a detached house."""
    house_type      = 'House'
    width           = 8
    length          = 8
    mtr_clearance   = 2
    price           = 285000
    percentage      = 1.04
    color           = '#8ca861'

    # def calc_value(self, free_space):
    #     self.free_space = xxxx
    #     self.value = self.price + self.price * (self.percentage * self.free_space)

class Bungalow(Building):
    """Class definition for a detached house."""
    house_type      = 'Bungalow'
    width           = 10
    length          = 7.5
    mtr_clearance   = 3
    price           = 399000
    percentage      = 1.04
    color           = '#E5B181'

    # def calc_value(self, free_space):
    #     self.free_space = xxxx
    #     self.value = self.price + self.price * (self.percentage * self.free_space)

class Maison(Building):
    """Class definition for a detached house."""
    house_type      = 'Maison'
    width           = 11
    length          = 10.5
    mtr_clearance   = 6
    price           = 610000
    percentage      = 1.06
    color           = '#DE6B48'

    # def calc_value(self, free_space):
    #     self.free_space = xxxx
    #     self.value = self.price + self.price * (self.percentage * self.free_space)

class Waterbody(object):
    """Class definition for a waterbody."""
    color           = "#7DBBC3"
    def __init__(self, x, y, width, length):
        self.x      = x
        self.y      = y
        self.width  = width
        self.length = length

        self.a = self.width / 2
        self.b = self.length / 2