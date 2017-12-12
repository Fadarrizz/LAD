from classes import *
from helpers import *

amount = Amount()

Grid(BuildingGenerator(BuildingQueue(amount)),Variant(amount),amount, TotalScore())

# Show map
plt.show()
