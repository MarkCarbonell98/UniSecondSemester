import unittest

def binarySearch(a, key1, start, end):
    key = int(key1)
    size = end - start
    if size <= 0:
        return None
    center = (start + end) // 2
    if key == a[center]:
        return center
    elif key < a[center]:
        return binarySearch(a, key, start, center)
    else:
        return binarySearch(a, key, center+1, end)

def binarySearch2(a,key1):
    key = int(key1)
    if len(a) == 1 and a[0] == key:
        return 0
    if len(a) == 0:
        return None
    center = len(a) // 2
    if key == center:
        return center
    elif key < a[center]:
        b= []
        for t in a[:center]:
            b.append(t)
        return binarySearch2(b, key)
    else:
        b = []
        for t in a[center + 1:]:
            b.append(t)
        res = binarySearch2(b, key)
    if res == None:
        return None
    else:
        return res + center + 1    

# Aufgabe 2b
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
    {'binarySearch': [0, 100, 10], 'binarySearch2': [0,100, 10]},
    {'binarySearch': [0, 1000, 1], 'binarySearch2': [0,1000, 1]},
    {'binarySearch': [0, 10000, 5], 'binarySearch2': [0,10000, 5]},
    {'binarySearch': [0, 1000, 100], 'binarySearch2': [0,1000, 100]}
]

for i in range(len(possibleNs)):
    printBinarySearches(possibleNs[i]['binarySearch'], possibleNs[i]['binarySearch2'])

# Wie in der Auf. 1 gezeigt, hat binarySearch eine Komplexitat von O(log n) und binarySearch2 O(n)


#Aufgabe 3
def binarySearchI(a, key1):
    key = int(key1)
    start, end = 0 ,len(a) -1
    center = (start + end)//2
    while start <= end:
        if a[center] > key:
            end = center - 1
        elif a[center] < key:
            start = center + 1
        elif key == a[center]:
            return center
        center = (start + end)//2
    return None

#Tests
class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.lists = [
            {"list": [], "key": 0, "result": None},
            {"list": [0], "key": 0, "result": 0},
            {"list": [1], "key": 1, "result": 0},
            {"list": [-1,1], "key": 1, "result": 1},
            {"list": [1,2,3,4], "key": 3, "result": 2},
            {"list": [0, 2, 10, 15, 20], "key": 15, "result": 3},
            {"list": [-20, -10, -5, -1], "key": -1, "result": 3},
            {"list": [1, 1,2,5000], "key": 2, "result": 2},
            {"list": [0, 0, 0, 0, 0, 1], "key": 1, "result": 5},
            {"list": [-1, 0, 0, 0, 0, 0, 1], "key": -1, "result": 0},
            {"list": [-2, -1, 0], "key": -1, "result": 1},
        ]
        
    def test_binarySearch(self):
        for i in range(len(self.lists)):
            arr = self.lists[i]
            self.assertEqual(binarySearch(arr['list'], arr['key'], 0, len(arr['list'])), arr['result'], f"Search returns wrong value with input {arr['list']}")

    def test_binarySearchI(self):
        for i in range(len(self.lists)):
            arr = self.lists[i]
            self.assertEqual(binarySearchI(arr['list'], arr['key']), arr['result'], f"Search returns wrong value with input {arr['list']}")

if __name__ == "__main__":
    unittest.main()



