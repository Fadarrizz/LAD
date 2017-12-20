# course: Heuristieken
# team: LADs
# names: Daniel Walters, Auke Geerts, Leyla Banchaewa
# file: hillclimber.py
# description: This file contains the hillclimber algorithm

from functions.helpers import *
from classes.classes import *
from algorithms import randomfunction

def Hillclimber():
    """Tries to improves the total score by changing coordinates or swap
    two buildings for every iteration"""
    # calculate total score
    oldScore = TotalScore.totalScore()

    # save begin score
    beginScore = oldScore
    newScore = 0

    # amount of iterations
    SIZE = 1000

    for i in range(SIZE):
        # Choose random building from Building.buildingsPlaced
        b1 = Building.buildingsPlaced[RandomBuilding()]
        xy1 = (b1.x, b1.y)
        oldX = b1.x
        oldY = b1.y
        b2 = SecondRandomBuilding(b1)
        xy2 = (b2.x, b2.y)

        # get random boolean for choosing method
        bool = RandomBoolean()
        if bool == 0:
            newScore = ImproveScoreByGeneratingNewCoords(b1, oldScore)
            # if score is not higher, update score
            if CheckScoreImprovement(oldScore, newScore):
                oldScore = newScore
                continue
            # else reset to old coordinates
            b1.x = oldX
            b1.y = oldY

        if bool == 1:
            newScore = ImproveScoreWithSwapping(b1, b2, xy1, xy2, oldScore)
            # if score is higher, update score
            if CheckScoreImprovement(oldScore, newScore):
                oldScore = newScore
                continue
            #
            elif oldScore != newScore:
                SwapCoordinates(b1, b2, xy2, xy1)

        print("new score: ${:,.2f}".format(oldScore))

    # variables for printing
    endScore = oldScore - beginScore
    iterationScore = endScore / SIZE
    print("Improvement on score: ${:,.2f}".format(endScore))
    print("Average improvement per iteration: ${:,.2f}".format(iterationScore))

    return oldScore

def HillclimberTester():
    """Runs the Hillclimber function a given number of times.
    The amount of iterations and a factor have to be given."""
    i = 10
    f = 2

    GetScore = []

    print("starting test")
    while i < 400:
        print("Iteration:",i)
        amount = 60
        random(amount)
        print("Random score: ${:,.2f}".format(TotalScore.totalScore()))
        newScore = Hillclimber(i)
        i *= f
    print("done testing")
