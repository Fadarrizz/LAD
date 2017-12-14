




    """Checks if there is any collision with the chosen coordinates"""
    for neighbour in buildingsPlaced:
        yMIN = neighbour.y
        xMIN = neighbour.x
        yMAX = yMIN + neighbour.length
        xMAX = xMIN + neighbour.width

        # skip the indicated house
        if (thisBuilding.name == neighbour.name):
            continue
        if Overlap(x, x2, y, y2, xMIN, xMAX, yMIN, yMAX) or \
           CheckFreespaceOverlap(bType, x, y) or \
           WaterOverlap(x, y, x2, y2):
           return True
    return False

def GenerateCoordinates(bType):
    """Generates random coordinates"""
    xBorder = int(cs_Grid.xMAX - bType.width)
    yBorder = int(cs_Grid.yMAX - bType.length)

    x = randint(0, xBorder)
    x2 = x + bType.width
    y = randint(0, yBorder)
    y2 = y + bType.length
    return x, x2, y, y2
>>>>>>> master

def MoveAStep(side, coord, step):
    """Changes coordinate to the desired direction"""
    if side == 'left' or 'down':
        coord -= step
    if side == 'right' or 'up':
        coord += step
    return coord

def UndoStep(side, coord, step):
    """Makes a step in the opposite direction"""
    if side == 'left' or 'down':
        coord += step
    if side == 'right' or 'up':
        coord -= step
    return coord

# call function in main after BuildingGenerator


def GetHighestScore(scores):
    index, score = max(enumerate(scores), key=operator.itemgetter(1))
    return index, score


def GetScoreWithoutBuilding(totalScore, building, x, x2, y, y2):
    """Calculates total score without specific building"""
    distances = DistanceToNeighbours(x,x2,y,y2,building)
    smallestDistance = GetSmallestDistance(distances)
    thisScore = GetScore(building, smallestDistance)
    totalScore += thisScore
    return totalScore

def GetScoreSingleBuilding(totalScore, minusScore):
    """Calculates score of a single building"""
    bScore = totalScore - minusScore
    return bScore
<<<<<<< HEAD
>>>>>>> master
