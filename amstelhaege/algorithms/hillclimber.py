from helpers import *
import classes
from algorithms.randomfunction import *


def Hillclimber(i):
    """Improves the total score by generating new coords"""
    # backup buildings array
    functions.helpers.ArrayBackup(classes.classes.Building.buildingsPlaced)

    # calculate total score
    oldScore = classes.classes.TotalScore.totalScore()

    # save begin score
    beginScore = oldScore
    newScore = 0

    # define iterations
<<<<<<< HEAD
    SIZE = i
=======
    SIZE = 200
>>>>>>> master

    # print("executing Hillclimber...")
    for i in range(SIZE):

        # Choose random building from Building.buildingsPlaced
        building = classes.classes.Building.buildingsPlaced[functions.helpers.RandomBuilding()]
        xOld = building.x
        yOld = building.y

        # get new coords
        newCoords = functions.helpers.GetCoordinates(building.name, building)

        # apply new coords
        building.x = newCoords[0]
        building.y = newCoords[1]

<<<<<<< HEAD
        # Calculate new total score
        newScore = classes.TotalScore.totalScore()
=======
        # Calculate total score
        newScore = classes.classes.TotalScore.totalScore()
>>>>>>> master

        # if score is not higher, reset to old coordinates
        if functions.helpers.ScoreComparison(oldScore, newScore):
            print (oldScore, "is bigger than", newScore)
            building.x = xOld
            building.y = yOld
            continue
        # update score
        oldScore = newScore
<<<<<<< HEAD

    # print test results
    print("new score: ${:,.2f}".format(newScore))
    endScore = newScore - beginScore
    iterationScore = endScore / SIZE
    print("Improvement on score: ${:,.2f}".format(endScore))
    print("Average improvement per iteration: ${:,.2f}".format(iterationScore))
    return newScore

def HillclimberTester():
    """Runs the Hillclimber function a given number of times.
    The amount of iterations and a factor have to given."""
    i = 10
    f = 2

    GetScore = []

    print("starting test")
    while i < 400:
        print("Iteration:",i)
        amount = 60
        random(amount)
        print("Random score: ${:,.2f}".format(classes.TotalScore.totalScore()))
        newScore = Hillclimber(i)
        i *= f
    print("done testing")
=======
        print("new score:",oldScore)
        # print("New score:", newScore)
    print("done!")
    return oldScore
>>>>>>> master
