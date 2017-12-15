from functions.helpers import *

def random(amount):
    """Generates buildings with random coordinates"""
    random = BuildingGenerator(BuildingQueue(amount))
    return random
