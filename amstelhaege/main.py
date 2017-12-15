# course: Heuristieken
# team: LADs
# names: Daniel Walters, Auke Geerts, Leyla Banchaewa
# file: helpers.py
# description: This file contains a program that can generate three variants of
# a housingplan with 20, 40 or 60 houses and water. The housingplan is
# visualized in a figure on a grid, which also shows a total score of the
# calculated total value of all the houses.

# import matplotlib.pyplot as plt
# import matplotlib.patches as patches
# import matplotlib.ticker as plticker
from algorithms.randomfunction import *
import classes
from helpers import *
from algorithms.hillclimber import Hillclimber
from algorithms.simulatedannealing import SimulatedAnnealing

def main():
    amount = Amount()

    Grid(random(amount), Variant(Amount), amount, classes.TotalScore.totalScore())
    # Show map
    plt.show()

    # newScore = Hillclimber()

    newScore = SimulatedAnnealing()

    Grid(classes.Building.buildingsPlaced, Variant(Amount), amount, newScore)
    # Show map
    plt.show()

if __name__ == "__main__":
    main()
