import random, math

def createData(size):
    a = []
    while len(a) < size:
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        r = math.sqrt(x**2 + y**2)
        if r < 1.0:
            a.append(r)
    return a


def bucketMapNaive(r, M):
    return int(r * M)

def bucketMap(r, M):
    return int(r**2 * M)

data = createData(200)
M = 20

naiveData = []
normalData = []
for num in data:
    naiveIndex = bucketMapNaive(num, M)
    index = bucketMap(num, M)
    naiveData.append((naiveIndex, num))
    normalData.append((index, num))

sortedNaive = sorted(naiveData, key=lambda x: x[1])
sortedNormal = sorted(normalData, key=lambda x: x[1])

for i in range(len(sortedNaive)):
    print("Naive: ", sortedNaive[i], " Normal: ", sortedNormal[i])

naiveCount = 0 
for i in range(len(sortedNaive) - 1):
    if sortedNaive[i][0] == sortedNaive[i + 1][0]:
        naiveCount += 1
        print("Naive Index Count: ", sortedNaive[i], sortedNaive[i][0], " = ", naiveCount)
    else: 
        print("Naive Index Count: ", sortedNaive[i], " TOTAL ", sortedNaive[i][0], " = ", naiveCount)
        naiveCount = 0

normalCount = 0
for i in range(len(sortedNormal) - 1):
    if sortedNormal[i][0] == sortedNormal[i + 1][0]:
        normalCount += 1
        print("Normal Index Count: ", sortedNormal[i], sortedNormal[i][0], " = ", normalCount)
    else: 
        print("Normal Index Count: ", sortedNormal[i], " TOTAL ", sortedNormal[i][0], " = ", normalCount)
        normalCount = 0

# Die Erklauerung für der Unterschied zwischen die Verteilungen ist das bucketMapNaive() weis kleinere Indizes viel haufiger zu als bucketMap(). Dh, bei bucketMapNaive werden die Indizes kleiner gleich 8 nicht so viel zugewiesen wie die Indizes großer als 8. Grund dafür ist dass die multiplikation von r mit M liefert großere Zahlen zuruck schneller (Also, die Kurve hat eine Größere Steigung) als die Kurve von r**2 * M. Da wenn man eine Rationale zahl zum Quadrat erhöht, dann wir der Zahl kleiner wenn der nenner größer als der Zahler ist. Was in der Regel der Fall ist mit r

# Das hat als Konzequenz dass der Zahlen von bucketMap() nicht no schnell mit kleinere r Werte wachsten wie die von bucketMapNaive() was dazu führt dass die Indizes in ein Homogenerer Form verteilt werden.
