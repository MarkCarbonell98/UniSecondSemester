from pgm import readPGM, writePGM
width, height, data = readPGM("cells.pgm")

# Aufgabe 1
backgroundThreshold = 60
def createMastk(width, height, data, threshold):
    for x in range(width):
        for y in range(height):
            if data[x + y*width] < 60: 
                data[x+y*width] = 0
    return data

mask = createMastk(width, height, data, backgroundThreshold)
writePGM(width, height, mask, "mask.pgm")

