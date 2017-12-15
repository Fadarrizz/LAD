import helpers
import classes

def Hillclimber():
    # backup buildings array
    helpers.ArrayBackup(classes.Building.buildingsPlaced)

    # Calculate total score
    oldScore = classes.TotalScore.totalScore()
    newScore = 0

    # define iterations
    SIZE = 20

    print("executing Hillclimber...")
    for i in range(SIZE):

        # Choose random building from Building.buildingsPlaced
        building = classes.Building.buildingsPlaced[helpers.RandomBuilding()]
        xOld = building.x
        yOld = building.y

        newCoords = helpers.GetCoordinates(building.name, building)

        building.x = newCoords[0]
        building.y = newCoords[1]
        
        # Calculate total score
        newScore = classes.TotalScore.totalScore()

        # if score is not higher, reset to old coordinates
        if helpers.ScoreComparison(oldScore, newScore):
            building.x = xOld
            building.y = yOld
            continue
        oldScore = newScore
        print("new score:",newScore)
        # print("New score:", newScore)
    print("done!")
    return newScore
