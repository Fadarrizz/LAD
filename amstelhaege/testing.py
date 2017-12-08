from Classes import *

for b in Building.buildingsPlaced:
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
