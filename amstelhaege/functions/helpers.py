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
from algorithms import randomfunction
import operator

################################################################################

def chooseAlgorithm():
    option = int(input("Select option: 1. Hillclimber or 2. Simulated Annealing. \n"))
    algorithm = 0

    while option != 1 and option != 2:
        print("Option invalid, please choose your option by entering 1 or 2.")
        option = int(input("Select option: 1. Hillclimber or 2. Simulated Annealing. \n"))
    return option

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
    plt.xlabel('180 meter')
    plt.ylabel('160 meter')
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
    water = Waterbody(20, 104, 40, 36)
    water2 = Waterbody(120, 104, 40, 36)
    water3 = Waterbody(20, 20, 40, 36)
    water4 = Waterbody(120, 20, 40, 36)


    water = patches.Rectangle((water.x, water.y), water.width,
            water.length, facecolor=Waterbody.color, edgecolor = Waterbody.edgecolor)
    ax.add_artist(water)

    water2 = patches.Rectangle((water2.x, water2.y), water2.width,
            water2.length, facecolor=Waterbody.color, edgecolor = Waterbody.edgecolor)
    ax.add_artist(water2)

    water3 = patches.Rectangle((water3.x, water3.y), water3.width,
            water3.length, facecolor=Waterbody.color, edgecolor = Waterbody.edgecolor)
    ax.add_artist(water3)

    water4 = patches.Rectangle((water4.x, water4.y), water4.width,
            water4.length, facecolor=Waterbody.color, edgecolor = Waterbody.edgecolor)
    ax.add_artist(water4)

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

    # create arrays for counting placed buildings
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
        Building.buildingsPlaced.append(temp)

    # print("Building generation complete")
    return Building.buildingsPlaced

################################################################################

def GetCoordinates(name, bType):
    """"Returns generated coordinates if there isn't any collision"""
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
    """Generates random coordinates within a certain boundary"""
    xBorder = int(theGrid.xMAX - bType.width - bType.mtr_clearance)
    yBorder = int(theGrid.yMAX - bType.length - bType.mtr_clearance)

    x = randint(bType.mtr_clearance, xBorder)
    x2 = x + bType.width
    y = randint(bType.mtr_clearance, yBorder)
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
    """"Checks if there is overlap between two selected buildings"""
    if ((xMIN <= x <= xMAX  or   xMIN <= x2 <= xMAX) or \
        (x <= xMIN <= x2    or   x <= xMAX <= x2)) and \
       ((yMIN <= y <= yMAX  or   yMIN <= y2 <= yMAX) or \
        (y <= yMIN <= y2    or   y <= yMAX <= y2)):
        return True
    return False

################################################################################

def CheckFreespaceOverlap(bType, x, y):
    """Checks for every neighbour if there is freespace overlap"""
    for n in Building.buildingsPlaced:
        if (bType == n):
            pass
        elif FreespaceOverlap(bType, n, x, y) == True:
            return True
    return False

################################################################################

def FreespaceOverlap(bType, n, x, y):
    """Checks if there is any freespace overlap between buildings"""
    # check right side
    if ((x + bType.width + bType.mtr_clearance) < n.x) and \
        ((n.x - n.mtr_clearance) > (x + bType.width)):
        return False
    # check left side
    if (x - bType.mtr_clearance) > (n.x + n.width) and \
        ((n.x + n.width + n.mtr_clearance) < (x)):
        return False
    # check top side
    if ((y + bType.length + bType.mtr_clearance) < n.y) and \
        ((n.y - n.mtr_clearance) > (y + bType.length)):
        return False
    # check bottom side
    if (y - bType.mtr_clearance) > (n.y + n.length) and \
        ((n.y + n.length + n.mtr_clearance) < (y)):
        return False
    return True

################################################################################

def WaterOverlap(x, y, x2, y2):
    """Checks if the given coordinates are wihtin the water boundaries"""
    water = Waterbody(20, 104, 40, 36)
    water2 = Waterbody(120, 104, 40, 36)
    water3 = Waterbody(20, 20, 40, 36)
    water4 = Waterbody(120, 20, 40, 36)

    waterX = water.x
    waterY = water.y
    waterWidth = water.width
    waterLength = water.length

    waterX2 = water2.x
    waterY2 = water2.y
    waterWidth2 = water2.width
    waterLength2 = water2.length

    waterX3 = water3.x
    waterY3 = water3.y
    waterWidth3 = water3.width
    waterLength3 = water3.length

    waterX4 = water4.x
    waterY4 = water4.y
    waterWidth4 = water4.width
    waterLength4 = water4.length

    # check if coordinates aren't lying in waterbody
    if (waterX < x < (waterX + waterWidth) or \
        waterX < x2 < (waterX + waterWidth)) and \
        (waterY < y < (waterY + waterLength) or \
        waterY < y2 < (waterY + waterLength)) or (waterX2 < x < (waterX2 + waterWidth2) or \
        waterX2 < x2 < (waterX2 + waterWidth2)) and \
        (waterY2 < y < (waterY2 + waterLength2) or \
        waterY2 < y2 < (waterY2 + waterLength2)) or (waterX3 < x < (waterX3 + waterWidth3) or \
        waterX3 < x2 < (waterX3 + waterWidth3)) and \
        (waterY3 < y < (waterY3 + waterLength3) or \
        waterY3 < y2 < (waterY3 + waterLength3)) or (waterX4 < x < (waterX4 + waterWidth4) or \
        waterX4 < x2 < (waterX4 + waterWidth4)) and \
        (waterY4 < y < (waterY4 + waterLength4) or \
        waterY4 < y2 < (waterY4 + waterLength4)):

        return True
    return False

################################################################################

def DistanceToNeighbours(x, xMAX, y, yMAX, thisHouse):
    """Retrieves the freemeters between a building and its neighbour and adds it
    to an array"""
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
            if Freemeters(y,yMAX,x,xMAX,nY,nX,nL,nW) == 0:
                freeMeters = FreemetersLeftOrRight(x,xMAX,nX,nW)
            elif Freemeters(y,yMAX,x,xMAX,nY,nX,nL,nW) == 1:
                freeMeters = FreemetersUpOrDown(y,yMAX,nY,nL)
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
    """Checks at which side a neighbour lies"""
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
    """Calculates the amount of freemeters for that lies left or right from the
    selected building"""
    #neighbour on right side
    if (xMAX < nX):
        freeMeters = nX - xMAX
        return freeMeters
    #neighbour on left side
    elif(x > (nX + nW)):
        freeMeters = x - (nX + nW)
        return freeMeters

################################################################################

def FreemetersUpOrDown(y,yMAX,nY,nL):
    """Calculates the amount of freemeters for that lies above or under the
    selected building"""
    #neighbour on top
    if (yMAX < nY):
        freeMeters = nY - yMAX
        return freeMeters
    #neighbour bottom
    elif (y > (nY + nL)):
        freeMeters = y - (nY + nL)
        return freeMeters

################################################################################

def FreemetersDiagonal(y, nY,nL):
    """Returns a boolean for the side a diagonally-lying neighbour lies in:
    above or under"""
    if (y > (nY + nL)):
        return 0
    if (y < (nY + nL)):
        return 1

################################################################################

def FreemetersDiagonalBottom(y, x, nY,nL,nX,nW,yMAX,xMAX):
    """Calculates the amount of freemeters between a building an its at the
    bottom diagonally-lying neighbour"""
    #diagonal check bottom left
    if (x > (nX + nW)):
        a = x - (nX + nW)
        b = y - (nY + nL)
        cSquare = (a**2) + (b**2)
        freeMeters = math.sqrt(cSquare)
        return freeMeters
    #diagonal check bottom right
    if (xMAX < nX):
        a = xMAX - nX
        b = yMAX - nY
        cSquare = (a**2) + (b**2)
        freeMeters = math.sqrt(cSquare)
        return freeMeters

################################################################################

def FreemetersDiagonalTop(y, x, nY,nL,nX,nW,yMAX,xMAX):
    """Calculates the amount of freemeters between a building an its at the top
    diagonally-lying neighbour"""
    #diagonal check top left
    if (x > (nX + nW)):
        a = x + (nX + nW)
        b = y + (nY + nL)
        cSquare = (a**2) + (b**2)
        freeMeters = math.sqrt(cSquare)
        return freeMeters
    #diagonal check top right
    if (xMAX < nX):
        a = xMAX + nX
        b = yMAX + nY
        cSquare = (a**2) + (b**2)
        freeMeters = math.sqrt(cSquare)
        return freeMeters

################################################################################

def GetSmallestDistance(distances):
    smallestDistance = min(float(distance) for distance in distances)
    return smallestDistance

################################################################################

def GetScore(bType, smallestDistance):
    """Calculates the score for a single building"""
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

# def ScoreImprover(SIZE, oldScore):
#     """Tries to improve the score by selecting a method randomly for every
#     iteration"""

################################################################################

def ImproveScoreByGeneratingNewCoords(b1, oldScore):
    """Tries to improve the total score by generating new coordinates for a
    single building"""
    oldX = b1.x
    oldY = b1.y
    # get new coords
    newCoords = GetCoordinates(b1.name, b1)

    # apply new coords
    b1.x = newCoords[0]
    b1.y = newCoords[1]

    # Calculate total score
    newScore = TotalScore.totalScore()

    # if score is not higher, reset to old coordinates
    if ScoreComparison(oldScore, newScore):
        b1.x = oldX
        b1.y = oldY
    # else update score
    else:
        oldScore = newScore
    return oldScore

################################################################################

def ImproveScoreWithSwapping(b1, b2, xy1, xy2, oldScore):
    """Tries to improve the total score by swapping buildings"""
    swap = SwapCoordinates(b1, b2, xy1, xy2)
    if swap == False:
        return oldScore
    b1XY = swap[0]
    b2XY = swap[1]

    # Calculate total score
    newScore = TotalScore.totalScore()
    # if score is not higher, swap coords back to original
    if ScoreComparison(oldScore, newScore):
        SwapCoordinates(b1, b2, xy2, xy1)
    # else update score
    else:
        oldScore = newScore
    return oldScore

################################################################################

def RandomBoolean():
    """Return a random boolean"""
    bool = randint(0,2)
    return bool

################################################################################

def SecondRandomBuilding(b1):
    """Randomly selects building and checks if not the same as b1"""
    b2 = Building.buildingsPlaced[(RandomBuilding())]
    while b2 == b1:
        b2 = Building.buildingsPlaced[(RandomBuilding())]
    return b2

################################################################################

def SwapCoordinates(b1, b2, xy1, xy2):
    """Swaps coordinates of two buildings"""
    b1.x = xy2[0]
    b1.y = xy2[1]
    b2.x = xy1[0]
    b2.y = xy1[1]
    if collision(b1.name, b1, b1.x, b1.y, b2.x, b2.y) or \
          collision(b2.name, b2, b2.x, b2.y, b1.x, b1.y):
          b1.x = xy1[0]
          b1.y = xy1[1]
          b2.x = xy2[0]
          b2.y = xy2[1]
          return False
    return b1, b2

################################################################################

def GetHighestScore(scores):
    index, score = max(enumerate(scores), key=operator.itemgetter(1))
    return score

################################################################################
