from classes import *

build = Building.buildingsPlaced
for b in build:
    print(b.x)

# for a in buildingsPlaced:
#     for b in buildingsPlaced:
#
#     if (a.x + a.width + a.mtr_clearance) < b.x:
#         return True
#     if (a.x - a.width - a.mtr_clearance) > (b.x + b.width):
#         return True
#     if (a.y + a.length + a.mtr_clearance) < b.y:
#         return True
#     if (a.y - a.length - a.mtr_clearance) > (b.y + b.length):
#         return True
#     else:
#         return False

    #diagonal check bottom left
elif (y > (neighbour.y + neighbour.length)) and (x > (neighbour.x neighbour.width)):
        a = x - (neighbour.x + neighbour.width)
        b = y - (neighbour.y + neighbour.length)
        c_square = (a**2) + (b**2)
        free_meters = math.sqrt(c_square)
    #diagonal check bottom right
elif (y > (neighbour.y + neighbour.length)) and (xMAX < neighbour.x):
        a = x - (neighbour.x + neighbour.width)
        b = y - (neighbour.y + neighbour.length)
        c_square = (a**2) + (b**2)
        free_meters = math.sqrt(c_square)
