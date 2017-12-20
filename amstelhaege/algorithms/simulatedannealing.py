# course: Heuristieken
# team: LADs
# names: Daniel Walters, Auke Geerts, Leyla Banchaewa
# file: simulatedannealing.py
# description: This file contains all helper functions.

from classes.classes import *
from functions.helpers import *
from algorithms import randomfunction
import math
import matplotlib.pyplot as plt
import random

def SimulatedAnnealing(count):

    #scores Array
    Scores = TotalScore.Scores

    # Calculate total score
    oldScore = TotalScore.totalScore()

    #save begin score
    beginScore = oldScore

    #define newScore
    newScore = 0

    # define iterations
    SIZE = 1000

    # define initial temperature and minimal temperature
    c = 1
    c_min = 0.000001

    # define alpha, the cooling factor
    a = 0.9

    while c > c_min:
        for i in range(SIZE):

            # Choose random building from Building.buildingsPlaced
            b1 = Building.buildingsPlaced[RandomBuilding()]
            oldX = b1.x
            oldY = b1.y
            ap = (oldScore - newScore) / c
            # generate new coords and calculate new total score
            newScore = ImproveScoreByGeneratingNewCoords(b1, oldScore)
            # if score is not higher, reset to old coordinates
            if CheckScoreImprovement(oldScore, newScore):
                # accept improvement
                oldScore = newScore
            # define acceptance probility

            elif ap > random.random():
                # Calculate total score
                oldScore = newScore
            else:
                b1.x = oldX
                b1.y = oldY

            # Decrease temperature
            c = c * a
            TotalScore.Scores.append(oldScore)
        oldScore = GetHighestScore(TotalScore.Scores)
    # variables for printing
    endScore = oldScore - beginScore
    iterationScore = endScore / SIZE
    with open('SA60.txt', 'a') as f:
        print("iteration:", count, file=f)
        print("Begin score:", beginScore, file=f)
        print("New score", oldScore, file=f)
        print("Improvement on score: ${:,.2f}".format(endScore), file=f)
        print("Average improvement per iteration: ${:,.2f}".format(iterationScore), file=f)
        print("\n", file=f)
    return oldScore
