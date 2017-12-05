from Classes import *
from random import randint

coordsX = []
coordsY = []

def getCoordinates(bType):

    x = randint(0, 180)
    y = randint(0, 160)

    w = bType.width
    l = bType.length

    for i in Building.arr:

        if not Building.arr:
            count += 1

        else:

            lbX = bType.LB[0]
            ltX = bType.LT[0]
            rtX = bType.RT[0]
            rbX = bType.RB[0]

            rbY = bType.LB[1]
            ltY = bType.LT[1]
            rtY = bType.RT[0]
            rbY = bType.RB[0]

            for j in coordsX:
                x1 = j[0]
                x2 = j[1]

                for k in coordsY:
                    y1 = k[0]
                    y2 = k[1]

                    while ((x >= x1 and x <= x2) and (y >= y1 and y <= y2))
                    and (((x + bType.width) >= x1) and ((x + bType.width) <= x2)
                    and ((y + bType.length) >= y1) and ((y + bType.length) <= y2)):

                        x = randint(0, 180)
                        y = randint(0, 180)

    coordsX.append((x, (x + bType.width)))
    coordsY.append((y, (y + bType.length)))
    return x, y
