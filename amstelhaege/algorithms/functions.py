<<<<<<< HEAD
import operator

def collision(thisBuilding, x, x2, y, y2):
=======
def collision(thisBuilding, x, x2, y, y2, bType):
>>>>>>> 53cdb9afa5db10c01734fc1d6f6ee179459c73a8
    """Checks if there is any collision with the chosen coordinates"""
    for neighbour in buildingsPlaced:
        yMIN = neighbour.y
        xMIN = neighbour.x
        yMAX = yMIN + neighbour.length
        xMAX = xMIN + neighbour.width

        # skip the indicated house
        if (thisBuilding.name == neighbour.name):
<<<<<<< HEAD
            continue
=======
            pass
>>>>>>> 53cdb9afa5db10c01734fc1d6f6ee179459c73a8
        if Overlap(x, x2, y, y2, xMIN, xMAX, yMIN, yMAX) or \
           CheckFreespaceOverlap(bType, x, y) or \
           WaterOverlap(x, y, x2, y2):
           return True
    return False

<<<<<<< HEAD
def GenerateCoordinates(bType):
    """Generates random coordinates"""
    xBorder = int(cs_Grid.xMAX - bType.width)
    yBorder = int(cs_Grid.yMAX - bType.length)

=======
def GenerateCoordinates(bType, xBorder, yBorder):
>>>>>>> 53cdb9afa5db10c01734fc1d6f6ee179459c73a8
    x = randint(0, xBorder)
    x2 = x + bType.width
    y = randint(0, yBorder)
    y2 = y + bType.length
    return x, x2, y, y2

def MoveAStep(side, coord, step):
<<<<<<< HEAD
    """Changes coordinate to the desired direction"""
=======
>>>>>>> 53cdb9afa5db10c01734fc1d6f6ee179459c73a8
    if side == 'left' or 'down':
        coord -= step
    if side == 'right' or 'up':
        coord += step
    return coord
<<<<<<< HEAD

def UndoStep(side, coord, step):
    """Makes a step in the opposite direction"""
    if side == 'left' or 'down':
        coord += step
    if side == 'right' or 'up':
        coord -= step
    return coord

# call function in main after BuildingGenerator
def ArrayBackup(buildingsPlaced):
    """Makes backup of array"""
    # add arr to classes!
    arrBackup = []
    for building in buildingsPlaced:
        arrBackup.append(building)
    print('Backup completed')

def GetHighestScore(scores):
    index, score = max(enumerate(scores), key=operator.itemgetter(1))
    return index, score

def RandomBuilding():
    """Chooses random index for buildingsPlaced"""
    size = len(buildingsPlaced)
    index = randint(0, size)
    return index

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

def ScoreComparison(oldScore, newScore):
    if newScore > oldScore:
        return False
    return True
=======
    
>>>>>>> 53cdb9afa5db10c01734fc1d6f6ee179459c73a8
