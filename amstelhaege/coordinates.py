from Classes import *
from BuildingGenerator import *
from random import randint

coords = Building.coords

def getCoordinates(bType):

    xBorder = int(180 - bType.width)
    yBorder = int(160 - bType.length)

    x = randint(0, xBorder)
    y = randint(0, yBorder)

    for i in coords:

        if Building.arr == []:
            print ("empty arr")
            break

        xMIN = i[1]
        xMAX = i[1] + i[0].width

        yMIN = i[2]
        yMAX = i[2] + i[0].length

        while True:

            if (xMIN <= x <= xMAX and yMIN <= y <= yMAX):
                print("x and y are not right")
                x = randint(0, xBorder)
                y = randint(0, yBorder)
                print("changing chords")

            else:
                break

    coords.append((bType,x,y))
    return x, y
