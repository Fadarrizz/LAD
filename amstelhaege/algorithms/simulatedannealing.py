# course: Heuristieken
# team: LADs
# names: Daniel Walters, Auke Geerts, Leyla Banchaewa
# file: simulatedannealing.py
# description: This file contains all helper functions.

import classes
import functions.helpers
import random
import math
import matplotlib.pyplot as plt

def SimulatedAnnealing():

    # classes.Builidng.GetScore = []

    # backup buildings array
    functions.helpers.ArrayBackup(classes.classes.Building.buildingsPlaced)

    #scores Array
    Scores = classes.classes.TotalScore.Scores

    # Calculate total score
    oldScore = classes.classes.TotalScore.totalScore()

    #define newScore
    newScore = 0

    # define iterations
    SIZE = 100

    # define initial temperature and minimal temperature
    c = 1
    c_min = 0.00001

    # define alpha, de cooling factor
    a = 0.9

    #define iteration
    iteration = 0

    # define acceptance probility
    ap = math.exp((newScore - oldScore) / c)

    print("starting SimulatedAnnealing")
    while c > c_min:
        iteration +=1
        for i in range(SIZE):
            print("in for")
            # Choose random building from Building.buildingsPlaced
            building = classes.classes.Building.buildingsPlaced[functions.helpers.RandomBuilding()]
            xOld = building.x
            yOld = building.y

            newCoords = functions.helpers.GetCoordinates(building.name, building)

            building.x = newCoords[0]
            building.y = newCoords[1]
            print("coords changed:",newCoords[0],newCoords[1])

            if (functions.helpers.ScoreComparison(oldScore, newScore) == False):

                # Calculate total score
                newScore = classes.classes.TotalScore.totalScore()
                print("New score:", newScore)

            elif(ap > random.random()):
                # Calcualte total score
                newScore = classes.classes.TotalScore.totalScore()
                print("New score:", newScore)
            # Decrease temperature
            c = c * a
            oldScore = newScore
            print("iteration: ", iteration, "\n score: ", oldScore)
            classes.classes.TotalScore.Scores.append(oldScore)
        print (classes.classes.TotalScore.Scores)

        for i in classes.classes.TotalScore.Scores:
            for k in classes.classes.TotalScore.Scores:
                if i > k:
                    newScore = i
                else:
                    newScore = k
        return newScore
