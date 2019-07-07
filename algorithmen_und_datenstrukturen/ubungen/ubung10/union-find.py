size=5
anchor = list(range(size))
rank = [0]*size
print (anchor)
print (rank)
# [0, 1, 2, 3, 4]
# [0, 0, 0, 0, 0]
def union(x,y,anchor,rank):
#  find_set ohne Pfadkompression       
    def find_set(x):
        while anchor[x]!=x: #suche bis anchor[x] gleich x ist
            x=anchor[x]
        return x

#  find_set mit Pfadkompression   
#     def find_set(x):
#         if anchor[x]!=x: #suche bis anchor[x] gleich x ist
#             anchor[x]=find_set(anchor[x]) # Pfadkompression
#         return anchor[x]

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
    
 
union(0,1,anchor,rank)
print (anchor)
print (rank)
[1, 1, 2, 3, 4]
[0, 1, 0, 0, 0]
union(1,2,anchor,rank)
print (anchor)
print (rank)
[1, 1, 1, 3, 4]
[0, 1, 0, 0, 0]
union(3,4,anchor,rank)
print (anchor)
print (rank)
[1, 1, 1, 4, 4]
[0, 1, 0, 0, 1]
union(3,1,anchor,rank)
print (anchor)
print (rank)
[1, 1, 1, 4, 1]
[0, 2, 0, 0, 1]
union(3,1,anchor,rank)
print (anchor)
print (rank)
[1, 1, 1, 4, 1]
[0, 2, 0, 0, 1]
# Zusammenhaengende Komponenten
graph_2k = [[1], [0,2], [1],     [4,6], [3,5], [4], [3]]
graph_1k = [[1], [0,2], [1,3], [2,4,6], [3,5], [4], [3]]

def connectedComponentsUnionFind(graph):
    anchor = list(range(len(graph)))  # anchor = [0,1,2,3, ...]
    rank = [0]*len(graph)             # rank = [0,0,0,...]  
    for u in range(len(graph)):       # fuer alle Knoten
        for v in graph[u]:            # fuer alle adjanzenten Knoten/Kanten
            #if (v > u):               # Es reicht, wenn jede Kante einmal verarbeitet wird
                union(u,v,anchor,rank)
    
    return anchor

connectedComponentsUnionFind(graph_2k)
[1, 1, 1, 4, 4, 4, 4]