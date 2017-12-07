from Classes import *
from BuildingGenerator import *
from random import randint
import copy

coords          = Grid.coords
buildingsPlaced = Grid.buildingsPlaced

def getCoordinates(bType, name, count):

    xBorder = int(180 - bType.width)
    yBorder = int(160 - bType.length)

    x  = copy.copy(randint(0, xBorder))
    x2 = x + bType.width
    y  = copy.copy(randint(0, yBorder))
    y2 = y + bType.length

    count = 0

    for i in coords:

        if coords == []:
            print ("empty arr")
            break

        xMIN = i[2]
        xMAX = i[2] + i[1].width

        yMIN = i[3]
        yMAX = i[3] + i[1].length

        while True:

            if ((xMIN < x < xMAX
            or   xMIN < x2 < xMAX
            or   x < xMIN < x2
            or   x < xMAX < x2)
            and
                (yMIN < y < yMAX
            or   yMIN < y2 < yMAX
            or   y < yMIN < y2
            or   y < yMAX < y2)):

                print(x,y,"are not right, same as",i[0])
                x = copy.copy(randint(0, xBorder))
                x2 = x + bType.width
                y = copy.copy(randint(0, yBorder))
                y2 = y + bType.length
                print("changing chords")

            else:
                count += 1
                break

    print("checked all",count,"builings")
    coords.append((name+str(count),bType,x,y))
    return x, y
