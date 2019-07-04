
# aufgabe a
p = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,' ']

def inZeile(a,b):
    if b > 9 and b != ' ': 
        print(a, end=' ')
    else:
        print(a, end='  ')

def anfangderZeile(a,b):
    if a == ' ':
        if b > 9:
            print(' ', a, end=' ')
        else:
            print(' ', a, end='  ')
    elif b == ' ':
        if a > 9:
            print(' ', a, end='  ')
        else:
            print('  ', a, end= '  ')
    else:
        if a > 9:
            if b > 9: 
                print(' ',a, end=' ')
            else:
                print(' ',a, end='  ')
        else:
            if b > 9: 
                print('  ',a, end=' ')
            else:
                print('  ',a, end='  ')
            
def print_pos(p):
    for i in range(len(p)):
        if (i-3)%4 == 0:
            print(p[i], end='\n')
        elif i%4 == 0:
            if p[i] != ' ' and p[i+1] != ' ':
                anfangderZeile(p[i], p[i+1])
            else:
                if p[i] == ' ':
                    if p[i+1] > 9:
                        print('  ',p[i], end=' ')
                    else:
                        print('  ',p[i], end='  ')
                else:
                    if p[i] > 9:
                        print(' ', p[i], end='  ')
                    else:
                        print('  ', p[i], end='  ')
        else:
            if i == 14: 
                print(p[i], end=' ')
            else:
                if p[i+1] != ' ':
                    inZeile(p[i], p[i+1])
                else:
                    print(p[i], end='  ')
# print_pos(p)

# aufgabe b
import random

# topologische Sortierung hat O(E + V) komplexitaet. aCopylso gesamte Komplexitaet ist O(E) 

def swap(arr,a,b):
    arr[a], arr[b] = arr[b], arr[a]


def shuffle_pos(A, N, passedMove=False):
    aCopy = A.copy()
    lastMove = None
    puzzleLength = len(aCopy)
    sideLength = int(puzzleLength/4)
    for i in range(N):
        holePosition = aCopy.index(' ')
        move = random.randint(0,3)
        if passedMove != False:
            move = passedMove
        if move == 0 and lastMove != 2 and (holePosition + 1) + sideLength <= puzzleLength:
            swap(aCopy, holePosition, holePosition + sideLength)
        if move == 2 and lastMove != 0 and (holePosition + 1) - sideLength > 0:
            swap(aCopy, holePosition, holePosition - sideLength)
        if move == 3 and lastMove != 1 and ((holePosition) % sideLength) != 0:
            swap(aCopy, holePosition, holePosition-1)
        if move == 1 and lastMove != 3 and ((holePosition + 1) % sideLength) != 0:
            swap(aCopy, holePosition, holePosition+1)
        lastMove = move
    return aCopy

# shuffle_pos(p, 100)
# print_pos(p)

# aufgabe c

from collections import deque

def areArraysEqual(a,b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True

def printPathToSolution(parents,p, solution):
    pathToSolution = []
    numberOfMoves = 0
    nextElement = parents[str(solution)]
    # while not areArraysEqual(nextElement, solution):
    #     print_pos(nextElement)
    #     print(nextElement)
    #     nextElement = parents[str(nextElement)]
    #     print(nextElement)
    #     numberOfMoves += 1
    while not areArraysEqual(nextElement, p):
        print_pos(nextElement)
        nextElement = parents[str(nextElement)]
        numberOfMoves += 1
    print(f"The puzzle was solved in {numberOfMoves} moves")

def solve_bfs(p, maxlevel):
    parents = [None]*len(p)            
    solution = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,' ']
    parents = {str(p): p} 
    q = deque()                            
    q.append(p) 
    counter = 0                   
    while counter < maxlevel and len(q) > 0:
        puzzle = q.popleft()           
        if areArraysEqual(solution, puzzle):
            printPathToSolution(parents,p, solution)
            return True
        else:
            neighbor = (str(puzzle), puzzle)
            if neighbor[0] in parents: 
                nextNeighborUp = shuffle_pos(neighbor[1], 1, 0)
                nextNeighborDown = shuffle_pos(neighbor[1], 1, 2)
                nextNeighborLeft = shuffle_pos(neighbor[1], 1, 1)
                nextNeighborRight = shuffle_pos(neighbor[1], 1, 3)
                nextNeighborUpDictHash = str(nextNeighborUp)
                nextNeighborDownDictHash = str(nextNeighborDown)
                nextNeighborLeftDictHash = str(nextNeighborLeft)
                nextNeighborRightDictHash = str(nextNeighborRight)
                if not nextNeighborUpDictHash in parents:
                    parents[nextNeighborUpDictHash] = neighbor[1]
                    q.append(nextNeighborUp)
                if not nextNeighborDownDictHash in parents:
                    parents[nextNeighborDownDictHash] = neighbor[1]
                    q.append(nextNeighborDown)
                if not nextNeighborLeftDictHash in parents:
                    parents[nextNeighborLeftDictHash] = neighbor[1]
                    q.append(nextNeighborLeft)
                if not nextNeighborRightDictHash in parents:
                    parents[nextNeighborRightDictHash] = neighbor[1]
                    q.append(nextNeighborRight)
        counter += 1
    print("unsolved")
    return False

shuffledP = shuffle_pos(p, 10)

ausgangstellung = [3,7,11, 4, 2, 5, 6, 8, 1,9, 12, ' ', 13, 10, 14, 15]
shuffledP = [1, 2, 3, 4, 5, 6, 7, 8, ' ', 10, 11, 12, 9, 13, 14, 15]
solve_bfs(ausgangstellung, 1000000)

import unittest

class TestSchiebepuzzle(unittest.TestCase):
    def setUp(self):
        self.p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, ' ']
        self.maxlevel = 100000000
        self.test = shuffle_pos(self.p, random.randint(1, 20))
    
    def test_schiebepuzzle(self):
        self.assertTrue(solve_bfs(self.p, self.maxlevel))

if __name__ == '__main__':
    unittest.main()


