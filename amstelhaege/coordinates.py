from Classes import *
from BuildingGenerator import *
from random import randint
import copy

coords          = Grid.coords
buildingsPlaced = Grid.buildingsPlaced

def getCoordinates(bType, name, count):

    xBorder = int(100 - bType.width)
    yBorder = int(100 - bType.length)

    x  = copy.copy(randint(0, xBorder))
    x2 = x + bType.width
    y  = copy.copy(randint(0, yBorder))
    y2 = y + bType.length

    count = 0

    newCoor = [0,0]

    i = 0

    trigger = True

        while trigger == True:

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

        newCoor[0] = x
        newCoor[1] = y
        print('final coor:', newCoor)
    print("checked all",count,"builings")
    coords.append((name+str(count),bType,x,y))
    return newCoor
