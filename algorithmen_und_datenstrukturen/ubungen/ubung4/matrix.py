#naive Implementierung
from random import randint
import timeit

size = 100

A = [randint(-11, 10) for x in range(size * size)]
B = [randint(-11, 10) for x in range(size * size)]

def naiveMultiplication(matrixA, matrixB):
    C = [0 for x in range(size * size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                C[i + j*size] += matrixA[i + k*size] * matrixB[k + j*size]
    return C

def optimizedMultiplication(matrixA, matrixB):
    C = [0 for x in range(size * size)]
    for j in range(size): #die anderung in der Reihenfolge der Schleifen erlaubt as ausnutzen des Prozessors Cache in eine effizientere form. Da der Index j sich nicht so regelmaßig ändert wir der Index k. 
        jSize = j * size #eliminierung der loop invariant j * size
        for k in range(size):
            kSize = k * size
            kjSize = k + jSize #optimierung der variable jSize as kjSize, eliminierung eine unnotwendige Addition bei Ausführung der Schleife
            for i in range(size):
                C[i + jSize] += matrixA[i + kSize] * matrixB[kjSize] #Elimination der redundantem Code wie k * size, oder j*size, in die form der eliminierung der loop invariant
    return C



print("the naive implementation: ")
startTime = timeit.default_timer()
naiveMultiplication(A,B)
print(timeit.default_timer() - startTime)


print("the optimized implementation: ")
startTime = timeit.default_timer()
optimizedMultiplication(A,B)
print(timeit.default_timer() - startTime)



