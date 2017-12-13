def interference(x, x2, y, y2, xMIN, xMAX, yMIN, yMAX, bType):
    if Overlap(x, x2, y, y2, xMIN, xMAX, yMIN, yMAX) or \
       CheckFreespaceOverlap(bType, x, y) or \
       WaterOverlap(x, y, x2, y2):
       return True:
    return False

def set():
