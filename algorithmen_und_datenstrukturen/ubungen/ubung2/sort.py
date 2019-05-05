
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
    
    print("insertionSort counter = ", counter)

# mergesort
def merge(left, right):
    res = []
    i, j,counter = 0,0, 0
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
    n = len(a)
    if n <= 1:
        return a
    else:
        left = a[0 : n//2] # floor(n/2)
        right = a[n//2 : n]
        leftSorted = mergeSort(left)
        rightSorted = mergeSort(right)
        result, counter = merge(leftSorted, rightSorted)
        return result

# quicksort
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