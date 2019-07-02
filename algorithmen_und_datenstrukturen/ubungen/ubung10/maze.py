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