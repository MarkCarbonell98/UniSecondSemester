import copy
from timeit import Timer
from random import shuffle, randint


def insertionSort(inList):
    
    count = 0
    #iterate through all elements from left to right 
    for i in range(len(inList)):
        current = a[i] #remember the current element
        #find the position of the gap where 'current' is supposed to go
        j = i
        while j > 0:
            count+=1
            if current < a[j-1]: # a[j-1] should be to the right of current
                a[j] = a[j-1]    # move a[j-1] to the right
            else:
                break            # gap is at the correct position
            j -= 1               # shift the gap one position to the left
        a[j] = current           # place current into the gap
        
    return count


def merge(left, right):
    
    count = 0
    #initialize result list
    result = []
    #while both of them are not empty
    while len(left) > 0 and len(right) > 0:
        #compare the first element of each list, then pop the smaller one
        #and append it at the result list
        if left[0] > right [0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))
        #iterate count
        count += 1
    #append the rest of the remaining not empty list
    result.extend(right)
    result.extend(left)
    return result, count


def mergeSort(inList):
    
    count = 0
    #if its just one element or empty, return it
    if len(inList) <= 1:
        return inList, 0
    else:
        #otherwise split it in half
        left = inList[:len(inList) // 2]
        right = inList[len(inList) // 2:]
        #and do the same with the resulting two lists.
        #meanwhile, collect all counts
        leftSorted, c = mergeSort(left)
        count += c
        rightSorted, c = mergeSort(right)
        count += c
    result, c = merge(leftSorted, rightSorted)
    count += c
    #return the merged, sorted list and the accumulated sort count
    return result, count

def quickSort(inList, left=0, right=None): # standard quicksort
    
    #we want to be able to call quickSort(a), without having to specify the 
    #specific length.
    if right == None:
        right = len(inList)-1
    #every cycle the list is reordered so that every element < pivot is left 
    #of every element > pivot. Then the list are split into two partitions at 
    #the position of the pivot and the cycle starts anew for those partitions
    
    #do this while the sublists are longer then one
    if right > left :
        #retrieve the partition index, start quicksort for partitions, add up
        #counts
        i,count = partition(inList, left , right)    
        count += quickSort(inList, left , i - 1)      
        count += quickSort(inList, i + 1, right)
        return count
    else:
        return 0
        
        
def partition(inList, left, right):
    
    count = 0
    pivot = inList[right]     
    i  = left           
    j  = right - 1
    #let i (from left, to right) and j (from right, to left) move towards each
    #other and swap the elements which are in the wrong order relative to the 
    #pivot. stop if i reaches or overtakes j
    while True:
        while i < right and inList[i] <= pivot:
            i += 1
            count += 1
        while j > left and inList[j] >= pivot:
            j -= 1
            count += 1
        if i >= j:               
            break
        inList[i], inList[j] = inList[j], inList[i]
    #swap the pivot with ith element
    inList[i], inList[right] = inList[right], inList[i]      
    #return i. the list has now the property inList[:i] < inList[i] < inList[i:]
    #you can easily deduce by induction the list will be sorted if this is 
    #repeated for all partitions inList[:i] and inList[i:]
    return i,count                     


def quickSortR(inList, left=0, right=None): # randomized quicksort
    
    #we want to be able to call quickSort(a), without having to specify the 
    #specific length.
    if right is None:
        right = len(inList)-1
    #every cycle the list is reordered so that every element < pivot is left 
    #of every element > pivot. Then the list are split into two partitions at 
    #the position of the pivot and the cycle starts anew for those partitions
    
    #do this while the sublists are longer then one
    if right > left :
        #retrieve the partition index, start quicksort for partitions, add up
        #counts
        i,count = partitionR(inList, left , right)    
        count += quickSortR(inList, left , i - 1)      
        count += quickSortR(inList, i + 1, right)
        return count
    else:
        return 0
    
        
def partitionR(inList, left, right):
    
    count = 0
    #randomize the pivot and put it into its place
    pivot = inList[randint(left,right)]
    inList[right],inList[pivot] = inList[pivot],inList[right]
    i  = left           
    j  = right - 1
    #let i (from left, to right) and j (from right, to left) move towards each
    #other and swap the elements which are in the wrong order relative to the 
    #pivot. stop if i reaches or overtakes j
    while True:
        while i < right and inList[i] <= pivot:
            i += 1
            count += 1
        while j > left and inList[j] >= pivot:
            j -= 1
            count += 1
        if i >= j:               
            break
        inList[i], inList[j] = inList[j], inList[i]
    #swap the pivot with ith element
    inList[i], inList[right] = inList[right], inList[i]      
    #return i. the list has now the property inList[:i] < inList[i] < inList[i:]
    #you can easily deduce by induction the list will be sorted if this is 
    #repeated for all partitions inList[:i] and inList[i:]                             
    return i,count                     


def checkSort(inList, outList):
    
    #make a copy of the out list
    outListc = copy.deepcopy(outList)
    #compare lenghts
    if len(inList) != len(outList):
        return False
    #check for all elements to be the same
    for x in inList:
        try:
            outListc.remove(x)
        except:
            return False
    #check for all elements being sorted properly
    for i in range(len(outList) - 1):
        if outList[i] > outList[i + 1]:
            return False
    #all tests passed, return True
    return True
        

#*****************************************************************************#
#         Apply algorithms and save the collected data to files               #
#*****************************************************************************#

testDir = './'        
#open file with write access
f = open(testDir + 'varyN.txt', 'w')
#check the count of sort algorithms for lists
#between length 2 and 500 
for i in range(2, 500):
    #create random list
    a = list(range(i))
    shuffle(a)
    #and two copies -> 3 sorting algorithms
    b = copy.deepcopy(a)
    c = copy.deepcopy(a)
    #create a string containing information about
    #the respective counts, write it to file
    f.write(str(i) + "," + \
            str(insertionSort(a)) + "," + \
            str(mergeSort(b)[1]) + "," + \
            str(quickSort(c)) + "\n")
#close file
f.close()

#open file with write acess
f = open(testDir + 'varyT.txt', 'w')
#check the duration of sort algorithms for lists
#between length 2 and 500 
for i in range(2, 500):
    #create a random list
    a = list(range(i))
    shuffle(a)
    #and two copies -> 3 sorting algorithms
    b = copy.deepcopy(a)
    c = copy.deepcopy(a)
    #create a string containing information about
    #the respective durations, write it to file
    f.write(str(i) + ", " + \
            str(Timer("insertionSort(" + str(a) + ")", 'from __main__ import insertionSort').timeit(1)) + ", " + \
            str(Timer("mergeSort(" + str(b) + ")", 'from __main__ import mergeSort').timeit(1)) + ", " + \
            str(Timer("quickSort(" + str(c) + ")", 'from __main__ import quickSort').timeit(1)) + "\n");
#close file
f.close()

#open file with write access
f = open(testDir + 'badQs.txt', 'w')
#check the count of sort algorithms for lists
#between length 2 and 500 with a bad QsCondition
#(already ordered list)   
for i in range(2, 500):
    #create random list
    a = list(range(i))
    shuffle(a)
    #and two copies -> 3 sorting algorithms
    b = copy.deepcopy(a)
    c = copy.deepcopy(a)
    #create a string containing information about
    #the respective counts, write it to file
    f.write(str(i) + "," + \
            str(insertionSort(a)) + "," + \
            str(mergeSort(b)[1]) + "," + \
            str(quickSort(a)) + "\n")
#close file
f.close()

#open file with write access
f = open(testDir + 'randomQs.txt', 'w')
#check the count of sort algorithms for lists
#between length 2 and 500 with a randomized Qs
#algorithm
for i in range(2, 500):
    #create random list
    a = list(range(i))
    shuffle(a)
    #and two copies -> 3 sorting algorithms
    b = copy.deepcopy(a)
    c = copy.deepcopy(a)
    #create a string containing information about
    #the respective counts, write it to file
    f.write(str(i) + "," + \
            str(insertionSort(a)) + "," + \
            str(mergeSort(b)[1]) + "," + \
            str(quickSortR(a)) + "\n")
#close file
f.close()


