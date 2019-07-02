def dfs(graph, startnode):
    visited = [False]*len(graph)  # Flags, welche Knoten bereits besucht wurden
    
    def visit(node):              # rekursive Hilfsfunktion, die den gegebenen Knoten und dessen Nachbarn besucht
        if not visited[node]:     # Besuche node, wenn er noch nicht besucht wurde
            visited[node] = True  # Markiere node als besucht
            #print (node)            # Ausgabe der Knotennummer - pre-order
            for neighbor in graph[node]:   # Besuche rekursiv die Nachbarn
                visit(neighbor)
            print (node)            # Ausgabe der Knotennummer - post-order    
    
    visit(startnode)

graph=[[], [2,3], [4,5], [4,6,7], [2, 3], [2], [3], [3]]
dfs(graph, 1)
6
7
3
4
5
2
1
def dfs_info(graph, startnode):
    visited = [False]*len(graph)    # wurde ein Knoten bereits besucht?
    parents = [None]*len(graph)     # registriere für jeden Knoten den Vorgänger im Tiefensuchbaum
    discovery_order = []            # enthält am Ende die pre-order Sortierung
    finishing_order = []            # enthält am Ende die post-order Sortierung
    
    def visit(node, parent):        # rekursive Hilfsfunktion
        if not visited[node]:       # besuche 'node', wenn noch nicht besucht wurde
            visited[node] = True           # markiere 'node' als besucht
            parents[node] = parent         # speichere den Vorgänger von 'node'
            discovery_order.append(node)   # registriere, dass 'node' jetzt entdeckt wurde
            for neighbor in graph[node]:   # besuche rekursiv die Nachbarn ...
                visit(neighbor, node)      #  ... wobei 'node' zu deren Vorgänger wird
            finishing_order.append(node)   # registriere, dass 'node' jetzt fertiggestellt wurde
    
    visit(startnode, None)          # beginne bei 'startnode', der keinen Vorgänger hat
    
    return parents, discovery_order, finishing_order # gib die zusätzliche Informationen zurück

dfs_info(graph,1)
([None, None, 1, 4, 2, 2, 3, 3], [1, 2, 4, 3, 6, 7, 5], [6, 7, 3, 4, 5, 2, 1])
def dfs_info(graph, startnode):
    #visited = [False]*len(graph)   #* wurde ein Knoten bereits besucht?
    parents = [None]*len(graph)     # registriere für jeden Knoten den Vorgänger im Tiefensuchbaum
    discovery_order = []            # enthält am Ende die pre-order Sortierung
    finishing_order = []            # enthält am Ende die post-order Sortierung
    
    def visit(node, parent):        # rekursive Hilfsfunktion
        if parents[node] is None:       #* (== if not visited[node]) besuche 'node', wenn noch nicht besucht wurde 
            #visited[node] = True       #* markiere 'node' als besucht
            parents[node] = parent         # speichere den Vorgänger von 'node'
            discovery_order.append(node)   # registriere, dass 'node' jetzt entdeckt wurde
            for neighbor in graph[node]:   # besuche rekursiv die Nachbarn ...
                visit(neighbor, node)      #  ... wobei 'node' zu deren Vorgänger wird
            finishing_order.append(node)   # registriere, dass 'node' jetzt fertiggestellt wurde
    
    visit(startnode, startnode)          #* beginne bei 'startnode', der sein eigener Vorgänger ist
    
    return parents, discovery_order, finishing_order # gib die zusätzliche Informationen zurück

dfs_info(graph,1)
([None, 1, 1, 4, 2, 2, 3, 3], [1, 2, 4, 3, 6, 7, 5], [6, 7, 3, 4, 5, 2, 1])
from collections import deque

def bfs(graph, startnode):
    parents = [None]*len(graph)            # speichere für jeden Knoten den Vorgänger im Breitensuchbaum
    parents[startnode] = startnode         # Konvention: der Startknoten hat sich selbst als Vorgänger 
  
    q = deque()                            # Queue für die zu besuchenden Knoten
    q.append(startnode)                    # Startknoten in die Queue einfügen
    print(q)
    while len(q) > 0:                      # solange noch Knoten zu bearbeiten sind
        node = q.popleft()                 # Knoten aus der Queue nehmen (first in - first out)
        #print(node,end=', ')                        # den Knoten bearbeiten (hier: Knotennummer drucken)
        print(q)
        for neighbor in graph[node]:       # die Nachbarn expandieren
            if parents[neighbor] is None:  # Nachbar wurde noch nicht besucht
                parents[neighbor] = node   # => Vorgänger merken, Knoten dadurch als "besucht" markieren
                q.append(neighbor)         #    und in die Queue aufnehmen
                print(q)
                
bfs(graph,1)
deque([1])
deque([])
deque([2])
deque([2, 3])
deque([3])
deque([3, 4])
deque([3, 4, 5])
deque([4, 5])
deque([4, 5, 6])
deque([4, 5, 6, 7])
deque([5, 6, 7])
deque([6, 7])
deque([7])
deque([])
def undirected_cycle_test(graph):         # Annahme: der Graph ist zusammenhängend
                                          # (andernfalls führe den Algorithmus für jede Zusammenhangskomponente aus)
    visited = [False]*len(graph)          # Flags für bereits besuchte Knoten
    
    def visit(node, from_node):           # rekursive Hilfsfunktion: gibt True zurück, wenn Zyklus gefunden wurde
        if not visited[node]:             # wenn node noch nicht besucht wurde
            visited[node] = True          # markiere node als besucht
            for neighbor in graph[node]:  # besuche die Nachbarn ...
                if neighbor == from_node: # ... aber überspringe den Vaterknoten
                    continue
                if visit(neighbor, node): # ... signalisiere, wenn rekursiv ein Zyklus gefunden wurde
                    return True
            return False                  # kein Zyklus gefunden
        else:
            return True                   # Knoten schon besucht => Zyklus
    
    startnode = 0                         # starte bei beliebigem Knoten (hier: Knoten 0)
    return visit(startnode, startnode)    # gebe True zurück, wenn ein Zyklus gefunden wurde

graph_c=[[1,2], [0,3], [0, 3, 4, 5], [1,2], [2], [2]]
graph_a=[[1,2], [0  ], [0, 3, 4, 5], [  2], [2], [2]]

undirected_cycle_test(graph_c)
True
def connectedComponents(graph):
    anchors = [None] * len(graph)             # property map für Anker jedes Knotens
    labels  = [None] * len(graph)             # property map für Label jedes Knotens
       
    def visit(node, anchor):
        """anchor ist der Anker der aktuellen ZK"""
        if anchors[node] is None:         # wenn node noch nicht besucht wurde:
            anchors[node] = anchor        # setze seinen Anker
            labels[node] = labels[anchor] # und sein Label
            for neighbor in graph[node]:  # und besuche die Nachbarn
                visit(neighbor, anchor)
       
    current_label = 0                         # Zählung der ZK beginnt bei 0
    for node in range(len(graph)):
        if anchors[node] is None:             # Anker noch nicht bekannt => neue ZK gefunden
            labels[node] = current_label      # Label des Ankers setzen
            visit(node, node)                 # Knoten der neuen ZK rekursiv suchen
            current_label += 1                # Label für die nächste ZK hochzählen
    return anchors, labels
    
graph_2k = [[1], [0,2], [1],     [4,6], [3,5], [4], [3]]
graph_1k = [[1], [0,2], [1,3], [2,4,6], [3,5], [4], [3]]

connectedComponents(graph_2k)
([0, 0, 0, 3, 3, 3, 3], [0, 0, 0, 1, 1, 1, 1])