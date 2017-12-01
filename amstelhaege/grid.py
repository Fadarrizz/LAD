import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.ticker as plticker
import csv
import sys
from random import randint
from Classes import *

# Grid initialization
fig, ax = plt.subplots()
plt.axis('scaled')
ax.grid(which='major', axis='both', linestyle='-')
intervals = 10
loc = plticker.MultipleLocator(base=intervals)
ax.xaxis.set_major_locator(loc)
ax.yaxis.set_major_locator(loc)
ax.set_xlim(0, 180)
ax.set_ylim(0, 160)

#
building = []
coords = []

amount = int(input("How much buildings? (20, 40 or 60) \n"))
if not amount == 20 & amount == 40 & amount == 60:
    print("Please provide 20, 40 or 60")

h = int((amount * 0.6))
b = int((amount * 0.25))
m = int((amount * 0.15))

hArr    = ['h'] * h
bArr    = ['b'] * b
mArr    = ['m'] * m
building.extend(hArr+bArr+mArr)

print(building)

for i in building:
    if i == 'h':
        name    = 'H'
        bType   = House
        color   = 'green'

    elif i == 'b':
        name    = 'B'
        bType   = Bungalow
        color   = 'purple'

    elif i == 'm':
        name    = 'M'
        bType   = Maison
        color   = 'red'

    # Random coordinates
    x = randint(0, 180)
    y = randint(0, 160)

    # Create class object and add to array
    temp = bType(name + str(i), x, y)
    Building.arr.append(temp)

    # Add coordinates to array
    coords.append(temp.coordinates)

    # Temp variable with building information
    temp = patches.Rectangle((x, y), bType.width,
            bType.length, color=color)

    # Additional map values
    rx, ry  = temp.get_xy()
    cx      = rx + temp.get_width()/2.0
    cy      = ry + temp.get_height()/2.0

    # Add building to map
    ax.add_artist(temp)

for i in hArr:
    print(House.x)

# Show map
plt.show()

# def place_checker(x, y):
#     for coord in coords:
#         if x > item for item in a if item[0] ]
#         for item in a:
#             if x > item[0] and x < (item[0]
#
#         if x > item[0
