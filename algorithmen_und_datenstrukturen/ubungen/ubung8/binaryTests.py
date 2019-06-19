import matplotlib.pyplot as plt
from timeit import Timer

def binarySearch(a, key1, start, end):
    key = int(key1)
    size = end - start
    if size <= 0:
        return None
    center = (start + end) //2
    if key == a[center]:
        return center
    elif key > a[center]:
        return binarySearch(a, key, center + 1, end)
    else:
        return binarySearch(a, key, start, center)

def binarySearch2(a, key1):
    key = int(key1)
    if len(a) == 0:
        return None
    center = len(a)//2
    if key == a[center]:
        return key
    elif key < a[center]:
        b = []
        for t in a[:center]:
            b.append(t)
        return binarySearch2(b, key)
    else:
        b = []
        for t in a[center+1:]:
            b.append(t)
        res = binarySearch2(b, key)
    if res is None:
        return None
    else:
        return res + center + 1

print(binarySearch2(test, 5))

data2 = [10000, 300000, 1000]
data1 = [2, 10000, 100]

def printBinarySearches(nSearch1, nSearch2, titleSearch1 = "Binary Search Plot", titleSearch2 = "Binary Search 2 Plot"):
    xdata1 = []
    ydata1 = []
    xdata2 = []
    ydata2 = []
    for N in range(nSearch2[0], nSearch2[1], nSearch2[2]):
        t2 = Timer("binarySearch2(a,str(randint(0,"+str(N)+")))", "from random  import randint\nfrom __main__ import binarySearch2\na=range("+str(N)+")")
        time2 = t2.timeit(100)/100
        xdata2.append(N)
        ydata2.append(time2)
    for N in range(nSearch1[0], nSearch1[1], nSearch1[2]): 
        t1 = Timer("binarySearch(a,str(randint(0,"+str(N)+")),0,len(a))", "from   random import randint\nfrom __main__ import binarySearch\na=range("+str(N)+")")
        time1 = t1.timeit(100)/100
        xdata1.append(N)
        ydata1.append(time1)

    fig1 = plt.figure(1)
    ax1 = fig1.add_subplot(1, 1, 1)
    ax1.plot(xdata1, ydata1, color='tab:blue')
    ax1.set_title(titleSearch1)
    plt.xlabel('N')
    plt.ylabel('time (s)')
    fig2 = plt.figure(2)
    ax2 = fig2.add_subplot(1, 1, 1)
    ax2.plot(xdata2, ydata2, color='tab:orange')
    plt.xlabel('N')
    plt.ylabel('time (s)')
    ax2.set_title(titleSearch2)
    plt.show()

possibleNs = [
    {'binarySearch': [0, 100, 1], 'binarySearch2': [0,100, 1]},
    {'binarySearch': [100, 1000, 1], 'binarySearch2': [100,1000, 1]},
    {'binarySearch': [10000, 300000, 1000], 'binarySearch2': [2, 10000, 100]},
    {'binarySearch': [0, 100, 10], 'binarySearch2': [0,100, 10]}
    {'binarySearch': [0, 1000, 1], 'binarySearch2': [0,1000, 1]}
    {'binarySearch': [0, 10000, 5], 'binarySearch2': [0,10000, 5]}
    {'binarySearch': [0, 1000, 100], 'binarySearch2': [0,1000, 100]}
]

for i in range(len(possibleNs)):
    printBinarySearches(possibleNs[i]['binarySearch'], possibleNs[i]['binarySearch2'])