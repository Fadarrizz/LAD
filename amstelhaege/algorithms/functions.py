





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
