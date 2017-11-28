class Building(object):
    """Class definition for a house construction"""
    # __metaclass__ = ABCMeta
    arr             = []
    width           = 0
    length          = 0
    mtr_clearance   = 0
    price           = 0
    percentage      = 0

    def __init__(self, name, x, y):
        self.name   = name
        self.x      = x
        self.y      = y
        self.topright = self.x + self.width
        self.bottomleft = self.y - self.length
        self.bottomright = self.topright - self.length

    def coordinates(self):
        return '{}, {}'.format(self.x, self.y)

class House(Building):
    """Class definition for a detached house."""
    width           = 8
    length          = 8
    mtr_clearance   = 2
    price           = 285000
    percentage      = 1.04

    # def calc_value(self, free_space):
    #     self.free_space = xxxx
    #     self.value = self.price + self.price * (self.percentage * self.free_space)

class Bungalow(Building):
    """Class definition for a detached house."""
    width           = 10
    length          = 7.5
    mtr_clearance   = 3
    price           = 399000
    percentage      = 1.04

    # def calc_value(self, free_space):
    #     self.free_space = xxxx
    #     self.value = self.price + self.price * (self.percentage * self.free_space)

class Maison(Building):
    """Class definition for a detached house."""
    width           = 11
    length          = 10.5
    mtr_clearance   = 6
    price           = 610000
    percentage      = 1.06

    # def calc_value(self, free_space):
    #     self.free_space = xxxx
    #     self.value = self.price + self.price * (self.percentage * self.free_space)

class Coordinates(object):
    """Class definition for coordinates."""
    def __init__(self, x, y, width, length):
        self.lb     = (x, y)
        self.lt     = (x, (y+length))
        self.rt     = ((x+width), (y+length))
        self.rb     = ((x+width), y)

        def coordinates(self):
            return '{}, {}, {}, {}'.format(self.lb, self.lt, self.rt,
                                    self.rb)

class Waterbody(object):
    """Class definition for a waterbody."""
    def __init__(self, x, y, width, length, a, b):
        self.x      = x
        self.y      = y
        self.width  = width
        self.length = length

        def a(self):
            return self.width / 2

        def b(self):
            return self.length / 2
