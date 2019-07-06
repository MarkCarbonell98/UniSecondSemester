from pgm import readPGM, writePGM
width, height, data = readPGM("cells.pgm")

def createGraph(width, height, mask):
    adjacencyList = []
    leftPixel = 0
    rightPixel = 0
    lowerPixel = 0
    upperPixel = 0
    for x in range(width):
        for y in range(height):
            newVertex = []
            try:
                leftPixel = mask[(x - 1) + y * width]
            except IndexError:
                leftPixel = 0
            try:
                rightPixel = mask[(x + 1) + y * width]
            except IndexError:
                rightPixel = 0
            try:
                lowerPixel = mask[x + (y - 1) * width]
            except IndexError:
                lowerPixel = 0
            try:
                upperPixel = mask[x + (y + 1) * width]
            except IndexError:
                upperPixel = 0
                
            if x == 0 and y == 0:
                newVertex.append(rightPixel)
                newVertex.append(upperPixel)
            elif x == 0 and y == height - 1:
                newVertex.append(lowerPixel)
                newVertex.append(rightPixel)
            elif x == width - 1 and y == 0:
                newVertex.append(lowerPixel)
                newVertex.append(leftPixel)
            elif x == width -1 and y == height -1:
                newVertex.append(leftPixel)
                newVertex.append(upperPixel)
            elif x == 0 and y > 0 and y < height-1:
                newVertex.append(upperPixel)
                newVertex.append(lowerPixel)
                newVertex.append(rightPixel)
            elif x == width - 1 and y > 0 and y < height-1:
                newVertex.append(upperPixel)
                newVertex.append(lowerPixel)
                newVertex.append(leftPixel)
            elif x > 0 and x < width -1 and y == 0:
                newVertex.append(leftPixel)
                newVertex.append(rightPixel)
                newVertex.append(upperPixel)
            elif x > 0 and x < width -1 and y == height -1:
                newVertex.append(leftPixel)
                newVertex.append(rightPixel)
                newVertex.append(lowerPixel)
            else:
                newVertex.append(leftPixel)
                newVertex.append(rightPixel)
                newVertex.append(upperPixel)
                newVertex.append(lowerPixel)
            adjacencyList.append(newVertex)
    return adjacencyList

graph = createGraph(width, height, data)
print(graph)
