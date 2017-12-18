# course: Heuristieken
# team: LADs
# names: Daniel Walters, Auke Geerts, Leyla Banchaewa
# file: helpers.py
# description: This file contains a program that can generate three variants of
# a housingplan with 20, 40 or 60 houses and water. The housingplan is
# visualized in a figure on a grid, which also shows a total score of the
# calculated total value of all the houses.

from algorithms.randomfunction import random
import classes.classes
from functions.helpers import *
from algorithms.hillclimber import Hillclimber, HillclimberTester
from algorithms.simulatedannealing import SimulatedAnnealing

def main():
    # User input for amount of houses is stored as int in 'amount'
    amount = Amount()

    # User input for selection of algorithm is stored as int in 'option'
    option = chooseAlgorithm()

    # Random selection of house positioning (initial state map)
    Grid(random(amount), Variant(Amount), amount, TotalScore.totalScore())

    # Show map and save map
    plt.savefig('Initial', bbox_inches='tight')
    plt.show()

    # Run algorithm depending on option selected to change house positioning
    if option == 1:
        newScore = Hillclimber()
    elif option == 2:
        newScore = SimulatedAnnealing()

    # Build new map with variations, with hillclimbing or simulated annealing
    Grid(Building.buildingsPlaced, Variant(Amount), amount, newScore)

    plt.savefig('Improved', bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    main()
