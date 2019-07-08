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


def union(x,y,anchor,rank):
#  find_set ohne Pfadkompression       
    def find_set(x):
        while anchor[x]!=x: #suche bis anchor[x] gleich x ist
            x=anchor[x]
        return x
#  find_set mit Pfadkompression   
    # def find_set(x):
    #     if anchor[x]!=x: #suche bis anchor[x] gleich x ist
    #         anchor[x]=find_set(anchor[x]) # Pfadkompression
    #     return anchor[x]
    
    def link(x,y):
        if rank[x] > rank[y]:
            anchor[y] = x
        else: 
            anchor[x] = y
            if rank[x] == rank[y]:
                rank[y] += 1

    ax= find_set(x)
    ay= find_set(y)
    if ax!=ay:
        link(ax,ay)

def connectedComponents(graph):
    anchor = list(range(len(graph)))  # anchor = [0,1,2,3, ...]
    rank = [0]*len(graph)             # rank = [0,0,0,...]  
    for u in range(len(graph)):       # fuer alle Knoten
        for v in graph[u]:            # fuer alle adjanzenten Knoten/Kanten
            if (v > u):               # Es reicht, wenn jede Kante einmal verarbeitet wird
                union(u,v,anchor,rank)
    return anchor, rank

anchors, labels = connectedComponents(graph)
print(anchors)
print(labels)

writePGM(width, height, labels, "labeling.pgm")

    

