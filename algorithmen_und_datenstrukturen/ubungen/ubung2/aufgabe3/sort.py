from random import sample, randint
from copy import deepcopy
import matplotlib.pyplot as plt
import timeit
from math import log

def randomArray(n):
    array = [0] * n
    for i in range(n):
        array[i] = randint(0, 10000)
    return array

#insertion sort
def insertionSort(a):
    counter = 0
    for i in range(len(a)):
        current = a[i]
        j = i
        while j > 0:
            counter += 1
            if current < a[j - 1]:
                a[j] = a[j - 1]
            else:
                break
            j -= 1
        a[j] = current
    return a, counter

# mergesort
def merge(left, right):
    res = []
    i, j = 0,0
    counter = 0
    while i < len(left) and j < len(right):
        counter += 1
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i : len(left)] + right[j : len(right)]
    return res, counter

def mergeSort(a, counter = 0):
    mergeSort.counter = counter
    n = len(a)
    if n <= 1:
        return a, mergeSort.counter
    else:
        left = a[0 : n//2] # floor(n/2)
        right = a[n//2 : n]
        leftSorted, count1 = mergeSort(left, mergeSort.counter)
        rightSorted, count2 = mergeSort(right, mergeSort.counter)
        result, passedCounter = merge(leftSorted, rightSorted)
        # mergeSort.counter += passedCounter + count1 + count2
        mergeSort.counter += passedCounter
        return result, mergeSort.counter

# quicksort
def partition(a, l, r): #left and right pointers. a is the array
    pivot = a[r]
    i = l
    j = r - 1
    counter = 0
    while True:
        counter += 1
        while i < r and a[i] <= pivot:
            counter += 1
            i += 1
        while j > l and a[j] >= pivot:
            j -= 1
            counter += 1
        if i < j:
            a[i], a[j] = a[j], a[i] #swap
        else:
            break
    a[r] = a[i]
    a[i] = pivot
    return i, counter

def quickSortImpl(a, l, r, counter = 0):
    quickSortImpl.counter = counter
    if r > l:
        k, passedCounter = partition(a,l,r)
        quickSortImpl.counter += passedCounter
        quickSortImpl(a,l, k - 1, quickSortImpl.counter)
        quickSortImpl(a, k + 1, r, quickSortImpl.counter)
        return quickSortImpl.counter

def quickSort(a):
    count = quickSortImpl(a, 0, len(a) - 1)
    return a, count

def countAmmoutOfComparisons(arrayLength,fn,fnPointer, passedA,passedB, passedC, comparisonFunctionLabel, aString,bString,cString, hasLog = False):
    comparisonsArray = [0.0] * arrayLength
    for n in range(1, arrayLength + 1):
        testArray = randomArray(n)
        sortedArray, comparisonCount = fnPointer(testArray)
        comparisonsArray[n - 1] = comparisonCount
    
    fig = plt.figure()
    plt.plot(range(1, arrayLength + 1), comparisonsArray, label=f"{fn}")

    a = passedA
    b = passedB
    c = passedC

    if(hasLog):
        plt.plot(range(1, arrayLength+1), [a*log(n)* + b*n + c for n in range(1, arrayLength+1)], label=f"{comparisonFunctionLabel}, {aString} = {passedA}, {bString} = {passedB}, {cString} = {passedC}")
    else:
        plt.plot(range(1, arrayLength+1), [a*n**2 + b*n + c for n in range(1, arrayLength+1)], label=f"{comparisonFunctionLabel}, {aString} = {passedA}, {bString} = {passedB}, {cString} = {passedC}")

    plt.legend()
    plt.savefig(f"{fn}IterationCount.png")
    plt.show()

# countAmmoutOfComparisons(100, "insertionSort", insertionSort, .2, 2.2, 0.001, "a * n**2 + b*n + c ","a", "b", "c")

# countAmmoutOfComparisons(100, "mergeSort", mergeSort, .5, 2.3, 0.001, "d * n*log(n) + e*n + f ", "d", "e", "f", True)

# countAmmoutOfComparisons(100, "quickSort", quickSort, 1, 1.5, 0.0001, "g*n*log(n) + h*n + i ", "h", "i", "j", True)


test = sample(range(101), 50)
print(test.sort(), test)
test1 = deepcopy(test)
test2 = deepcopy(test)

test, comparisonCount1 = insertionSort(test)

test1, comparisonCount2 = mergeSort(test1)

test2, comparisonCount3 = quickSort(test2)

print(f"Insertion sort count = {comparisonCount1}, sorted array is",test )
print(f"MergeSort sort count = {comparisonCount2}, sorted array is",test1 )
print(f"Quicksort sort count = {comparisonCount3}, sorted array is",test2)

def printTest(arrLength, sortingMethod, passedA, passedB, passedC, comparisonFunctionLabel, aString, bString, cString, hasLog = False):
    maxN = arrLength
    time = [0.0] * maxN

    for n in range(1, maxN + 1):
        setup = f'''
from __main__ import randomArray, {sortingMethod}
testArray = randomArray({n})
        '''

        prog = f'''
{sortingMethod}(testArray)
        '''
        timer = timeit.Timer(prog, setup)
        time[n - 1] = timer.timeit(100) / 100

    figure = plt.figure()
    plt.plot(range(1, maxN + 1), time, label=f"{sortingMethod}")

    a = passedA
    b = passedB
    c = passedC
    if(hasLog):
        plt.plot(range(1, maxN+1), [a*n*log(n) + b*n + c for n in range(1, maxN+1)], label=f"{comparisonFunctionLabel}, {aString} = {passedA}, {bString} = {passedB}, {cString} = {passedC}")
    else:
        plt.plot(range(1, maxN+1), [a*n**2 + b*n + c for n in range(1, maxN+1)], label=f"{comparisonFunctionLabel}, {aString} = {passedA},, {bString} = {passedB}, {cString} = {passedC}")

    plt.legend()
    plt.savefig(f"{sortingMethod}")
    plt.show()
    return time

# printTest(100, "insertionSort", 3e-9, 3e-10, 1e-9,  "comparison a * N^2 * b * N + c", "a", "b", "c") # print insertionSort

# printTest(100, "mergeSort",.9e-6, 2.1e-8, 1e-7, "comparison d * N * log N + e * N + f", "d", "e", "f", True)

# printTest(100, "quickSort", 1.4e-6, 2.1e-8, 1e-7,"comparison g * N * log h + e * N + i", "g", "h", "i",  True)

def checkSorting(arrayBefore, arrayAfter):
    if(len(arrayBefore) != len(arrayAfter)):return False
    sortedArray = deepcopy(arrayBefore)
    sortedArray.sort()
    for i in range(len(arrayBefore)):
        if(arrayAfter[i] != sortedArray[i]): return False
    if(arrayAfter != sortedArray): return False
    return True

lastTest = sample(range(101), 50)
clone1 = deepcopy(lastTest)
clone2 = deepcopy(lastTest)

assert(checkSorting(lastTest, insertionSort(lastTest)[0]))
assert(checkSorting(clone1, mergeSort(clone1)[0]))
assert(checkSorting(clone2, quickSort(clone2)[0]))
# assert(checkSorting(lastTest, test)) # this one will fail
    



