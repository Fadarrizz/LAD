from Classes import *
from BuildingGenerator import *
from random import randint

coords = Building.coords

def getCoordinates(bType, name, count):

    xBorder = int(180 - bType.width)
    yBorder = int(160 - bType.length)

    x = randint(0, xBorder)
    x2 = x + bType.width
    y = randint(0, yBorder)
    y2 = y + bType.length

    for i in coords:

        if Building.arr == []:
            print ("empty arr")
            break

        xMIN = i[2]
        xMAX = i[2] + i[1].width

        yMIN = i[3]
        yMAX = i[3] + i[1].length

        while True:

            if (xMIN <= x <= xMAX and yMIN <= y <= yMAX):
                print("LB not right, same as",i[0])
                x = randint(0, xBorder)
                x2 = x + bType.width
                y = randint(0, yBorder)
                y2 = y + bType.length
                print("changing chords")

            if (xMIN <= x <= xMAX and yMIN <= y2 <= yMAX):
                print("LT not right, same as",i[0])
                x = randint(0, xBorder)
                x2 = x + bType.width
                y = randint(0, yBorder)
                y2 = y + bType.length
                print("changing chords")

            if (xMIN <= x2 <= xMAX and yMIN <= y2 <= yMAX):
                print("RT not right, same as",i[0])
                x = randint(0, xBorder)
                x2 = x + bType.width
                y = randint(0, yBorder)
                y2 = y + bType.length
                print("changing chords")

            if (xMIN <= x2 <= xMAX and yMIN <= y <= yMAX):
                print("RB not right, same as",i[0])
                x = randint(0, xBorder)
                x2 = x + bType.width
                y = randint(0, yBorder)
                y2 = y + bType.length
                print("changing chords")


                    # print("({},{})".format(x,y),"are not right, same as",i[0])
                    # x = randint(0, xBorder)
                    # x2 = x + bType.width
                    # y = randint(0, yBorder)
                    # y2 = y + bType.length
                    # print("changing chords")

            else:
                break
    print("All corners OK")
    coords.append((name+str(count),bType,x,y))
    return x, y
