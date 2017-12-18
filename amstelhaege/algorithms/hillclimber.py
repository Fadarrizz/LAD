from functions.helpers import *
from classes.classes import *
from algorithms import randomfunction

def Hillclimber():
    """Improves the total score by generating new coords"""
    # backup buildings array
    ArrayBackup(Building.buildingsPlaced)

    # calculate total score
    oldScore = TotalScore.totalScore()

    # save begin score
    beginScore = oldScore
    newScore = 0

    # define iterations
    SIZE = 200

    # print("executing Hillclimber...")
    for i in range(SIZE):

        # Choose random building from Building.buildingsPlaced
        building = Building.buildingsPlaced[RandomBuilding()]
        xOld = building.x
        yOld = building.y

        # get new coords
        newCoords = GetCoordinates(building.name, building)

        # apply new coords
        building.x = newCoords[0]
        building.y = newCoords[1]

        # Calculate total score
        newScore = TotalScore.totalScore()

        # if score is not higher, reset to old coordinates
        if ScoreComparison(oldScore, newScore):
            building.x = xOld
            building.y = yOld
            continue
        # update score
        oldScore = newScore
        print("new score: ${:,.2f}".format(oldScore))
    endScore = oldScore - beginScore
    iterationScore = endScore / SIZE
    print("Improvement on score: ${:,.2f}".format(endScore))
    print("Average improvement per iteration: ${:,.2f}".format(iterationScore))
    return oldScore


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
