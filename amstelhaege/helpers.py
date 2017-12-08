import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.ticker as plticker
from random import randint
from Classes import *

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

    buildingsPlaced = Grid.buildingsPlaced
    coords          = Grid.coords

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


def buildingQueue():
    print("Starting building generation")
    # empty array
    buildingsPlaced = []
    coords = []

    # init temp array
    building = []

    amount = int(input("How much buildings? (20, 40 or 60) \n"))
    # if not amount == 20 & amount == 40 & amount == 60:
    #     print("Please provide 20, 40 or 60")

    h = int((amount * 0.6))
    b = int((amount * 0.25))
    m = int((amount * 0.15))

    hArr    = ['h'] * h
    bArr    = ['b'] * b
    mArr    = ['m'] * m
    # building.extend(hArr+bArr+mArr)
    building.extend(mArr+bArr+hArr)
    return building

def BuildingGenerator(building):

    countH = 0
    countB = 0
    countM = 0

    for i in building:
        if i == 'h':
            name    = 'H'
            bType   = House
            countH += 1
            count   = countH

        elif i == 'b':
            name    = 'B'
            bType   = Bungalow
            countB += 1
            count   = countB

        elif i == 'm':
            name    = 'M'
            bType   = Maison
            countM += 1
            count   = countM

        # Random coordinates
        xy = getCoordinates(bType, name, count)
        x = xy[0]
        y = xy[1]

        # Create class object and add to array
        temp = bType(name+str(count),x,y)
        print("Created", name+str(count),"at", "({},{})".format(x,y))

        buildingsPlaced.append(temp)

    print("Building generation complete")
    return buildingsPlaced

def Coordinates(bType, name, count):

    xBorder = int(100 - bType.width)
    yBorder = int(100 - bType.length)

    x  = randint(0, xBorder))
    x2 = x + bType.width
    y  = randint(0, yBorder))
    y2 = y + bType.length

    while True:

        for i in range(len(coords)):

            if coords == []:
                print ("empty arr")
                break

            xMIN = i[2]
            xMAX = i[2] + i[1].width

            yMIN = i[3]
            yMAX = i[3] + i[1].length

            print(xMIN,xMAX,yMIN,yMAX)

            # if ((xMIN <= x or x <= xMAX) and (yMIN <= y or y <= yMAX)):

            if ((xMIN <= x <= xMAX
            or   xMIN <= x2 <= xMAX
            or   x <= xMIN <= x2
            or   x <= xMAX <= x2)
            and
                (yMIN <= y <= yMAX
            or   yMIN <= y2 <= yMAX
            or   y <= yMIN <= y2
            or   y <= yMAX <= y2)):

                print(x,y,"are not right, same as",i[0])
                x = copy.copy(randint(0, xBorder))
                x2 = x + bType.width
                y = copy.copy(randint(0, yBorder))
                y2 = y + bType.length
                print('current coor:',x,y)

                print("changing chords")
                break
        break

print("checked all",count,"builings")
coords.append((name+str(count),bType,x,y))
return x,y
