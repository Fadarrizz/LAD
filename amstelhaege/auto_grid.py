import csv
import sys
from Classes import Building, House, Bungalow, Maison, Waterbody

bType = input("What type of building? \n (H, B or M) ")
amount = input("How much buildings? ")

houses = []


if bType == 'h' or 'H':
    name = 'H'
    for i in amount:
        name += str(i)
        houses.append(House('H0', 0, 0))
        print(houses)
