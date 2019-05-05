from math import log
import matplotlib.pyplot as plt
from random import randint
import timeit

def randomArray(N):
    array = [0] * N
    for i in range(N):
        array[i] = randint(0, 10000)
    return array

def builtinSort(array):
    return sorted(array)

maxN = 100
time = [0.0] * maxN

for N in range(1, maxN+1):
    setup = '''
from __main__ import randomArray, builtinSort
array = randomArray({})
    '''.format(N)
    prog = '''
builtinSort(array)
    '''
    timer = timeit.Timer(prog, setup)
time[N-1] = timer.timeit(100) / 100

fig = plt.figure()

plt.plot(range(1, maxN+1), time, label='builtin')

a = 0.0
b = 1e-7
plt.plot(range(1, maxN+1), [a*N*log(N)+b*N for N in range(1, maxN+1)],label='a*N*log(N)+b*N')

plt.legend()
plt.savefig('time.png')
plt.show()