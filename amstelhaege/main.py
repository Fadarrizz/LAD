# course: Heuristieken
# team: LADs
# names: Daniel Walters, Auke Geerts, Leyla Banchaewa
# file: main.py
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
    count = 0
    for i in range(20):
        count += 1
        # User input for amount of houses is stored as int in 'amount'
        amount = 60

        # User input for selection of algorithm is stored as int in 'option'
        option = 1

        # Random selection of house positioning (initial state map)
        Grid(random(amount), Variant(Amount), amount, TotalScore.totalScore())
        # print("initialscore",i,":", TotalScore.totalScore(), file=f)
        # Show map
        plt.show()
        # plt.savefig('initial'+str(i), bbox_inches='tight')

        # Run algorithm depending on option selected to change house positioning
        if option == 1:
            newScore = Hillclimber(count)
        elif option == 2:
            newScore = SimulatedAnnealing(count)

        # Build new map with variations, with hillclimbing or simulated annealing
        Grid(Building.buildingsPlaced, Variant(Amount), amount, newScore)
        # print("improvedscore",i,":", newScore, file=f)
        # Show map
        plt.savefig('improved'+str(i), bbox_inches='tight')

if __name__ == "__main__":
    main()
