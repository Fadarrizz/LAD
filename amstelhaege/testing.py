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

x = [1,2,3]

for i in x:
    if i > 2:
        if i == 3:
            print(i,'= 3')
            pass
        print(i,'> 2')
    else:
        print('lol')
    print('end')
