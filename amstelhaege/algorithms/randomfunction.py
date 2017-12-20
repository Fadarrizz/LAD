# course: Heuristieken
# team: LADs
# names: Daniel Walters, Auke Geerts, Leyla Banchaewa
# file: randomfunction.py
# description: This file contains the random algorithm

from functions.helpers import *

def random(amount):
    """Generates buildings with random coordinates"""
    random = BuildingGenerator(BuildingQueue(amount))
    return random
