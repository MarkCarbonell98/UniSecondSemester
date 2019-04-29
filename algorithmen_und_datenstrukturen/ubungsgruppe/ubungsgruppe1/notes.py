# python ist ein Dynamisch Typisierte Sprache
# c++ ist statisch Typisiert



from random import randint
import timeit

def buildinSort(array):
    return sorted(array)

def randomArray(n):
    array = [None] * n
    for i in range(n):
        array[i] = randint(0,10000)
    return array

print(randomArray(20))
import matplotlib.pylot as plt

maxN = 100
for n in range(1, maxN + 1):
    setup = '''
from __main__ import randomArray, buildinSort
array = randomArray({})
    '''.format(n)

    prog = '''
buildinSort(array)
    '''
    t = timeit.Timer(prog, setup)
    print(f'For an array of the length {n}: {t.timeit(1000) / 1000}')
    fig = plt.figure()
    plt.plot(range(1, maxN + 1), t, label="buildin")
    a = 1e-7
    plt.plot(range(1, maxN + 1), [a*n for n in range(1, maxN + 1)], label="a*n")
    plt.legend()
    plt.show 


#matplotlib 




#zeitmessung
