import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.ticker as plticker
from Classes import *
from BuildingGenerator import *

def Grid():
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

    # add water to map
    water = Waterbody(100, 88, 80, 72)

    # Temp variable with building information
    water = patches.Rectangle((water.x, water.y), water.width,
            water.length, color='blue')
    ax.add_artist(water)

    buildingGenerator()

    for i in Building.arr:
        # Temp variable with building information
        temp = patches.Rectangle((i.x, i.y), i.width, i.length,
                color=i.color)

        # Add building to map
        ax.add_artist(temp)

    # Show map
    plt.show()

Grid()
