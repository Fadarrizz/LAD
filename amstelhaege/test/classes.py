class Building(object):

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
        self.coordinates = [(x,y), (x, (y + self.length)), ((x + self.width),
                        (y + self.length)), ((x + self.width), y)]

    def __repr__(self):
        return coordinates

class House(Building):
    """Class definition for a detached house."""
    width           = 8
    length          = 8
    mtr_clearance   = 2
    price           = 285000
    percentage      = 1.04
