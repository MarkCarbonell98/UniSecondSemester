def selectionSort(a):
    n = len(a)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
            a[i], a[min] = a[min], a[i]

# sorting => g is min
# gortins => i = 1
# girtons => swap i mit n
# gintors => swap t und o
# ginotrs => swap t und r
# ginorts => swap t und s
# ginorst => complete
# 


import random
testList = random.sample(range(101), 50)
selectionSort(testList)
print("Selection sort: ",testList)

def insertionSort(a):
    n = len(a)
    for i in range(n):
        current = a[i]
        j = i
        while j > 0:
            if current < a[j - 1]:
                a[j] = a[j - 1]
            else:
                break
            j -= 1
        a[j] = current

# sorting 
# ssrtring 
# osrting
# orsting
# 
# 
# 

testList = random.sample(range(101), 50)
insertionSort(testList)
print("Insertion sort: ",testList)

# mergesort und quicksort

def merge(left, right):
    res = []
    i, j = 0,0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i : len(left)] + right[j : len(right)]
    return res

def mergeSort(a):
    n = len(a)
    if n <= 1:
        return a
    else:
        left = a[0 : n//2] # floor(n/2)
        right = a[n//2 : n]
        leftSorted = mergeSort(left)
        rightSorted = mergeSort(right)
        return merge(leftSorted, rightSorted)

testList = random.sample(range(101), 50)
print("MergeSort", mergeSort(testList))
# sorting
# sor ting
# s or ti ng
# s o r t i n g
# s or it gn
# ors gint
# ginorst

def partition(a, l, r): #left and right pointers. a is the array
    pivot = a[r]
    i = l
    j = r - 1
    while True:
        while i < r and a[i] <= pivot:
            i += 1
        while j > l and a[j] >= pivot:
            i -= 1
        if i < j:
            a[i], a[j] = a[j], a[i] #swap
        else:
            break
        a[r] = pivot
        return i

def quickSortImpl(a, l, r):
    if r > l:
        k = partition(a,l,r)
        quickSortImpl(a,l, k - 1)
        quickSortImpl(a, k + 1, r)

def quickSort(a):
    quickSortImpl(a, 0, len(a) - 1)

testList = random.sample(range(101), 50)
print(quickSort(testList))
