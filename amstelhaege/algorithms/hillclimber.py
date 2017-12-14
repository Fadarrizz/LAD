# choose random building
# choose random coordinates
# check for collision with new coords
# check total score
# 	if not improved, discard coords
# 	else, keep changes

# backup buildings array
ArrayBackup(buidingsPlaced)

# Calculate total score
oldScore = classes.TotalScore.totalScore()

# define iterations
SIZE = 10

while i < SIZE:
    # Choose random building from Building.buildingsPlaced
    building = buildingsPlaced[RandomBuilding()]
    xOld = building.x
    yOld = building.y

    # Generate new random coordinates
    coords = GenerateCoordinates(building.bType)
    x = coords[0]
    x2 = coords[1]
    y = coords[2]
    y2 = coords[3]

    # Check for collision
    while collision(x, x2, y, y2):
        coords = GenerateCoordinates(building.bType)
        x = coords[0]
        x2 = coords[1]
        y = coords[2]
        y2 = coords[3]

    building.x = x
    building.y = y

    # Calculate total score
    newScore = classes.TotalScore.totalScore()

    if ScoreComparison:
        building.x = xOld
        building.y = yOld
