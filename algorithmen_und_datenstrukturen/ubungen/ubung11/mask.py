from pgm import readPGM, writePGM
width, height, data = readPGM("cells.pgm")

# Aufgabe 1
backgroundThreshold = 60
def createMastk(width, height, data, threshold):
    mask = [0]*len(data)
    for x in range(width):
        for y in range(height):
            if data[x + y*width] >= threshold: 
                mask[x+y*width] = data[x + y * width]
    return mask

mask = createMastk(width, height, data, backgroundThreshold)
# writePGM(width, height, mask, "mask.pgm")


def createGraph(width, height, mask):
    adjacencyList = []
    leftPixel = 0
    rightPixel = 0
    lowerPixel = 0
    upperPixel = 0
    currentPixel = 0

    for x in range(width):
        for y in range(height):
            currentPixel = mask[x + y * width]
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
                newVertex.append(lowerPixel)
                newVertex.append(rightPixel)
            elif x == 0 and y == height - 1:
                newVertex.append(upperPixel)
                newVertex.append(rightPixel)
            elif x == width - 1 and y == 0:
                newVertex.append(lowerPixel)
                newVertex.append(leftPixel)
            elif x == width - 1 and y == height - 1:
                newVertex.append(upperPixel)
                newVertex.append(leftPixel)
            elif x == 0 and y > 0 and y < height-1:
                newVertex.append(upperPixel)
                newVertex.append(lowerPixel)
                newVertex.append(rightPixel)
            elif x == width - 1 and y > 0 and y < height-1:
                newVertex.append(upperPixel)
                newVertex.append(lowerPixel)
                newVertex.append(leftPixel)
            elif x > 0 and x < width - 1 and y == 0:
                newVertex.append(leftPixel)
                newVertex.append(rightPixel)
                newVertex.append(lowerPixel)
            elif x > 0 and x < width - 1 and y == height - 1:
                newVertex.append(leftPixel)
                newVertex.append(rightPixel)
                newVertex.append(upperPixel)
            else:
                newVertex.append(leftPixel)
                newVertex.append(rightPixel)
                newVertex.append(upperPixel)
                newVertex.append(lowerPixel)

            for weight in list(newVertex):
                if weight < backgroundThreshold and currentPixel >= backgroundThreshold or (weight >= backgroundThreshold and  currentPixel < backgroundThreshold):
                    newVertex.remove(weight)
            if len(newVertex):
                adjacencyList.append(newVertex)
    return adjacencyList

graph = createGraph(width, height, mask)

def isBackground(arr):
    for element in arr:
        if element != 0:
            return False
    return True

def connectedComponents(graph):
    anchors = [0] * len(graph) #equivalent to visited
    labels = [0] * len(graph)

    currentLabel = 1
    def visit(node, anchor):
        stack = [node]
        while(len(stack)):
            node = stack.pop(0)
            if not anchors[node] and not isBackground(graph[node]):
                anchors[node] = anchor
                labels[node] = labels[anchor]
                for neighbor in graph[node]:
                    if not anchors[neighbor] and not isBackground(graph[neighbor]):
                        stack.append(neighbor)

    for node in range(len(graph)):
        if not anchors[node] and not isBackground(graph[node]):
            labels[node] = currentLabel
            visit(node, node)
            currentLabel+= 1
    return anchors, labels


anchors, labels = connectedComponents(graph)
print(labels)
# writePGM(width, height, labels, "labeling.pgm")

    

