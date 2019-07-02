# Aufgabe 1a

def dfs(graph, startnode):
    visited = [False]*len(graph)  # Flags, welche Knoten bereits besucht wurden
    
    def visit(node):              # rekursive Hilfsfunktion, die den gegebenen Knoten und dessen Nachbarn besucht
        if not visited[node]:     # Besuche node, wenn er noch nicht besucht wurde
            visited[node] = True  # Markiere node als besucht
            print(node)            # Ausgabe der Knotennummer - pre-order
            for neighbor in graph[node]:   # Besuche rekursiv die Nachbarn
                visit(neighbor)
    
    visit(startnode)

# alg aus der vorlesung... 

graph = [[1], [2,3], [1], [4,5], [3], [3,6,7], [5], [5,8,10], [7,9,10], [8], [7,8, 11], [12,13], [11] ,[11, 14, 15], [13], [13]]

for arr in graph:
    arr.sort(reverse=True)

print("Adjazenzlisten: ", graph)

# dfs(graph, 0)

def way_out(graph, startnode, targetnode):
    visited = [None]*len(graph)
    deadEnds = [None]*len(graph)
    def visit(node):
        isDeadEnd = len(graph[node]) == 1 and node != targetnode and node != startnode
        if deadEnds[node] != None and deadEnds[node].backtrack:
            print(node, "backtracking")
        else:
            print(node)
        if node == targetnode:
            print(targetnode, f"target reached with {12341234}  dead ends")
        if not visited[node]:
            visited[node] = True
            if isDeadEnd:
                deadEnds[node] = {"node": node, "backtrack": graph[node][0]}
                print(node, "dead end")
            for neighbor in graph[node]:
                visit(neighbor)
    visit(startnode)

way_out(graph, 0, 15)
