from Classes import *
from random import randint

tempArr  = [];

x = randint(0,180)
y = randint(0,160)

temp = House('H' + '1', Coordinates(x, y, House.width, House.length))
tempArr.append(temp)
