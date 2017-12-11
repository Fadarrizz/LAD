class Building(object):

    waterPlaced     = []
    coords          = []
    width           = 0
    length          = 0
    mtr_clearance   = 0
    price           = 0
    percentage      = 0

    def __init__(self, name, x, y):
        self.name   = name
        self.x      = x
        self.y      = y
        self.LB = (x,y)
        self.LT = (x, (y + self.length))
        self.RT = ((x + self.width), (y + self.length))
        self.RB = ((x + self.width), y)

    def __repr__(self):
        return coordinates

class Waterbody(object):
    """Class definition for a waterbody."""
    width = 40
    length = 36
    color           = "#7DBBC3"
    # def __init__(self, x, y, width, length):
    #     self.x      = x
    #     self.y      = y
    #     self.width  = width
    #     self.length = length
    #
    #     self.a = self.width / 2
    #     self.b = self.length / 2
