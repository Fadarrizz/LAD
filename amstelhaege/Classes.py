class PlaceableObject(object):
    """Class definition for a placeable object"""
    
    def __init__(self, x, y, width, length):
        self.x = x
        self.y = y
        self.width = width
        self.length = length

class Building(PlaceableObject):
    """Class definition for a house construction"""

    def __init__(self, x, y, width, length, meters_clearance, price, percentage):
        super().__init__(x, y, width, length)
        self.meters_clearance = meters_clearance
        self.price = price
        self.percentage = percentage

        self.meters_clearance = meters_clearance

    # variable for number of houses created
    num_houses = 0

    # increase by one each time a house of any type is made
    num_houses += 1

    def coordinates(self):
        return '{} {}'.format(self.x, self.y)


class House(Building):
    """Class definition for a detached house."""
    def __init__(self, x, y):
        super().__init__(x, y, width, length, meters_clearance, price, percentage)

    def calc_value(self, free_space):
        self.free_space = xxxx
        self.value = self.price + self.price * (self.percentage * self.free_space)


class Bungalow(Building):
    """Class definition for a detached house."""
    def __init__(self, x, y):
        super().__init__(x, y, width, length, meters_clearance, price, percentage)

    def calc_value(self, free_space):
        self.free_space = xxxx
        self.value = self.price + self.price * (self.percentage * self.free_space)


class Maison(Building):
    """Class definition for a detached house."""
    def __init__(self, x, y):
        super().__init__(x, y, width, length, meters_clearance, price, percentage)

    def calc_value(self, free_space):
        self.free_space = xxxx
        self.value = self.price + self.price * (self.percentage * self.free_space)

class Waterbody(PlaceableObject):
    """Class definition for a waterbody."""
    def __init__(self, x, y , width, length):
        super().__init__(x, y , width, length)
