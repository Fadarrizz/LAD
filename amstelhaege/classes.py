import helpers

class theGrid (object):
    xMAX = 180
    yMAX = 160

class Building(object):
    """Class definition for a house construction"""
    # __metaclass__ = ABCMeta
    buildingsPlaced = []
    coords          = []
    GetScore        = []
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
    percentage      = 0.03
    color           = '#8ca861'

class Bungalow(Building):
    """Class definition for a detached house."""
    house_type      = 'Bungalow'
    width           = 10
    length          = 7.5
    mtr_clearance   = 3
    price           = 399000
    percentage      = 0.04
    color           = '#E5B181'

class Maison(Building):
    """Class definition for a detached house."""
    house_type      = 'Maison'
    width           = 11
    length          = 10.5
    mtr_clearance   = 6
    price           = 610000
    percentage      = 0.06
    color           = '#DE6B48'

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

#################################################################################

class TotalScore(object):
    def totalScore():
        buildingsPlaced = Building.buildingsPlaced
        score = 0
        # add counter
        count = 0
        # iterate over every house placed
        for thisHouse in buildingsPlaced:
            count += 1

            # coordinates of the x and y ranges of relative house
            x = thisHouse.x
            xMAX = thisHouse.x + thisHouse.width
            y = thisHouse.y
            yMAX = thisHouse.y + thisHouse.length

            distances = helpers.DistanceToNeighbours(x,xMAX,y,yMAX,thisHouse)
            smallestDistance = helpers.GetSmallestDistance(distances)

            thisScore = helpers.GetScore(thisHouse, smallestDistance)
            score += thisScore
            # score = 0
        return score

#################################################################################
