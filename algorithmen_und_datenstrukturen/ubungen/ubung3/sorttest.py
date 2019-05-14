import unittest
from random import randint
import copy

class Student:
    def __init__(self, name, mark):
        '''Construct new Student object with given 'name' and 'mark'.'''
        self.name = name
        self.mark = mark

    def getName(self):
        '''Access the name.'''
        return self.name

    def getMark(self):
        '''Access the mark.'''
        return self.mark

    def __repr__(self):
        '''Convert Student object to a string.'''
        return "%s: %3.1f" % (self.name, self.mark)

    def __eq__(self, other):
        '''Check if two Student objects are equal.'''
        return self.name == other.name and self.mark == other.mark

##################################################################

def insertionSort(a, key=lambda x: x):
    '''
    Sort the array 'a' in-place.

    Parameter 'key' must hold a function that, given a complicated
    object, extracts the property to be sorted by. By default, this
    is the object itself (useful to sort integers). To sort Students
    by name, for example, you would call:
        insertionSort(students, key=Student.getName)
    whereas to sort by mark, you use
        insertionSort(students, key=Student.getMark)
    This corresponds to the behavior of Python's built-in sorting functions.
    '''
    for i in range(1, len(a)):
        current = a[i]
        j = i
        while j > 0:
            # großer stets kleiner, und wechsel des Swaps auf linie 48
            if key(a[j-1]) > key(current):
                a[j] = a[j-1]
            else:
                break
            j -= 1
        a[j] = current

def merge(left, right, key = lambda x : x):
    res = []
    i, j = 0,0
    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i : len(left)] + right[j : len(right)]
    return res

def mergeSort(a, key=lambda x : x):
    n = len(a)
    if n <= 1:
        return a
    else:
        left = a[0 : n//2] # floor(n/2)
        right = a[n//2 : n]
        leftSorted = mergeSort(left, key)
        rightSorted = mergeSort(right, key)
        result = merge(leftSorted, rightSorted, key)
        return result

##################################################################

class TestSortingFunctions(unittest.TestCase):

    def setUp(self):
        '''Create test data.'''

        # integer arrays
        self.int_arrays = [
            [],           # empty array
            [1],          # one element
            [2,1],        # two elements
            [3,2,3,1],    # the array from the exercise text
            [randint(0, 4) for k in range(10)], # 10 random ints
            [randint(0, 4) for k in range(10)]  # another 10 random ints
        ]

        # Student arrays
        self.student_arrays = [
           [Student('Adam', 1.3),
            Student('Bert', 2.0),
            Student('Elsa', 1.0),
            Student('Greg', 1.7),
            Student('Jill', 2.7),
            Student('Judy', 3.0),
            Student('Mike', 2.3),
            Student('Patt', 5.0)], # without replicated marks

           [Student('Adam', 1.3),
            Student('Bert', 2.0),
            Student('Elsa', 1.3),
            Student('Greg', 1.0),
            Student('Jill', 1.7),
            Student('Judy', 1.0),
            Student('Mike', 2.3),
            Student('Patt', 1.3)], # with replicated marks, alphabetic

           [Student('Bert', 2.0),
            Student('Mike', 2.3),
            Student('Elsa', 1.3),
            Student('Judy', 1.0),
            Student('Patt', 2.0),
            Student('Greg', 1.0),
            Student('Jill', 1.7),
            Student('Adam', 1.3)] # with replicated marks, random order
        ]

    def testBuiltinSort(self):
        # test the integer arrays
        for a in self.int_arrays:
            copyOfASorted = copy.deepcopy(a)
            copyOfASorted.sort()
            self.checkIntegerSorting(a, copyOfASorted)

        # test the Student arrays
        for a in self.student_arrays:
            copyOfASorted = copy.deepcopy(a)
            copyOfASorted.sort(key=lambda x : x.mark)
            self.checkStudentSorting(a, copyOfASorted)

    def testInsertionSort(self):
        # test the integer arrays
        for a in self.int_arrays:
            copyOfASorted = copy.deepcopy(a)
            insertionSort(copyOfASorted)
            self.checkIntegerSorting(a, copyOfASorted)

        # test the Student arrays
        for a in self.student_arrays:
            copyOfASorted = copy.deepcopy(a)
            insertionSort(copyOfASorted, lambda x : x.mark)
            self.checkStudentSorting(a, copyOfASorted)

    def testMergeSort(self):
        # test the integer arrays
        for a in self.int_arrays:
            copyOfA = copy.deepcopy(a)
            copyOfASorted = mergeSort(copyOfA)
            self.checkIntegerSorting(a, copyOfASorted)

        # test the Student arrays
        for a in self.student_arrays:
            copyOfA = copy.deepcopy(a)
            copyOfASorted = mergeSort(copyOfA, lambda x : x.mark);
            self.checkStudentSorting(a, copyOfASorted)
            ... # your code here (test that array is sorted and stable)

    def checkIntegerSorting(self, original, result):
        '''Parameter 'original' contains the array before sorting,
        parameter 'result' contains the result of the sorting algorithm.'''
        self.assertEqual(len(original), len(result), "the length is not equal")
        for i in range(len(original)):
            assert original[i] in result
        for i in range(len(result)):
            assert result[i] in original
        resultCopy = copy.deepcopy(result)
        resultCopy.sort()
        self.assertEqual(result, resultCopy, "the result is not sorted properly")

    def checkStudentSorting(self, original, result):
        '''Parameter 'original' contains the array before sorting,
        parameter 'result' contains the result of the sorting algorithm.'''
        
        self.assertEqual(len(original), len(result), "the length is not equal");
        for i in range(len(original)):
            assert original[i] in result
        for i in range(len(result)):
            assert result[i] in original
        resultCopy = copy.deepcopy(result)
        resultCopy.sort(key=lambda x : x.mark)
        self.assertEqual(result, resultCopy, "the result is not sorted properly")

        #tests für stabile Sortierung
        for i in range(len(result)):
            for j in range(i+1,len(result)):
                if(result[i] == result[j]):
                    self.assertLess(original.index(result[i]), original.index(result[j]), "The sort was not stable");
        


##################################################################

if __name__ == '__main__':
    unittest.main()
