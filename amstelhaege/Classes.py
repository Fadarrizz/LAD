class PlaceableObject(object):

    """Class definition for a placeable object"""

    def __init__(self, x, y, w, l, a, b):
        self.x = x
        self.y = y
        self.w = w
        self.l = l
        self.a = self.w / 2
        self.b = self.l /2

class Building(PlaceableObject):
    """Class definition for a house construction"""

    # variable for number of houses created
    num_houses = 0

    def __init__(self, x, y, w, l, a, b, meters_clearance, price, percentage):
        super().__init__(x, y, w, l)
        self.meters_clearance = 2
        self.price = 3
        self.percentage = percentage

    # increase by one each time a house of any type is made
    num_houses += 1

    def coordinates(self):
        return '{} {}'.format(self.x, self.y)

class House(Building):
    """Class definition for a detached house."""
    def __init__(self, x, y):
        super().__init__(x, y, w, l, a, b meters_clearance, price, percentage)

    # def calc_value(self, free_space):
    #     self.free_space = xxxx
    #     self.value = self.price + self.price * (self.percentage * self.free_space)

class Bungalow(Building):
    """Class definition for a detached house."""
    def __init__(self, x, y):
        super().__init__(x, y, w, l, a, b, meters_clearance, price, percentage)

    # def calc_value(self, free_space):
    #     self.free_space = xxxx
    #     self.value = self.price + self.price * (self.percentage * self.free_space)

class Maison(Building):
    """Class definition for a detached house."""
    def __init__(self, x, y):
        super().__init__(x, y, w, l, a, b, meters_clearance, price, percentage)

    # def calc_value(self, free_space):
    #     self.free_space = xxxx
    #     self.value = self.price + self.price * (self.percentage * self.free_space)

class Waterbody(PlaceableObject):
    """Class definition for a waterbody."""
    def __init__(self, x, y , w, l, a, b):
        super().__init__(x, y , w, l, a, b)
