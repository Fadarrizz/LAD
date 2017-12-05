import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.ticker as plticker
from random import randint
from classes import *

def getCoordinates():

    x = randint(0, 180)
    y = randint(0, 160)

    for i in Building.arr:

        if not Building.arr:
            count += 1
            print("arr is empty")

        else:
            x1 = (i-1).xs[0]
            x2 = (i-1).xs[1]

            y1 = (i-1).ys[0]
            y2 = (i-1).ys[1]

            while (x >= x1 and x <= x2):
                x = randint(0, 180)

            while (y >= y1 and y <= y2):
                y = randint(0, 160)

    return x, y

coords = getCoordinates();
print(Building.arr)
print(coords)
