import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.ticker as plticker
from random import randint
from classes import *

# Map placement queue
building = []

x = randint(0, 180)
y = randint(0, 160)

# lb = (x, y)
# lt     = (x, (y + 8))
# rt     = ((x + 8), (y + 8))
# rb     = ((x + 8), y)

temp = House('h1', x, y)
building.append(temp.coordinates)
print(building)

tArr = [(1,2), (1,4), (3,5), (5,7)]

s = item[0][0]
print(s)
