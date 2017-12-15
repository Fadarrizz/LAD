
# course: Heuristieken
# team: LADs
# names: Daniel Walters, Auke Geerts, Leyla Banchaewa
# file: simulatedannealing.py
# description: This file contains all helper functions.

import classes
import helpers
import random

def SimulatedAnnealing():
    # backup buildings array
    helpers.ArrayBackup(classes.Building.buildingsPlaced)

    # Calculate total score
    oldScore = classes.TotalScore.totalScore()

    #define newScore
    newScore = 0

    # define iterations
    SIZE = 100

    # define initial temperature and minimal temperature
    c = 1
    c_min = 0.00001

    # define alpha, de cooling factor
    a = 0.9

    # define acceptance probility
    ap = (newScore - oldScore / c)

    print("starting Hillclimber")
    while c > c_min:
        for i in range(SIZE):
            print("in for")
            # Choose random building from Building.buildingsPlaced
            building = classes.Building.buildingsPlaced[helpers.RandomBuilding()]
            xOld = building.x
            yOld = building.y

            newCoords = helpers.GetCoordinates(building.name, building)

            building.x = newCoords[0]
            building.y = newCoords[1]
            print("coords changed:",newCoords[0],newCoords[1])

            if (helpers.ScoreComparison(oldScore, newScore) == False):

                # Calculate total score
                newScore = classes.TotalScore.totalScore()
                print("New score:", newScore)
            # if helpers.ScoreComparison(oldScore, newScore):
            #     building.x = xOld
            #     building.y = yOld
            #     print("coords reset")
            #     continue
            #     print("New score:", newScore)

            elif(ap < random.random()):
                # Calcualte total score
                newScore = classes.TotalScore.totalScore()
                print("New score:", newScore)
            # Decrease temperature
            c = c * a

        return newScore
