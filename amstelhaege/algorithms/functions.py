def collision(thisBuilding, x, x2, y, y2, bType):
    """Checks if there is any collision with the chosen coordinates"""
    for neighbour in buildingsPlaced:
        yMIN = neighbour.y
        xMIN = neighbour.x
        yMAX = yMIN + neighbour.length
        xMAX = xMIN + neighbour.width

        # skip the indicated house
        if (thisBuilding.name == neighbour.name):
            pass
        if Overlap(x, x2, y, y2, xMIN, xMAX, yMIN, yMAX) or \
           CheckFreespaceOverlap(bType, x, y) or \
           WaterOverlap(x, y, x2, y2):
           return True
    return False

def GenerateCoordinates(bType, xBorder, yBorder):
    "Generates random coordinates"
    x = randint(0, xBorder)
    x2 = x + bType.width
    y = randint(0, yBorder)
    y2 = y + bType.length
    return x, x2, y, y2

def MoveAStep(side, coord, step):
    """Changes coordinate to the desired direction"""
    if side == 'left' or 'down':
        coord -= step
    if side == 'right' or 'up':
        coord += step
    return coord
