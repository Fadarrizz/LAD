import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.ticker as plticker
from Classes import *
from BuildingGenerator import *

buildingsPlaced = Grid.buildingsPlaced
coords          = Grid.coords

def Grid():
    # Grid initialization
    fig, ax = plt.subplots()
    plt.axis('scaled')
    ax.grid(which='major', axis='both', linestyle='-')
    intervals = 10
    loc = plticker.MultipleLocator(base=intervals)
    ax.xaxis.set_major_locator(loc)
    ax.yaxis.set_major_locator(loc)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    # add water to map
    water = Waterbody(100, 88, 80, 72)

    # Temp variable with building information
    water = patches.Rectangle((water.x, water.y), water.width,
            water.length, color='blue')
    ax.add_artist(water)

    build = buildingGenerator()

    count = 0
    print(buildingsPlaced)

    for i in build:
        print("in for loop")
        # Temp variable with building information
        temp = patches.Rectangle((i.x, i.y), i.width, i.length,
                color=i.color)

        # Add building to map
        ax.add_artist(temp)
        count += 1
        print("added",count,"to map",i.coordinates)
        # Show map

        # var = input()

    plt.show()
Grid()
