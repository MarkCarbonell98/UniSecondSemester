
def merge(left, right):
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j += 1
    res += left[i: len(left)] + right[j: len(right)]
    return res

def mergeSort(a):
    n = len(a)
    if n <= 1:
        return a
    left = a[0:n//2]
    right = a[n//2:n]
    leftSorted = mergeSort(left)
    rightSorted = mergeSort(right)
    return merge(leftSorted, rightSorted)

def insertionSort(a):
    for i in range(len(a)):
        correct = a[i]
        j = i
        while j > 0:
            if correct < a[j - 1]:
                a[j] = a[j - 1]
            else:
                break
            j -= 1
        a[j] = correct
    return a

# quicksort
def quickSort(a):
    quickSortImpl(a, 0, len(a) - 1)
    return a

def quickSortImpl(a, l, r):
    if r > l:
        k = partition(a, l, r)
        quickSortImpl(a, l, k - 1)
        quickSortImpl(a, k + 1, r)

def partition(a, l, r):
    pivot = a[r]
    i = l
    j = r - 1
    while True:
        while i < r and a[i] <= pivot: i += 1
        while j > l and a[j] >= pivot: j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
        else: 
            break
    a[r] = a[i]
    a[i] = pivot
    return i
        

test1 = [4,-1,0,5,3,7,10]
test2 = [4,-1,0,5,3,7,10]
test3 = [4,-1,0,5,3,7,10]

insertionSort = insertionSort(test1)
mergeSort = mergeSort(test2)
quickSort = quickSort(test3)
print(insertionSort)
print(mergeSort)
print(quickSort)


