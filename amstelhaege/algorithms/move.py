from classes import *

def Move():
    # pak huis
    # kies richting
    # zet stap
    # onthou score in array, undo stap
    # herhaal voor alle richtingen
    # kijk welke het beste is - TotalScore
    # zet beste stap
    # herhaal tot niet meer mogelijk
    # pak volgend huis

    # instantiate list
    buildingsPlaced = Building.buildingsPlaced

    # define step size
    step = 0.5

    # total score
    totalScore = TotalScore()

<<<<<<< HEAD


=======
    # array for checking new total scores
    newScores = []

>>>>>>> 53cdb9afa5db10c01734fc1d6f6ee179459c73a8
    for thisBuilding in buildingsPlaced:

        x = thisBuilding.x
        y = thisBuilding.x
        x2 = x + thisBuilding.width
        y2 = y + thisBuilding.length
        bType = thisBuilding.house_type

<<<<<<< HEAD
        while True:
            # array for checking new total scores
            newScores = []
            # array for all sides with
            sides = [('left', x), ('right', x), ('up', y), ('down', y)]
            for side in sides:

                thisBuilding.side[1] = MoveAStep(side[0], side[1], step)
                if collision(thisBuilding, x, x2, y, y2, bType):
                    thisBuilding.side[1] = UndoStep(side[0], side[1], step)
                    continue
                newScores.append(TotalScore())
                thisBuilding.side[1] = UndoStep(side[0], side[1], step)

            highestScore = GetHighestScore(newScores)
=======
        sides = [('left', x), ('right', x), ('up', y), ('down', y)]
        for side in sides:
            side[1] = MoveAStep(side[0], side[1], step)
            if collision(thisBuilding, x, x2, y, y2, bType):
                # undo step (NOT DONE)
                pass
            newScores.append(TotalScore())
            # undo step
>>>>>>> 53cdb9afa5db10c01734fc1d6f6ee179459c73a8

        # TODO:
        # see which score is the best
        # if non: go to next building
        # otherwise, make that step
        # go to next building
