import helpers
import classes

def Hillclimber():
    # backup buildings array
    helpers.ArrayBackup(classes.Building.buildingsPlaced)

    # Calculate total score
    oldScore = classes.TotalScore.totalScore()

    # define iterations
    SIZE = 50

    print("starting Hillclimber")
    for i in range(SIZE):
        print("in for")
        # Choose random building from Building.buildingsPlaced
        building = classes.Building.buildingsPlaced[helpers.RandomBuilding()]
        xOld = building.x
        yOld = building.y

        newCoords = helpers.GetCoordinates(building.name, building)

        building.x = newCoords[0]
        building.y = newCoords[1]
        print("coords changed:",newCoords[0],newCoords[1])

        # Calculate total score
        newScore = classes.TotalScore.totalScore()

        if helpers.ScoreComparison(oldScore, newScore):
            building.x = xOld
            building.y = yOld
            print("coords reset")
            continue
        print("New score:", newScore)
    return newScore
