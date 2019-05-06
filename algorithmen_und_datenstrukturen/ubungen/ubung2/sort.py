
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
        a[r] = pivot
    return i, counter

def quickSortImpl(a, l, r, counter = 0):
    quickSortImpl.counter = counter
    if r > l:
        k, passedCounter = partition(a,l,r)
        quickSortImpl.counter += passedCounter
        quickSortImpl(a,l, k - 1, quickSortImpl.counter)
        quickSortImpl(a, k + 1, r, quickSortImpl.counter)
        return a, quickSortImpl.counter

def quickSort(a):
    newArray, count = quickSortImpl(a, 0, len(a) - 1)
    return newArray, count



from random import sample
from copy import deepcopy
test = sample(range(101), 50)
test1 = deepcopy(test)
test2 = deepcopy(test)

test, comparisonCount1 = insertionSort(test)

test1, comparisonCount2 = mergeSort(test1)

test2, comparisonCount3 = quickSort(test2)

print(f"Insertion sort count = {comparisonCount1}, sorted array is",test )
print(f"MergeSort sort count = {comparisonCount2}, sorted array is",test1 )
print(f"Quicksort sort count = {comparisonCount3}, sorted array is",test2)