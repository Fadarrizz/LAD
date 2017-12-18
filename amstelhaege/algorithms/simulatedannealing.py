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

def SimulatedAnnealing():

    #scores Array
    Scores = TotalScore.Scores

    # Calculate total score
    oldScore = TotalScore.totalScore()

    #save begin score
    beginScore = oldScore

    #define newScore
    newScore = 0

    # define iterations
    SIZE = 200

    # define initial temperature and minimal temperature
    c = 1
    c_min = 0.000001

    # define alpha, de cooling factor
    a = 0.9

    while c > c_min:
        iteration = 1
        for i in range(SIZE):

            # Choose random building from Building.buildingsPlaced
            b1 = Building.buildingsPlaced[RandomBuilding()]
            xy1 = (b1.x, b1.y)
            b2 = SecondRandomBuilding(b1)
            xy2 = (b2.x, b2.y)
            # get random boolean for choosing method
            bool = RandomBoolean()
            if bool == 0:
                newScore = ImproveScoreByGeneratingNewCoords(b1, oldScore)
            if bool == 1:
                newScore = ImproveScoreWithSwapping(b1, b2, xy1, xy2, oldScore)
            # define acceptance probility
            ap = (oldScore - newScore) / c
            if ap > random.random():
                # Calcualte total score
                newScore = TotalScore.totalScore()
            # Decrease temperature
            c = c * a
            oldScore = newScore
            iteration += 1
            TotalScore.Scores.append(oldScore)
        oldScore = GetHighestScore(TotalScore.Scores)
    # variables for printing
    endScore = oldScore - beginScore
    iterationScore = endScore / SIZE
    print("Improvement on score: ${:,.2f}".format(endScore))
    print("Average improvement per iteration: ${:,.2f}".format(iterationScore))
    return oldScore
