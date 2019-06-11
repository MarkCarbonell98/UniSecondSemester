import random, math
import unittest

#Aufgabe 2a

def createData(size):
    a = []
    while len(a) < size:
        x, y = random.uniform(-1,1), random.uniform(-1,1)
        r = math.sqrt(x**2 + y**2)
        if r < 1.0:
            a.append(r)
    return a

def bucketMapNaive(r, M):
    return int(r*M)

def bucketMap(r, M):
    return int(r**2 * M)

data = createData(200)
M = 30

naiveData = []
normalData = []

for num in data:
    naiveIndex =bucketMapNaive(num, M)
    index = bucketMap(num, M)
    naiveData.append((naiveIndex, num))
    normalData.append((index, num))
    
sortedNaive = sorted(naiveData, key=lambda x: x[1])
sortedNormal = sorted(normalData, key=lambda x: x[1])

for i in range(len(sortedNaive)):
    print("Naive: ", sortedNaive[i], " Normal: ", sortedNormal[i])

naiveCountlens = []   
naiveCount = 0
for i in range(len(sortedNaive)-1):
    if sortedNaive[i][0] == sortedNaive[i+1][0]:
        naiveCount += 1
        print("Naive Index Count: ", sortedNaive[i], sortedNaive[i][0], " = ", naiveCount)
        if i == len(sortedNaive)-2:
            naiveCountlens.append(naiveCount)
    else:
        naiveCountlens.append(naiveCount)
        print("Normal Index Count: ", sortedNaive[i], " TOTAL ", sortedNaive[i][0], " = ", naiveCount)
        naiveCount = 0

normalCountlens = []   
normalCount = 0
for i in range(len(sortedNormal)-1):
    if sortedNormal[i][0] == sortedNormal[i+1][0]:
        normalCount += 1
        print("Normal Index Count: ", sortedNormal[i], sortedNormal[i][0], " = ", normalCount)
        if i == len(sortedNormal)-2:
            normalCountlens.append(normalCount)
    else:
        normalCountlens.append(normalCount)
        print("Normal Index Count: ", sortedNormal[i], " TOTAL ", sortedNormal[i][0], " = ", normalCount)
        normalCount = 0

# Die Erklauerung für der Unterschied zwischen die Verteilungen ist das bucketMapNaive() weis kleinere Indizes viel haufiger zu als bucketMap(). Dh, bei bucketMapNaive werden die Indizes kleiner gleich 8 nicht so viel zugewiesen wie die Indizes großer als 8. Grund dafür ist dass die multiplikation von r mit M liefert großere Zahlen zuruck schneller (Also, die Kurve hat eine Größere Steigung) als die Kurve von r**2 * M. Da wenn man eine Rationale zahl zum Quadrat erhöht, dann wir der Zahl kleiner wenn der nenner größer als der Zahler ist. Was in der Regel der Fall ist mit r

# Das hat als Konzequenz dass der Zahlen von bucketMap() nicht no schnell mit kleinere r Werte wachsten wie die von bucketMapNaive() was dazu führt dass die Indizes in ein Homogenerer Form verteilt werden.

#Aufgabe 2b

def chi2Test(bucket_lens, N):
    c = N/M
    chi2 = 0
    for nk in range(len(bucket_lens)):
        chi2 += (bucket_lens[nk]-c)**2/c
    print(chi2)
    tau = math.sqrt(2*chi2)-math.sqrt(2*M-3)
    if math.fabs(tau) > 3:
        return False
    else:
        return True
        
chi2Test(normalCountlens, 200)
chi2Test(naiveCountlens, 200)

#b) Mit verschiedenen M und N zeigt sich, dass 
# der Test bei der naiven Implementierung meistens 
# fehlschlägt und für die normale jedes Mal bestätigt
# wird, dass die Werte gleich verteilt sind.

def insertionSort(a):
    N = len(a)
    
    for i in range(N):
        current = a[i]
        j = i
        while j > 0:
            if current < a[j-1]:
                a[j] = a[j-1]
            else:
                break
            j -=1
        a[j] = current

# aufgabe 2c

# hilfe funktion für die tests
def createRandomArray(length):
    arr = []
    for i in range(length):
        arr.append(random.randint(-100,100))
    return arr

def bucketSort(a, bucketMap, d = 5):
    if len(a) == 0: return []
    N = len(a)
    M = int(N/float(d))
    
    buckets = [[]for k in range(M)]
    
    for k in range(len(a)):
        index = bucketMap(a[k], M)
        buckets[index].append(a[k])
        
    start = 0
    
    for k in range(M):
        insertionSort(buckets[k])
        end= start+ len(buckets[k])
        a[start:end] = buckets[k]
        start += len(buckets[k])
        
def testBucketSort(unsort):
    sort = sorted(unsort)
    bucketSort(unsort, bucketMap, 5)
    if sort == unsort:
        return True
    else:
        return False

from copy import deepcopy

class bucketSortTests(unittest.TestCase):
    def setUp(self):
        self.testArrays = [
            createRandomArray(20),
            createRandomArray(15),
            createRandomArray(0),
            createRandomArray(5),
        ],

    def test_Sorting(self):
        for i in range(len(self.testArrays)):
            for j in range(len(self.testArrays[i])):
                actualArray = self.testArrays[i][j]
                arrayCopy = deepcopy(actualArray)
                bucketSort(actualArray, bucketMap)
                arrayCopyComparison = sorted(arrayCopy)
                self.assertEqual(len(actualArray), len(arrayCopyComparison), "The list does not have the same length")
                self.assertListEqual(arrayCopyComparison, actualArray, "The array is not sorted properly")


if __name__ == "__main__":
    unittest.main()

dataneu = createData(200)
testBucketSort(dataneu)
#BucketSort funktioniert

import timeit
import matplotlib.pyplot as plt

t = []
t_naive = []
size = []
for n in range(1000,10001,1000):
    timer_1 = timeit.Timer(stmt= 'bucketSort(a,bucketMap, 5)',
                           setup = 'from __main__ import insertionSort,'+
                           'bucketSort, bucketMap, createData \n' +
                           'a = createData('+ str(n) + ')\n')
    timer_2 = timeit.Timer(stmt= 'bucketSort(a,bucketMapNaive, 5)',
                           setup = 'from __main__ import insertionSort,'+
                           'bucketSort, bucketMapNaive, createData \n' +
                           'a = createData('+ str(n) + ')\n')
    time_1 = timer_1.repeat(repeat = 10, number = 1)
    time_2 = timer_2.repeat(repeat = 10, number = 1)
    t.append(min(time_1))
    t_naive.append(min(time_2))
    size.append(n)

plt.xlabel('Anzahl der Elemente')
plt.ylabel('Laufzeit [s]')
plt.title('Laufzeit bucketSort')
plt.axis([0,10100,0,0.008])
plt.plot(size,t,'ro', label='bucketMap')
plt.plot(size,t_naive,'b*', label='bucketMapNaive')
plt.legend(loc='upper left')
plt.show()

#an dem Diagramm zeigt sich das lineare Wachstum
