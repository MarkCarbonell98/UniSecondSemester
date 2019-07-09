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


def isBackground(vertex):
    for weight in vertex:
        if weight != 0:
            return False
    return True

def connectedComponents(graph):
    anchors = [n for n in range(len(graph))]
    labels = [0] * len(graph)
    currentLabel = 0
    for vertex in anchors:
        if not labels[vertex]:
            stack = [vertex]
            while len(stack) > 0:
                actualVertex = stack.pop()
                if not labels[vertex]:
                    labels[vertex] = currentLabel
                    anchors[vertex] = vertex
                print(actualVertex, currentLabel)
                for neighbor in graph[actualVertex]:
                    if not labels[neighbor]:
                        stack.append(neighbor)
            currentLabel += 1
    return anchors, labels
    



anchors, labels = connectedComponents(graph)
print(anchors, labels)

'''
for all vertexs in graph
    currentLabel = 0
    if label[v] is None:
        label[v] = currentLabel
        fuhre DFS mit start v und aus, und setze fur alle besuchte Knoten der label, currentLabel, und anchor[v'] = v (parent node of all visited nodes)
    currentLabel += 1
'''

'''
    Union find

    def findAnchor(node):
        while anchor[node] != node
            a = anchor[node]
        return a

    for vertexs in graph:
        for u in Nachbarn(v) geschnittent mit {u in V: u > v}
            a1 = findAnchor(v)
            a2 = findAnchor(u)
            getting both anchors
            if a1 < a2:
                anchor[a2] = a1
            else:
                anchor[a1] = a2
            if a1 != a2:
                link(a1,a2)


'''
    

