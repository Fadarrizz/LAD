import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.ticker as plticker
import math as math
from random import randint
from classes import *

buildingsPlaced = Building.buildingsPlaced
coords          = Building.coords

#################################################################################

def Amount():
    amount = int(input("How many buildings? (20, 40 or 60) \n"))
    # while amount != 20 and amount != 40 and amount != 60:
    #     print("Please provide 20, 40 or 60")
    #     amount = int(input("How many buildings? (20, 40 or 60) \n"))
    return amount

#################################################################################

def Variant(amount):
    if amount == 20:
        variant = "Variant 1"
    elif amount == 40:
        variant = "Variant 2"
    elif amount == 60:
        variant = "Variant 3"
    else:
        variant = "Amstelhaege"
    return variant
#################################################################################

def Grid(build, variant, amount, totalScore):
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
    plt.suptitle(variant)
    plt.title(str(amount) + ' buildings - score: € %.2f ' + str(totalScore))

    water = Waterbody(100, 88, 80, 72)

    water = patches.Rectangle((water.x, water.y), water.width,
            water.length, color=Waterbody.color)
    ax.add_artist(water)

    for i in build:
        # Temp variable with building information
        temp = patches.Rectangle((i.x, i.y), i.width, i.length,
                facecolor=i.color, edgecolor='black')

        # Add building to map
        ax.add_artist(temp)

    # # Show map
    # plt.show()

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

            xMIN = i[2]                 # x coordinate
            xMAX = i[2] + i[1].width    # x coordinate + width
            yMIN = i[3]                 # y coordinate
            yMAX = i[3] + i[1].length   # y coodinate + length

            if Overlap(x, x2, y, y2, xMIN, xMAX, yMIN, yMAX) or \
               CheckFreespaceOverlap(bType, x, y):

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

def BuildingQueue(amount):
    print("Starting building generation")

    # empty array
    buildingsPlaced = []
    coords = []

    # init temp array
    building = []

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

def CheckFreespaceOverlap(a, x, y):
    for b in buildingsPlaced:
        if (a == b):
            pass
        elif FreespaceOverlap(a, b, x, y) == True:
            return True
    return False

#################################################################################

def FreespaceOverlap(a, b, x, y):
    if ((x + a.width + a.mtr_clearance) < b.x) and \
        (b.x - b.mtr_clearance > x + a.width + a.mtr_clearance):
        return False
    if (x - a.mtr_clearance) > (b.x + b.width) and \
        (b.x + b.width + b.mtr_clearance < x - a.mtr_clearance):
        return False
    if ((y + a.length + a.mtr_clearance) < b.y) and \
        (b.y + b.mtr_clearance > y + a.length + a.mtr_clearance):
        return False
    if (y - a.mtr_clearance) > (b.y + b.length) and \
        (b.y + b.length + b.mtr_clearance < y - a.mtr_clearance):
        return False
    return True

#################################################################################

def TotalScore():
    score = 0
    # add counter
    count = 0
    # iterate over every house placed
    for thisHouse in buildingsPlaced:
        count += 1
        print("round: ", count)

        # coordinates of the x and y ranges of relative house
        x = thisHouse.x
        xMAX = thisHouse.x + thisHouse.width
        y = thisHouse.y
        yMAX = thisHouse.y + thisHouse.length
        print(x, xMAX, y, yMAX)

        distances = DistanceToNeighbours(x,xMAX,y,yMAX,thisHouse)
        print(distances)
        smallestDistance = GetSmallestDistance(distances)

        thisScore = GetScore(thisHouse, smallestDistance)
        print(thisScore)
        score += thisScore
        # score = '?'
    return score

#################################################################################

def DistanceToNeighbours(x, xMAX, y, yMAX, thisHouse):

    # empty temp array
    tempArr = []

    for neighbour in buildingsPlaced:
        nY = neighbour.y
        nX = neighbour.x
        nL = neighbour.length
        nW = neighbour.width

        # skip the indicated house
        if (thisHouse.name == neighbour.name):
            pass
        else:
            print("neighbour:", nX, nY, nW, nL)
            if Freemeters(y,yMAX,x,xMAX,nY,nX,nL,nW) == 0:
                freeMeters = FreemetersLeftOrRight(y,yMAX,x,xMAX,nY,nX,nL,nW)
                print("right or left:", freeMeters)
            elif Freemeters(y,yMAX,x,xMAX,nY,nX,nL,nW) == 1:
                freeMeters = FreemetersUpOrDown(y,yMAX,x,xMAX,nY,nX,nL,nW)
                print("top or bottom:", freeMeters)
            else:
                if FreemetersDiagonal(y, nY,nL) == 0:
                    freeMeters = FreemetersDiagonalBottom(y,x,nY,nL,nX,nW,yMAX,xMAX)
                else:
                    freeMeters = FreemetersDiagonalTop(y,x,nY,nL,nX,nW,yMAX,xMAX)
            tempArr.append(freeMeters)
    return tempArr

#################################################################################

def Freemeters(y,yMAX,x,xMAX,nY,nX,nL,nW):
    # left/right check
    if (y <= nY <= yMAX) or \
       (y <= (nY + nL) <= yMAX):
       return 0
    # bottom or top check
    elif (x <= nX <= xMAX) or \
       (x <= (nX + nW) <= xMAX):
       return 1

#################################################################################

def FreemetersLeftOrRight(y,yMAX,x,xMAX,nY,nX,nL,nW):
    #neighbour on right side
    if (xMAX < nX):
        freeMeters = nX - xMAX
        print("right side:", freeMeters)
        return freeMeters
    #neighbour on left side
    elif(x > (nX + nW)):
        freeMeters = x - (nX + nW)
        print("left side:", freeMeters)
        return freeMeters
    else:
        print("should be diagonal")

#################################################################################

def FreemetersUpOrDown(y,yMAX,x,xMAX,nY,nX,nL,nW):
    #neighbour on top
    if (yMAX < nY):
        freeMeters = nY - yMAX
        return freeMeters
    #neighbour bottom
    elif (y > (nY + nL)):
        freeMeters = y - (nY + nL)
        return freeMeters

#################################################################################

def FreemetersDiagonal(y, nY,nL):
    if (y > (nY + nL)):
        return 0
    if (y < (nY + nL)):
        return 1

#################################################################################

def FreemetersDiagonalBottom(y, x, nY,nL,nX,nW,yMAX,xMAX):
    #diagonal check bottom left
    if (x > (nX + nW)):
        a = x - (nX + nW)
        b = y - (nY + nL)
        c_square = (a**2) + (b**2)
        freeMeters = math.sqrt(c_square)
        print("bottom left",freeMeters)
        return freeMeters
    #diagonal check bottom right
    if (xMAX < nX):
        a = xMAX - nX
        b = yMAX - nY
        c_square = (a**2) + (b**2)
        freeMeters = math.sqrt(c_square)
        print("bottom right:",freeMeters)
        return freeMeters

#################################################################################

def FreemetersDiagonalTop(y, x, nY,nL,nX,nW,yMAX,xMAX):
    #diagonal check top left
    if (x > (nX + nW)):
        a = x - (nX + nW)
        b = y - (nY + nL)
        c_square = (a**2) + (b**2)
        freeMeters = math.sqrt(c_square)
        print("top left:",freeMeters)
        return freeMeters
    #diagonal check top right
    if (xMAX < nX):
        a = xMAX - nX
        b = yMAX - nY
        c_square = (a**2) + (b**2)
        freeMeters = math.sqrt(c_square)
        print("top right:",freeMeters)
        return freeMeters

#################################################################################

def GetSmallestDistance(distances):

    smallestDistance = min(float(distance) for distance in distances)
    return smallestDistance

     ###code om voor elke freeMeters te vergelijken of dit de kleinste afstand is in vergelijking tot de rest

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

#################################################################################

def GetScore(bType, smallestDistance):
    value = bType.price + (((smallestDistance - bType.mtr_clearance) * \
            bType.percentage) * bType.price)
    return value
