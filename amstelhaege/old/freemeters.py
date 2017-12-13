def getNeighbours():
    #empty array of neighbours
    neighbours = Building.neighbours
    free_meters = 0
    # add counter
    count = 0
    # iterate over every house placed
    for this_house in buildingsPlaced:
        count += 1
        neighbours = []
        print("round: ", count)

        # coordinates of the x and y ranges of relative house
        x = this_house.x
        xMAX = this_house.x + this_house.width
        y = this_house.y
        yMAX = this_house.y + this_house.length

        print(Neighbours(x, xMAX, y, yMAX, neighbours, this_house))

#################################################################################

def Neighbours(x, xMAX, y, yMAX, neighbours, this_house):

    for neighbour in buildingsPlaced:
        nY = neighbour.y
        nX = neighbour.x
        nL = neighbour.length
        nW = neighbour.width

        # skip the relative house
        if (this_house.name == neighbour.name):
            pass
        else:
            if Freemeters(y,yMAX,x,xMAX,nY,nX,nL,nW):
                free_meters = FreemetersUpOrDown(y,yMAX,x,xMAX,nY,nX,nL,nW)
                print("top or bottom distance:", free_meters)
            elif Freemeters(y,yMAX,x,xMAX,nY,nX,nL,nW) == False:
                free_meters = FreemetersLeftOrRight(y,yMAX,x,xMAX,nY,nX,nL,nW)
                print("left or right distance:", free_meters)
            else:
                free_meters = FreemetersDiagonal(nY,nL,nX,nW,xMAX)

            #add each neighbouring house with its distance
            neighbours.append((neighbour.house_type, free_meters))
            return(neighbours)

#################################################################################

def Freemeters(y,yMAX,x,xMAX,nY,nX,nL,nW):
    if (y <= nY <= yMAX) or \
       (y <= (nY + nL) <= yMAX):
       return True
    if (x <= nX <= xMAX) or \
       (x <= (nX + nW) <= xMAX):
       return False

#################################################################################

def FreemetersLeftOrRight(y,yMAX,x,xMAX,nY,nX,nL,nW):
    #neighbour on right side
    if (xMAX < nX):
        free_meters = nX - xMAX
        return free_meters
    #neighbour on left side
    elif(x > (nX + nW)):
        free_meters = x - (nX + nW)
        return free_meters

#################################################################################

def FreemetersUpOrDown(y,yMAX,x,xMAX,nY,nX,nL,nW):
    #neighbour on top
    if (yMAX < nY):
        free_meters = nY - yMAX
        return free_meters
    #neighbour bottom
    elif (y > (nY + nL)):
        free_meters = x - (nY + nL)
        return free_meters

#################################################################################

def FreemetersDiagonal(nY,nL,nX,nW,xMAX):
    #diagonal check bottom left
    if (y > (nY + nL)) and (x > (nX + nW)):
            a = x - (nX + nW)
            b = y - (nY + nL)
            c_square = (a**2) + (b**2)
            free_meters = math.sqrt(c_square)
            return free_meters
    #diagonal check bottom right
    if (y > (nY + nL)) and (xMAX < nX):
            a = x - (nX + nW)
            b = y - (nY + nL)
            c_square = (a**2) + (b**2)
            free_meters = math.sqrt(c_square)
            return free_meters
