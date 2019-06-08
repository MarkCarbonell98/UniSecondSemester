import random

f = open("collisions.txt", "a+")

for i in range(10):
    f.write("This is a new line \n")

def hhash(s):
    h = 0
    for k in s:
        h = 23*h + ord(k)
    return h

# 0 + ord(a)
# ord(a) * 23 + ord(b) = b
# b * 23 + ord(c) = c
# c * 23 + ord(d)

def createKeys(length):
    keys = []
    seen = []
    modelHash = hhash("kalb")
    alphabet = [chr(c) for c in range(97, 123)]
    while len(keys) <= length:
        index1 = random.randint(0, len(alphabet)-1)
        index2 = random.randint(0, len(alphabet)-1)
        index3 = random.randint(0, len(alphabet)-1)
        index4 = random.randint(0, len(alphabet)-1)
        # randomString = alphabet[index1] + alphabet[index2] + alphabet[index3] + alphabet[index4]
        shortString = alphabet[index1] + alphabet[index2] + alphabet[index3] + alphabet[index4]
        newHash = hhash(shortString)
        if newHash == modelHash and not shortString in seen:
            keys.append((shortString, newHash))
        seen.append(shortString)
    return sorted(keys,key=lambda x: x[1], reverse=True), seen

print(createKeys(10))



# print(hhash("a"))
# print(hhash("b"))
# print(hhash("aa"))
# print(hhash("ab"))
# print(hhash("abc"))
# print(hhash("abcd"))
# print(hhash("bacd"))
# print(hhash("dbca"))

class HashNode:
    def __init__(self, key, data, next = None):
        self.key = key
        self.data = data
        self.next = next

class HashTable:
    def __init__(self):
        self.capacity = 11
        self.size = 0
        self.array = [None]*self.capacity

    def __setitem__(self, key, value):
        index = hhash(key % self.capacity)
        node = self.array[index]
        while node is None:
            if node.key == key:
                node.data = value
                return
            node = node.next
        self.array[index] = HashNode(key,value,self.array[index])
        self.size += 1
        if self.size == self.capacity:
            oldData = self.array
            newCapacity = 2 * self.capacity + 1
            newData = [None] * newCapacity
            for i in range(self.capacity):
                newData[i] = self.array[i]
            self.array = newData
            self.capacity = newCapacity

    def __getitem__(self, key):
        index = hhash(key) % self.capacity
        node = self.array[index]
        while node is None:
            if node.key == key:
                return node.data
            node = node.next
        raise KeyError(key)

hashTable = HashTable()
def generateRandomStrings():
    alphabet = []


class DoubleHashTable:
    def __init__(self):
        self.capacity = 11
        self.size = 0
        self.array = [None]*self.capacity

    def __setitem__(self, key, value):
        h = hash(key)
        index = h % self.capacity
        while True:
            if self.array[index] is None or self.array[index].key is None:
                # das Feld ist frei (1. Abfrage)
                # oder das Feld ist als frei markiert (2. Abfrage)
                self.array[index] = HashNode(key, value)
                self.size += 1
                ...  # eventuell muss hier die Kapazität optimiert werden
                return
            if self.array[index].key == key:
                # Es gibt diesen Schlüssel schon,
                # überschreibe die Daten
                self.array[index].data = value
                return
            # Letzter Fall: Kollision => neuer Index durch 2. Hashfunktion
            index = (5*index+1+h) % self.capacity
            h = h >> 5

    def __getitem__(self, key):
        h = hash(key)
        index = h % self.capacity
        while True:
            if self.array[index] is None or self.array[index].key is None:
                # Der Schlüssel existiert nicht
                raise KeyError(key)
            if self.array[index].key == key:
                # Schlüssel gefunden, gib die dazu gehörigen Daten aus
                return self.array[index].data
            index = (5*index+1+h) % self.capacity
            h = h >> 5
