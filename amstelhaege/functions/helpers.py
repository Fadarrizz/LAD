# course: Heuristieken
# team: LADs
# names: Daniel Walters, Auke Geerts, Leyla Banchaewa
# file: helpers.py
# description: This file contains all helper functions.

import math as math
from random import randint
from classes.classes import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.ticker as plticker
import algorithms.randomfunction
import operator

################################################################################

def Amount():
    """Ask user input for amount of houses, i.e. the variant of the houseplan.
    Also returns the amount as an integer.
    """

    amount = int(input("How many buildings? (20, 40 or 60) \n"))

    # keep asking for input until either 20, 40 or 60 is given
    while amount != 20 and amount != 40 and amount != 60:
        print("Amount invalid. Please choose one of the three options.")
        amount = int(input("How many buildings? (20, 40 or 60) \n"))

    return amount

################################################################################

def Variant(amount):
    """Depending on the user input, the houseplan variant is determined."""

    if amount == 20:
        variant = "Variant 1"
    elif amount == 40:
        variant = "Variant 2"
    elif amount == 60:
        variant = "Variant 3"
    else:
        variant = "Amstelhaege"
    return variant

################################################################################

def Grid(build, variant, amount, totalScore):
    """Places the created houses visually on a grid."""

    # Grid initialization
    fig, ax = plt.subplots()
    plt.axis('scaled')
    ax.grid(which='major', axis='both', color ='silver', linestyle='--')
    intervals = 10
    loc = plticker.MultipleLocator(base=intervals)
    ax.xaxis.set_major_locator(loc)
    ax.yaxis.set_major_locator(loc)
    ax.set_xlim(0, theGrid.xMAX)
    ax.set_ylim(0, theGrid.yMAX)
    ax.set_axisbelow(True)
    plt.suptitle(variant + ' - ' + str(amount) + ' buildings')
    plt.title('score: ${:,.2f}'.format(totalScore))

    # static waterbody placement
    water = Waterbody(100, 88, 80, 72)
    water = patches.Rectangle((water.x, water.y), water.width,
            water.length, facecolor=Waterbody.color, edgecolor = Waterbody.edgecolor)
    ax.add_artist(water)

    # iterate over each house in the build array build and place house on grid
    for i in build:
        meters = i.mtr_clearance

        # Temp variable with building information
        temp = patches.Rectangle((i.x, i.y), i.width, i.length,
                facecolor=i.color, edgecolor = 'black')

        clearance =patches.Rectangle(((i.x - i.mtr_clearance), (i.y - i.mtr_clearance)), (i.width + (i.mtr_clearance * 2)), (i.length+(i.mtr_clearance * 2)),
                facecolor=i.color, alpha = 0.4)

        # Add building to visual grid
        ax.add_artist(temp)
        ax.add_artist(clearance)

################################################################################

def BuildingQueue(amount):
    """Generates a list indicating how many houses per type should be built."""

    print("Starting building generation")

    Building.buildingsPlaced = []
    Building.coords = []
    building = []

    h = int((amount * 0.6))
    b = int((amount * 0.25))
    m = int((amount * 0.15))

    # calculate amount of houses per type to build
    hArr    = ['h'] * h
    bArr    = ['b'] * b
    mArr    = ['m'] * m

    # building array is filled with
    building.extend(mArr+bArr+hArr)

    return building

################################################################################

def BuildingGenerator(building):
    """Generates a list of instantiated houses with the corresponding
    coordinates of the bottom-left corner."""

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

        # get random coordinates
        xy = GetCoordinates(name, bType)
        x = xy[0]
        y = xy[1]

        # create class object and add to array
        temp = bType(name+str(count),x,y)
        print("Created", name+str(count),"at", "({},{})".format(x,y))

        Building.buildingsPlaced.append(temp)

    print("Building generation complete")
    return Building.buildingsPlaced

################################################################################

def GetCoordinates(name, bType):
    # Generate random coordinates
    coords = GenerateCoordinates(bType)
    x = coords[0]
    x2 = coords[1]
    y = coords[2]
    y2 = coords[3]

    # Check for collision
    while collision(name, bType, x, x2, y, y2):
        coords = GenerateCoordinates(bType)
        x = coords[0]
        x2 = coords[1]
        y = coords[2]
        y2 = coords[3]

    return x,y

################################################################################

def GenerateCoordinates(bType):
    """Generates random coordinates"""
    xBorder = int(theGrid.xMAX - bType.width)
    yBorder = int(theGrid.yMAX - bType.length)

    x = randint(0, xBorder)
    x2 = x + bType.width
    y = randint(0, yBorder)
    y2 = y + bType.length
    return x, x2, y, y2

################################################################################

def collision(name, bType, x, x2, y, y2):
    """Checks if there is any collision with the chosen coordinates"""
    if Building.buildingsPlaced == []:
        if WaterOverlap(x, y, x2, y2):
            return True

    for neighbour in Building.buildingsPlaced:
        yMIN = neighbour.y
        xMIN = neighbour.x
        yMAX = yMIN + neighbour.length
        xMAX = xMIN + neighbour.width

        # skip the indicated house
        if (name == neighbour.name):
            continue
        # checks for collision
        if Overlap(x, x2, y, y2, xMIN, xMAX, yMIN, yMAX) or \
           CheckFreespaceOverlap(bType, x, y) or \
           WaterOverlap(x, y, x2, y2):
           return True
    return False

################################################################################

def Overlap(x, x2, y, y2, xMIN, xMAX, yMIN, yMAX):
    if ((xMIN <= x <= xMAX  or   xMIN <= x2 <= xMAX) or \
        (x <= xMIN <= x2    or   x <= xMAX <= x2)) and \
       ((yMIN <= y <= yMAX  or   yMIN <= y2 <= yMAX) or \
        (y <= yMIN <= y2    or   y <= yMAX <= y2)):
        return True
    return False

################################################################################

def CheckFreespaceOverlap(bType, x, y):
    for n in Building.buildingsPlaced:
        if (bType == n):
            pass
        elif FreespaceOverlap(bType, n, x, y) == True:
            return True
    return False

################################################################################

def FreespaceOverlap(bType, n, x, y):
    # check right side
    if ((x + bType.width + bType.mtr_clearance) < n.x) and \
        ((n.x - n.mtr_clearance) > (x + bType.width + bType.mtr_clearance)):
        # print('no overlap right side')
        return False
    # check left side
    if (x - bType.mtr_clearance) > (n.x + n.width) and \
        ((n.x + n.width + n.mtr_clearance) < (x - bType.mtr_clearance)):
        # print('no overlap left side')
        return False
    # check top side
    if ((y + bType.length + bType.mtr_clearance) < n.y) and \
        ((n.y - n.mtr_clearance) > (y + bType.length + bType.mtr_clearance)):
        # print('no overlap top side')
        return False
    # check bottom side
    if (y - bType.mtr_clearance) > (n.y + n.length) and \
        ((n.y + n.length + n.mtr_clearance) < (y - bType.mtr_clearance)):
        # print('no overlap bottom side')
        return False
    return True

################################################################################

def WaterOverlap(x, y, x2, y2):
    water = Waterbody(100, 88, 80, 72)
    waterX = water.x
    waterY = water.y
    waterWidth = water.width
    waterLength = water.length

    # check if coordinates aren't lying in waterbody
    if (waterX < x < (waterX + waterWidth) or \
        waterX < x2 < (waterX + waterWidth)) and \
        (waterY < y < (waterY + waterLength) or \
        waterY < y2 < (waterY + waterLength)):
        return True
    return False

################################################################################

def DistanceToNeighbours(x, xMAX, y, yMAX, thisHouse):

    # empty temp array
    tempArr = []

    for neighbour in Building.buildingsPlaced:
        nY = neighbour.y
        nX = neighbour.x
        nL = neighbour.length
        nW = neighbour.width

        # skip the indicated house
        if (thisHouse.name == neighbour.name):
            pass
        else:
            # print("neighbour:", nX, nY, nW, nL)
            if Freemeters(y,yMAX,x,xMAX,nY,nX,nL,nW) == 0:
                freeMeters = FreemetersLeftOrRight(x,xMAX,nX,nW)
                # print("right or left:", freeMeters)
            elif Freemeters(y,yMAX,x,xMAX,nY,nX,nL,nW) == 1:
                freeMeters = FreemetersUpOrDown(y,yMAX,nY,nL)
                # print("top or bottom:", freeMeters)
            else:
                if FreemetersDiagonal(y, nY,nL) == 0:
                    freeMeters = FreemetersDiagonalBottom(y,x,nY,nL,nX,nW, \
                    yMAX, xMAX)
                else:
                    freeMeters = FreemetersDiagonalTop(y,x,nY,nL,nX,nW, \
                    yMAX, xMAX)
            tempArr.append(freeMeters)
    return tempArr

################################################################################

def Freemeters(y,yMAX,x,xMAX,nY,nX,nL,nW):
    # left/right check
    if (y <= nY <= yMAX) or \
       (y <= (nY + nL) <= yMAX):
       return 0
    # bottom/top check
    if (x <= nX <= xMAX) or \
       (x <= (nX + nW) <= xMAX):
       return 1
    # left/right check from neighbour perspective
    if (nY <= y <= (nY + nL)) or \
       (nY <= yMAX <= (nY + nL)):
       return 0
    # bottom/top check from neighbour perspective
    if (nX <= x <= (nX + nW)) or \
       (nX <= xMAX <= (nX + nW)):
       return 1

################################################################################

def FreemetersLeftOrRight(x,xMAX,nX,nW):
    #neighbour on right side
    if (xMAX < nX):
        freeMeters = nX - xMAX
        # print("right side:", freeMeters)
        return freeMeters
    #neighbour on left side
    elif(x > (nX + nW)):
        freeMeters = x - (nX + nW)
        # print("left side:", freeMeters)
        return freeMeters

################################################################################

def FreemetersUpOrDown(y,yMAX,nY,nL):
    #neighbour on top
    if (yMAX < nY):
        freeMeters = nY - yMAX
        # print("top side:", freeMeters)
        return freeMeters
    #neighbour bottom
    elif (y > (nY + nL)):
        freeMeters = y - (nY + nL)
        # print("bottom side:", freeMeters)
        return freeMeters

################################################################################

def FreemetersDiagonal(y, nY,nL):
    if (y > (nY + nL)):
        return 0
    if (y < (nY + nL)):
        return 1

################################################################################

def FreemetersDiagonalBottom(y, x, nY,nL,nX,nW,yMAX,xMAX):
    #diagonal check bottom left
    if (x > (nX + nW)):
        a = x - (nX + nW)
        b = y - (nY + nL)
        cSquare = (a**2) + (b**2)
        freeMeters = math.sqrt(cSquare)
        # print("bottom left",freeMeters)
        return freeMeters
    #diagonal check bottom right
    if (xMAX < nX):
        a = xMAX - nX
        b = yMAX - nY
        cSquare = (a**2) + (b**2)
        freeMeters = math.sqrt(cSquare)
        # print("bottom right:",freeMeters)
        return freeMeters

################################################################################

def FreemetersDiagonalTop(y, x, nY,nL,nX,nW,yMAX,xMAX):
    #diagonal check top left
    if (x > (nX + nW)):
        a = x + (nX + nW)
        b = y + (nY + nL)
        cSquare = (a**2) + (b**2)
        freeMeters = math.sqrt(cSquare)
        # print("top left:",freeMeters)
        return freeMeters
    #diagonal check top right
    if (xMAX < nX):
        a = xMAX + nX
        b = yMAX + nY
        cSquare = (a**2) + (b**2)
        freeMeters = math.sqrt(cSquare)
        # print("top right:",freeMeters)
        return freeMeters

################################################################################

def GetSmallestDistance(distances):

    smallestDistance = min(float(distance) for distance in distances)
    return smallestDistance

################################################################################

def GetScore(bType, smallestDistance):
    value = bType.price + (((smallestDistance - bType.mtr_clearance) * \
            bType.percentage) * bType.price)
    return value

################################################################################

def ArrayBackup(buildingsPlaced):
    """Makes backup of array"""
    arrBackup = []
    for building in Building.buildingsPlaced:
        arrBackup.append(building)
    print('Backup completed')

################################################################################

def RandomBuilding():
    """Chooses random index for buildingsPlaced"""
    size = len(Building.buildingsPlaced)
    index = randint(0, (size-1))
    return index

################################################################################

def ScoreComparison(oldScore, newScore):
    """Compares old score with new score"""
    if newScore > oldScore:
        return False
    return True

################################################################################
