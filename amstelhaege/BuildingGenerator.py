from Classes import *
from coordinates import getCoordinates
from random import randint

def buildingGenerator():
    print("Starting building generation")
    # empty array
    Building.arr = []
    Building.coords = []

    # init temp array
    building = []

    amount = int(input("How much buildings? (20, 40 or 60) \n"))
    # if not amount == 20 & amount == 40 & amount == 60:
    #     print("Please provide 20, 40 or 60")

    h = int((amount * 0.6))
    b = int((amount * 0.25))
    m = int((amount * 0.15))

    hArr    = ['h'] * h
    bArr    = ['b'] * b
    mArr    = ['m'] * m
    building.extend(hArr+bArr+mArr)

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
        xy = getCoordinates(bType)
        x = xy[0]
        y = xy[1]

        # Create class object and add to array
        temp = bType(name+str(count), x, y)
        print("Created", name+str(count))

        Building.arr.append(temp)

    print("Building generation complete")