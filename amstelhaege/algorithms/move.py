from classes import *

# pak huis
# kies richting
# zet stap
# onthou score in array, undo stap
# herhaal voor alle richtingen
# kijk welke het beste is - TotalScore
# zet beste stap
# herhaal tot niet meer mogelijk
# pak volgend huis

# instantiate list
buildingsPlaced = Building.buildingsPlaced

# define step size
step = 0.5

for thisHouse in buildingsPlaced:

    # step to right
    thisHouse.x += step

    if interference(x, x2, y, y2, xMIN, xMAX, yMIN, yMAX, thisHouse.bType)
