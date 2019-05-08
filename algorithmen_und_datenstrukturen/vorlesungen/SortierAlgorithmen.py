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
    res = []     # the result array is initially empty
    i, j = 0, 0  # i and j always point to the first element in left and 
                #  right that has not yet been processed (= added to res)
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:    # compare the first unprocessed elements of left and right
            res.append(left[i])   # the smallest remaining element is in left => add to res
            i += 1                # go to next element in left
        else:
            res.append(right[j])  # the smallest remaining element is in right => add to res
            j += 1                # go to next element in right
    # either left or right has been used up, add the remaining elements of the other
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    # the latter two while loops can be abbreviated by Python's slice syntax
    # res += left[i:len(left)] + right[j:len(right)]
    # (syntax: array[m:n] returns the subarray from index m (inclusive) to index n (exclusive))
    return res


def mergeSort(a):  # sort 'a' out-of-place (i.e. a new sorted array is returned, 'a' is unchanged)
    N = len(a)     # number of elements
    if N <= 1:
        return a   # arrays with 0 or 1 elements are already sorted => stop recursion
    else:
        left  = a[0:N//2]   # slice syntax: left subarray
                            # N//2 is Python's 'floor division'
        right = a[N//2:N]   # slice syntax: right subarray
        leftSorted  = mergeSort(left)  # recursively sort left and ...
        rightSorted = mergeSort(right) # ... right subarrays
        return merge(leftSorted, rightSorted)  # merge the sorted parts and return result

testList = random.sample(range(101), 50)
print("MergeSort", mergeSort(testList))
# sorting
# sor ting
# s or ti ng
# s o r t i n g
# s or it gn
# ors gint
# ginorst

def partition(a, l, r):
    pivot = a[r]     # Pivot-Element. Hier wird willkürlich das letzte Element verwendet.
    i  = l           # i und j sind Laufvariablen
    j  = r - 1
    while True:
        while i < r and a[i] <= pivot:
            i += 1               # finde von links das erste Element > pivot
        while j > l and a[j] >= pivot:
            j -= 1               # finde von rechts das ersten Element < pivot
                                # (von links gesehen ist dies das letzte Element < pivot)
        if i < j:                # a[i] und a[j] sind beide auf der falschen Seite des Pivot
            a[i], a[j] = a[j], a[i]  # => vertausche sie
        else:                    # alle Elemente sind auf der richtigen Seite
            break                # => Schleife beenden      
    a[r] = a[i]                  # schaffe eine Lücke für das Pivot
                                # wegen a[i] >= pivot gehört das bisherige a[i] auf die rechte Seite
                                # wegen a[j] <= pivot und i >= j ist i die richtige Position
    a[i] = pivot                 # bringe das Pivot an seine endgültige Position i
    return i                     # gib die engültige Position des Pivots zurück

def quickSortImpl(a, l, r): 
    """a ist das zu sortierende Array, 
    l und r sind die linke und rechte Grenze (inklusive) des zu sortierenden Bereichs"""

    if r > l:                     # Rekursionsabschluss: wenn r <= l, enthält der Bereich höchstens ein Element
                                # und muss nicht mehr sortiert werden
        k = partition(a, l, r)    # k ist der Index des sog. Pivot-Elements (s. u.)
        quickSortImpl(a, l, k-1)  # rekursives Sortieren des linken ... 
        quickSortImpl(a, k+1, r)  # ... und rechten Teilarrays

def quickSort(a):                 # sortiere Array 'a' in-place
    quickSortImpl(a, 0, len(a)-1) # rufe den eigentlichen Algorithmus mit Arraygrenzen auf  

testList = random.sample(range(101), 50)
print(quickSort(testList))
