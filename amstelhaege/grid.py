import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.ticker as plticker
from Classes import *
from coordinates import getCoordinates

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

# empty array
Building.arr = []

# init temp array
building = []

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

    # Create class object and add to array
    temp = bType(name + str(i), 0, 0)

    # Random coordinates
    xy = getCoordinates(temp)
    print(xy)
    x = xy[0]
    y = xy[1]

    tempName = name + str(i)

    # Create class object and add to array
    temp = bType(name + str(i), x, y)
    Building.arr.append(temp)

    # Temp variable with building information
    temp = patches.Rectangle((x, y), bType.width,
            bType.length, color=color)

    # Additional map values
    rx, ry  = temp.get_xy()
    cx      = rx + temp.get_width()/2.0
    cy      = ry + temp.get_height()/2.0

    # Add building to map
    ax.add_artist(temp)

# Show map
plt.show()
