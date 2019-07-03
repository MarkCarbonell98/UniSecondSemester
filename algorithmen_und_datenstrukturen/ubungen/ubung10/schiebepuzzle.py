
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

# topologische Sortierung hat O(E + V) komplexitaet. Also gesamte Komplexitaet ist O(E) 

def swap(arr,a,b):
    arr[a], arr[b] = arr[b], arr[a]

def shuffle_pos(A, N):
    lastMove = None
    puzzleLength = len(A)
    sideLength = int(puzzleLength/4)
    for i in range(N):
        holePosition = A.index(' ')
        move = random.randint(0,3)
        if move == 0 and lastMove != 2 and (holePosition + 1) + sideLength <= puzzleLength: # up
            swap(A, holePosition, holePosition + sideLength)
        elif move == 2 and lastMove != 0 and (holePosition + 1) - sideLength > 0:
            swap(A, holePosition, holePosition - sideLength)
        elif move == 3 and lastMove != 1 and ((holePosition) % sideLength) != 0:
            swap(A, holePosition, holePosition-1)
        elif move == 1 and lastMove != 3 and ((holePosition + 1) % sideLength) != 0:
            swap(A, holePosition, holePosition+1)
        lastMove = move

shuffle_pos(p, 100)
print_pos(p)

# aufgabe c

from collections import deque

def solve_bfs(p, maxlevel):
    parents = [None]*len(p)            
    parents = {str(p): p} 
    print(parents)
    q = deque()                            # Queue für die zu besuchenden Knoten
    q.append(p) 
    counter = 0;                   # Startknoten in die Queue einfügen
    
    while len(q) > 0:
        if counter == maxlevel: break                      # solange noch Knoten zu bearbeiten sind
        counter += 1
        puzzle = q.popleft()                 # Knoten aus der Queue nehmen (first in - first out)
        print_pos(puzzle) 
        key = str(puzzle)    
        for neighbor in parents[key]:       # die Nachbarn expandieren
            if parents[neighbor] is None:  # Nachbar wurde noch nicht besucht
                parents[neighbor] = puzzle   
                q.append(neighbor)         



solve_bfs(p, 1000)

