import math
import unittest

def nachBetragSortieren(a):
    b = sorted(a, key=math.fabs)
    print(b)

array = [-2,1,-8, -3, 5]
nachBetragSortieren(array)

def tupelSortieren(a):
    d = sorted(a, key = lambda tupel: math.fabs(tupel[1]))
    print(d)

tupel = [('a', 3),('b', -2), ('c', 1)]
tupelSortieren(tupel)

def sorting(a):
    f = []
    g = []

    for i in range(len(a)):
        if a[i]%2 == 0:
            f.append(a[i])
        else:
            g.append(a[i])
    return sorted(f)+sorted(g, reverse = True)


newarray = [3, 4, -7, -9, 1, 6, -8]
sorting(newarray)

class TestSort(unittest.TestCase):

    def setUp(self):
        '''Create test data.'''

        # small arrays
        self.testArrays = [
            [],           # empty array
            [2],        # one element
            [3,2],  # two elements
            [5, -2, 7, 11, -4, 4, 12, 3, -9] # multiple entries (with negatives)
        ]
    
    def testsorting(self):
        sorted = []
        for a in self.testArrays:
            sorted.append(sorting(a))
        
        for a in sorted:
            if len(self.testArrays[a]) != len(sorted[a]):
                return False
            for i in len(a):
                gerade = True
                if a[i]%2 == 0:
                    if gerade == False:
                        return False
                if a[i]%2 == 0 and a[i+1]%2 == 0:
                    if a[i] > a[i+1]:
                        return False
                if a[i]%2 != 0 and a[i+1]%2 != 0:
                    gerade = False
                    if a[i] < a[i+1]:
                        return False
                    
if __name__ == '__main__':
    unittest.main(exit=False)                
        
        
        
        