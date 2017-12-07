from random import randint
from classes import *

coords = [(25, 40), (102, 88), (14, 36)]

xBorder = int(180 - House.width)
yBorder = int(160 - House.length)

x = int(input("give x plz:"))
x2 = x + House.width
y = int(input("give y plz:"))
y2 = y + House.length

for i in coords:

    xMIN = i[0]
    xMAX = i[0] + House.width
    print("xMIN:", xMIN, "xMAX", xMAX)

    yMIN = i[1]
    yMAX = i[1] + House.length
    print("yMIN:", yMIN, "yMAX:", yMAX)

    while True:
        # if ((xMIN <= x <= xMAX and yMIN <= y <= yMAX) or
        #     (xMIN <= x <= xMAX and yMIN <= y2 <= yMAX) or
        #     (xMIN <= x2 <= xMAX and yMIN <= y2 <= yMAX) or
        #     (xMIN <= x2 <= xMAX and yMIN <= y <= yMAX)):

        if ((xMIN < x < xMAX
        or   xMIN < x2 < xMAX
        or   x < xMIN < x2
        or   x < xMAX < x2)
        and
            (yMIN < y < yMAX
        or   yMIN < y2 < yMAX
        or   y < yMIN < y2
        or   y < yMAX < y2)):

            print("coords not right")
            x = randint(0, xBorder)
            x2 = x + House.width
            y = randint(0, yBorder)
            y2 = y + House.length
            print("changing chords")

        else:
            break
    print("checked all",x,y,"are good")
