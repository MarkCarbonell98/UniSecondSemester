# Aufgabe 1a

graph = [[1], [2,3], [1], [4,5], [3], [3,6,7], [5], [5,8,10], [7,9,10], [8], [7,8, 11], [12,13], [11] ,[11, 14, 15], [13], [13]]

for arr in graph:
    arr.sort(reverse=True)

print("Adjazenzlisten: ", graph)

# aufgabe 1b
def way_out(graph, startnode, targetnode):
    visited = [None]*len(graph)
    deadEnds = set()
    targetReached = [False]
    def visit(node):
        if node == targetnode:
            targetReached[0] = True
        isDeadEnd = len(graph[node]) == 1 and node != targetnode and node != startnode
        if isDeadEnd:
            deadEnds.add(node)
            print(node, "dead end")
        else:
            print(node)
        if not visited[node]:
            visited[node] = True
            for neighbor in graph[node]:
                if(visited[neighbor]):
                    print(neighbor, "(backtracking)")
                visit(neighbor)
    visit(startnode)
    if targetReached[0]:
        print("taget reached")
        print(f"the algorithm found {len(deadEnds)} dead ends on the way")
    else:
        print("target out of range")
    return deadEnds, targetReached

# der anfang und ende des Graphes werden nicht als dead ends betrachtet
way_out(graph, 0, 15)

def way_out_stack(graph, startnode, endnode):
    stack = [startnode]
    visited = [None]*len(graph)
    targetReached = [False]
    deadEnds = set()
    while(len(stack)):
        node = stack.pop(0)
        isDeadEnd = len(graph[node]) == 1 and node != startnode and node != endnode
        if isDeadEnd:
            deadEnds.add(node)
            print(node, "dead end")
        else:
            if node == endnode:
                targetReached[0] = True
            print(node)

        if not visited[node]:
            visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                stack.append(neighbor)
            else:
                print(neighbor, "(backtrack)")
    if targetReached[0]:
        print("target reached")
        print(f"the algorithm found {len(deadEnds)} dead ends on the way")
    else:
        print("target out of range")
    return deadEnds, targetReached

way_out_stack(graph, 0, 15)

import unittest

class TestWayOut(unittest.TestCase):
    def setUp(self):
        self.graph = graph
        self.possibleSearches = [[0,15], [1,15], [0,0], [4,15], [1,5], [15,15]]

    # somit laufen way_out und way_out_stack gleich
    def test_both_way_outs(self):
        for i in range(len(self.possibleSearches)):
            actualStartAndEndNodes = self.possibleSearches[i]
            deadEnds, targetReached = way_out(self.graph, actualStartAndEndNodes[0], actualStartAndEndNodes[1])
            deadEndsStack, targetReachedStack = way_out_stack(self.graph, actualStartAndEndNodes[0], actualStartAndEndNodes[1])
            self.assertEqual(len(deadEndsStack), len(deadEnds))
            self.assertEqual(len(targetReached), len(targetReachedStack))
            self.assertEqual(deadEnds, deadEndsStack)
            self.assertEqual(targetReached, targetReachedStack)

    

if __name__ == '__main__':
    unittest.main()



