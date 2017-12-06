from Classes import *
from random import randint

coordsX = []
coordsY = []

def getCoordinates(bType):

    x = randint(0, 180)
    y = randint(0, 160)

    w = bType.width
    l = bType.length

    print("i dunno where im going")
    count = 0

    for i in Building.arr:
        print ("im in the loop")

        if Building.arr == []:
            count += 1
            print("im counting", count)

        else:
            print("i'm getting the house.lb etc")
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
                print ("in the second loop")
                for k in coordsY:
                    y1 = k[0]
                    y2 = k[1]

                    print ("in the third loop")
                    #
                    # while True:
                    #     if (x1 <= x <= x2):
                    #         correct = 1
                    #     elif (y1 <= y <= y2):
                    #         correct = 1
                    #     else:
                    #         correct = 0
                    #         break
                    # #      and (((x + bType.width) >= x1)
                    # # and ((x + bType.width) <= x2)) and (((y + bType.length) >= y1)
                    # # and ((y + bType.length) <= y2))):
                    #     print ("in while statement")
                    #
                    #     if (correct == 1):
                    #         x = randint(0, 180)
                    #         y = randint(0, 180)


                    while (((x1 <= x <= x2) and (y1 <= y <= y2)) and (((x + bType.width) >= x1)
                    and ((x + bType.width) <= x2)) and (((y + bType.length) >= y1)
                    and ((y + bType.length) <= y2))):
                        print ("in while statement")
                        x = randint(0, 180)
                        y = randint(0, 180)
                        print("changed: ", x, y)

    coordsX.append((x, (x + bType.width)))
    coordsY.append((y, (y + bType.length)))
    return x, y
