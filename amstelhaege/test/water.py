
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.ticker as plticker
from random import randint
from classes import *

waterPlaced = Building.waterPlaced
def makegrid(water):

    # Grid initialization
    fig, ax = plt.subplots()
    plt.axis('scaled')
    ax.grid(which='major', axis='both', color ='gray', linestyle='--')
    intervals = 10

    loc = plticker.MultipleLocator(base=intervals)
    ax.xaxis.set_major_locator(loc)
    ax.yaxis.set_major_locator(loc)
    ax.set_xlim(0, 180)
    ax.set_ylim(0, 160)
    ax.set_axisbelow(True)

    for i in water:
            temp = patches.Rectangle((i.x, i.y), i.width,
            i.length, color=Waterbody.color)
            ax.add_artist(water)

    # Show map
    plt.show()

def getWater():
    water = []
    print ("got get water")
    countW = 0

    for i in range (4):
        name    = 'W'
        bType   = Waterbody
        countW  += 1

        # Random coordinates
        # xy = GetCoordinates(bType, name, countW)
        # x = xy[0]
        # y = xy[1]

        if i == 0:
            x = 0
            y = 0

        elif i == 1:
            x = 0
            y = 124

        elif i == 2:
            x = 140
            y = 124

        else:
            x = 114
            y = 0

        # Create class object and add to array
        temp_water = bType(name+str(countW),x,y)
        print("Created", name+str(countW),"at", "({},{})".format(x,y))

        waterPlaced.append(temp_water)

    waterplaced = waterPlaced
    print("Building generation complete")
    print (waterPlaced)
    return waterPlaced

makegrid(getWater)
