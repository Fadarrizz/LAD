from Classes import *
from BuildingGenerator import *
from random import randint

coords = Building.coords

def getCoordinates(bType, name, count):

    xBorder = int(180 - bType.width)
    yBorder = int(160 - bType.length)

    x = randint(0, xBorder)
    y = randint(0, yBorder)

    for i in coords:

        if Building.arr == []:
            print ("empty arr")
            break

        xMIN = i[2]
        xMAX = i[2] + i[1].width
        # print("x min and max",xMIN, xMAX)

        yMIN = i[3]
        yMAX = i[3] + i[1].length

        while True:

            if (xMIN <= x <= xMAX and yMIN <= y <= yMAX):
                print("are not right, same as",i[0],
                        "at ({},{})".format(x,y))
                x = randint(0, xBorder)
                y = randint(0, yBorder)
                print("changing chords")

            else:
                break

    coords.append((name+str(count),bType,x,y))
    return x, y
