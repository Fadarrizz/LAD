from classes import *
from random import randint

coordsX = []
coordsY = []

def getCoordinates(bType):

    x = randint(0, 180)
    y = randint(0, 160)

    w = bType.width
    l = bType.length

    count = 0

    for i in Building.arr:

        if Building.arr == []:
            count += 1
            print("im counting", count)

        else:
            lbX = bType.LB[0]
            ltX = bType.LT[0]
            rtX = bType.RT[0]
            rbX = bType.RB[0]

            rbY = bType.LB[1]
            ltY = bType.LT[1]
            rtY = bType.RT[0]
            rbY = bType.RB[0]

            corners = []
            corners.append((lbX, ltX))

            for j in coordsX:
                x1 = j[0]
                x2 = j[1]

                for k in coordsY:
                    y1 = k[0]
                    y2 = k[1]

                    while True:
                        if (x1 <= x <= x2):
                            correct = 1
                            print("x is not right")

                            if (y1 <= y <= y2):
                                print("y is not right")
                                correct = 1
                            else:
                                correct = 0
                                break
                        else:
                            correct = 0
                            break
                    #      and (((x + bType.width) >= x1)
                    # and ((x + bType.width) <= x2)) and (((y + bType.length) >= y1)
                    # and ((y + bType.length) <= y2))):

                        if (correct == 1):
                            x = randint(0, 180)
                            y = randint(0, 180)
                            print("new coords chosen ", x, y)

                    # while (((x1 <= x <= x2) and (y1 <= y <= y2)) and (((x + bType.width) >= x1)
                    # and ((x + bType.width) <= x2)) and (((y + bType.length) >= y1)
                    # and ((y + bType.length) <= y2))):
                    #     print ("in while statement")
                    #     x = randint(0, 180)
                    #     y = randint(0, 180)
                    #     print("changed: ", x, y)

    coordsX.append((x, (x + bType.width)))
    coordsY.append((y, (y + bType.length)))
    return x, y
