# choose random building
# choose random coordinates
# check for collision with new coords
# check total score
# 	if not improved, discard coords
# 	else, keep changes
trigger = True

while trigger == True:
    # Choose random building from Building.buildingsPlaced
    building = buildingsPlaced(RandomBuilding())

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

    # Calculate total score
    
