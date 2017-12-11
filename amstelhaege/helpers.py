import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.ticker as plticker
from random import randint
from classes import *

buildingsPlaced = Building.buildingsPlaced
coords          = Building.coords

def Grid(build):
    """Places requested houses on grid"""

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

    water = Waterbody(100, 88, 80, 72)

    water = patches.Rectangle((water.x, water.y), water.width,
            water.length, color=Waterbody.color)
    ax.add_artist(water)

    count = 0

    print(build)
    for i in build:
        # Temp variable with building information
        temp = patches.Rectangle((i.x, i.y), i.width, i.length,
                facecolor=i.color, edgecolor='black')

        # Add building to map
        ax.add_artist(temp)
        count += 1
        # print("added",count,"to map",i.coordinates)

    # Show map
    plt.show()

#################################################################################

def GetCoordinates(bType, name, count):

    xBorder = int(180 - bType.width)
    yBorder = int(160 - bType.length)

    x  = randint(0, xBorder)
    x2 = x + bType.width
    y  = randint(0, yBorder)
    y2 = y + bType.length

    invalid = True

    while invalid:
        invalid = False
        for i in coords:

            if coords == []:
                print ("empty arr")
                break

            xMIN = i[2]
            xMAX = i[2] + i[1].width
            yMIN = i[3]
            yMAX = i[3] + i[1].length

            # freespace = FreespaceOverlap(bType, x, y)

            if Overlap(x, x2, y, y2, xMIN, xMAX, yMIN, yMAX) or CheckOverlap(bType, x, y) :

                print(x,y,"are not right, same as",i[0],i[2],i[3])
                x = randint(0, xBorder)
                x2 = x + bType.width
                y = randint(0, yBorder)
                y2 = y + bType.length
                print("changing chords")
                invalid = True
                break

    print("checked all",count,"buildings")
    coords.append((name+str(count),bType,x,y))
    return x,y

#################################################################################

def BuildingQueue():
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

#################################################################################

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
        xy = GetCoordinates(bType, name, count)
        x = xy[0]
        y = xy[1]

        # Create class object and add to array
        temp = bType(name+str(count),x,y)
        print("Created", name+str(count),"at", "({},{})".format(x,y))

        buildingsPlaced.append(temp)

    print("Building generation complete")
    return buildingsPlaced

#################################################################################

def GenerateBuildings():
    BuildingGenerator(BuildingQueue())

#################################################################################

def Overlap(x, x2, y, y2, xMIN, xMAX, yMIN, yMAX):

    if ((xMIN <= x <= xMAX  or   xMIN <= x2 <= xMAX
    or   x <= xMIN <= x2    or   x <= xMAX <= x2)
    and
        (yMIN <= y <= yMAX  or   yMIN <= y2 <= yMAX
    or   y <= yMIN <= y2    or   y <= yMAX <= y2)):
        return True

    return False

#################################################################################

def CheckOverlap(a, x, y):
    for b in buildingsPlaced:
        if (a == b):
            pass
        elif FreespaceOverlap(a, b, x, y) == True:
            return True
    return False

#################################################################################

def FreespaceOverlap(a, b, x, y):
    if ((x + a.width + a.mtr_clearance) < b.x) and (b.x - b.mtr_clearance > x + a.width + a.mtr_clearance):
        return False
    if (x - a.mtr_clearance) > (b.x + b.width) and (b.x + b.width + b.mtr_clearance < x - a.mtr_clearance):
        return False
    if ((y + a.length + a.mtr_clearance) < b.y) and (b.y + b.mtr_clearance > y + a.length + a.mtr_clearance):
        return False
    if (y - a.mtr_clearance) > (b.y + b.length) and (b.y + b.length + b.mtr_clearance < y - a.mtr_clearance):
        return False

    return True

#################################################################################

def getNeighbours():
    #empty array of neighbours
    neighbours = Building.neighbours
    free_meters = 0
    # add counter
    count = 0
    # iterate over every house placed
    for this_house in buildingsPlaced:
        count += 1
        neighbours = []
        print("round: ", count)
        for neighbour in buildingsPlaced:
            # coordinates of the x and y ranges of relative house
            x = this_house.x
            xMAX = this_house.x + this_house.width

            y = this_house.y
            yMAX = this_house.y + this_house.length

            # skip the relative house
            if (this_house.name == neighbour.name):
                pass

            else:
                #LB or LT in y-axis range
                if (y <= neighbour.y <= yMAX) or (y <= (neighbour.y + neighbour.length) <= yMAX):
                    #neighbour on right side
                    if (xMAX < neighbour.x):
                        free_meters = neighbour.x - xMAX
                    #neighbour on left side
                    elif(x > (neighbour.x + neighbour.width)):
                        free_meters = x - (neighbour.x + neighbour.width)
                    print("left or right distance:", free_meters)

                elif (x <= neighbour.x <= xMAX) or (x <= neighbour.x + (neighbour.width) <= xMAX):
                    #neighbour on top
                    if (yMAX < neighbour.y):
                        free_meters = neighbour.y - yMAX
                    #neighbour bottom
                    elif (y > (neighbour.y + neighbour.length)):
                        free_meters = x - (neighbour.y + neighbour.length)
                    print("top or bottom distance:", free_meters)

                #diagonal check bottom left
            elif (y > (neighbour.y + neighbour.length)) and (x > (neighbour.x neighbour.width)):
                    a = x - (neighbour.x + neighbour.width)
                    b = y - (neighbour.y + neighbour.length)
                    c_square = (a**2) + (b**2)
                    free_meters = math.sqrt(c_square)
                #diagonal check bottom right
            elif (y > (neighbour.y + neighbour.length)) and (xMAX < neighbour.x):
                    a = x - (neighbour.x + neighbour.width)
                    b = y - (neighbour.y + neighbour.length)
                    c_square = (a**2) + (b**2)
                    free_meters = math.sqrt(c_square)

            #add each neighbouring house with its distance
            neighbours.append((neighbour.house_type, free_meters))
        print(neighbours)


        ###code om voor elke free_meters te vergelijken of dit de kleinste afstand is in vergelijking tot de rest

        # global nearest_house
        # for i, j in enumerate(neighbours):
        #     house = j[0]
        #     distance = j[1]
        #
        #     next_pair = (i+1)
        #     next_house = next_pair[0]
        #     new_distance = (j+1)[1]
        #
        #     if distance > new_distance:
        #         nearest_house = next_house

        print(nearest_house)
