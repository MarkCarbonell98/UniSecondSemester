import random

# aufgabe A
def rotateLeft(root):
    newRoot = root.right
    root.right = newRoot.left
    newRoot.left = root
    return newRoot

def rotateRight(root):
    newRoot = root.left
    root.left = newRoot.right
    newRoot.right = root
    return newRoot

#Aufgabe b
class Node:
    def __init__(self, key):
        self.key = key
        self.priority = 1
        self.left = self.right = None
    
    def __repr__(self):
        return f"Node({self.key}, {self.priority}, left: {self.left}, right: {self.right})"

class RandomTreap:
    def __init__(self):
        self.root = None
        self.size = 0

    def __insert(self, node, key):
        if not node:
            self.size += 1
            newNode = Node(key)
            newNode.priority = random.randint(-100, 100)
            return newNode
        if key <= node.key and node.left:
            node.left = self.__insert(node.left, key)
            if node.left.priority > node.priority:
                node = rotateRight(node)
        else:
            node.right = self.__insert(node.right,key)
            if node.right.priority > node.priority:
                node = rotateLeft(node)
        return node

    def insert(self, key):
        self.root = self.__insert(self.root, key)

    def __repr__(self):
        return repr(self.root)

    def __depth(self, node):
        if node is None:
            return 0
        else:
            return max(self.__depth(node.left), self.__depth(node.right)) + 1

    def depth(self):
        return self.__depth(self.root)

class DynamicTreap:
    def __init__(self):
        self.root = None
        self.size = 0

    def __insert(self, node, key):
        if not node:
            self.size += 1
            return Node(key)
        if key == node.key:
            node.priority += 1
            if node.left and node.left.priority > node.priority:
                node = rotateRight(node)
            elif node.right and node.right.priority > node.priority:
                node = rotateLeft(node)
        elif key < node.key and node.left:
            node.left = self.__insert(node.left, key)
            if node.left.priority > node.priority:
                node = rotateRight(node)
        else:
            node.right = self.__insert(node.right,key)
            if node.right.priority > node.priority:
                node = rotateLeft(node)
        return node

    def insert(self, key):
        self.root = self.__insert(self.root, key)

    def __repr__(self):
        return repr(self.root)

    def __depth(self, node):
        if node is None:
            return 0
        else:
            return max(self.__depth(node.left), self.__depth(node.right)) + 1

    def depth(self):
        return self.__depth(self.root)

    def top(self, min_priority):
        if not self.root:
            return None
        i = self.root
        queue, visited = [i], []
        while(len(queue)):
            i = queue.pop(0)
            if i.priority > min_priority:
                visited.append((i.key, i.priority))
            if i.left:
                queue.append(i.left)
            if i.right:
                queue.append(i.right)
        return visited

    def __sorted(self, node):
        if node == None:
            yield from self.__sorted(node.left)
            yield node
            yield from self.__sorted(node.right)

    def sorted(self):
        return self.__sorted(self.root)

# zip funktion nimmt zwei generators und gibt einen Zahl von einen Generator nach dem anderen. Gleichzeitig

# @given(definiert parametern fuer eine bestimmte funktion)
def treapEqual(t1, t2):
    if t1 == None and t2 == None:
        return True
    elif t1 != None and t2 != None:
        return t1.key == t2.key and treapEqual(t1.right, t2.right) and treapEqual(t1.left, t2.left)
    else:
        return False


randomTreap = RandomTreap()
randomTreap.insert(1)
randomTreap.insert(-1)
randomTreap.insert(3)
randomTreap.insert(-4)
randomTreap.insert(6)
randomTreap.insert(-9)
randomTreap.insert(204)
randomTreap.insert(-201)
randomTreap.insert(1* 20)
randomTreap.insert(-1* 20)
randomTreap.insert(3* 20)
randomTreap.insert(-4* 20)
randomTreap.insert(6* 20)
randomTreap.insert(-9* 20)
randomTreap.insert(204* 20)
randomTreap.insert(-201* 20)
# print(randomTreap.root)

dynamicTreap = DynamicTreap()
dynamicTreap.insert(1)
dynamicTreap.insert(-1)
dynamicTreap.insert(3)
dynamicTreap.insert(-4)
dynamicTreap.insert(6)
dynamicTreap.insert(-9)
dynamicTreap.insert(204)
dynamicTreap.insert(-201)
dynamicTreap.insert(1* 20)
dynamicTreap.insert(-1* 20)
dynamicTreap.insert(3* 20)
dynamicTreap.insert(-4* 20)
dynamicTreap.insert(6* 20)
dynamicTreap.insert(-9* 20)
dynamicTreap.insert(204* 20)
dynamicTreap.insert(-201* 20)
dynamicTreap.insert(-201* 20)
dynamicTreap.insert(-201* 20)
dynamicTreap.insert(-201* 20)

# print(dynamicTreap.root)



# aufgabe c

lengthOfTexts = []

# File einlesen und nach Unicode konvertieren (damit Umlaute korrekt sind)
def createRandomAndDynamicTreap(filename):
    filename = "die-drei-musketiere.txt"
    s = open(filename, encoding="latin-1").read()
    for k in ',;.:-"\'!?':
        s = s.replace(k, '') # Sonderzeichen entfernen
    s = s.lower() # Alles klein schreiben
    text = s.split() # String in Array von Wörtern umwandeln
    print(f"Total amount of words in text {filename} is {len(text)}")
    lengthOfTexts.append(len(text))
    rt = RandomTreap()
    dt = DynamicTreap()
    for word in text:
        rt.insert(word)
        dt.insert(word)
    return rt,dt

dreiMusketiereWords = createRandomAndDynamicTreap('die-drei-musketiere.txt')
helmholtz = createRandomAndDynamicTreap("helmholtz-naturwissenschaften.txt")
casanova = createRandomAndDynamicTreap("casanova-erinnerungen-band-2.txt")

print(treapEqual(dreiMusketiereWords[0].root, dreiMusketiereWords[1].root))

print(treapEqual(helmholtz[0].root, helmholtz[1].root))

print(treapEqual(helmholtz[0].root, helmholtz[1].root))


# aufgabe d

print(f"Die drei muskeitere enthalt {dreiMusketiereWords[0].size} verschiede worter")
print(f"Helmholtz enthalt {helmholtz[0].size} verschiede worter")
print(f"Casanova enthalt {casanova[0].size} verschiede worter")

# Ein perfekt balancierter Baum mit n elementen enthalt genau der tiefe t = log basis sigma(n) wo sigma der Goldene Schnitt ist

#in dem fall sollte der Tiefe von unsere Treaps ungefahr 25,5... sein. Ist aber mehr als das doppelte davon

print(f"depth of Die Drei Musketiere RandomTreap: {dreiMusketiereWords[0].depth()}, DynamicTreap: {dreiMusketiereWords[1].depth()}")
print(f"depth of Helmholtz RandomTreap: {dreiMusketiereWords[0].depth()}, DynamicTreap: {dreiMusketiereWords[1].depth()}")
print(f"depth of Casanova RandomTreap: {dreiMusketiereWords[0].depth()}, DynamicTreap: {dreiMusketiereWords[1].depth()}")

n = 165594
N1 = lengthOfTexts[0]
N2 = lengthOfTexts[1]
N3 = lengthOfTexts[2]

def getDepthOfNode(node, key, level = 1):
    if node == None:
        return 0
    if node.key == key:
        return level
    downLevel = getDepthOfNode(node.left, key, level + 1)
    if downLevel != 0:
        return downLevel
    downLevel = getDepthOfNode(node.right, key,level + 1)
    return downLevel

def getAllNodes(root):
    if not root:
        return None
    i = root
    queue, visited = [i], []
    while(len(queue)):
        i = queue.pop(0)
        visited.append(i)
        if i.left:
            queue.append(i.left)
        if i.right:
            queue.append(i.right)
    return visited

def mittlereTiefe(treap, amountOfWordsInTreap):
    result = 0
    allNodes = getAllNodes(treap.root)
    for i in range(len(allNodes)):
        node = allNodes[i]
        result += getDepthOfNode(node, node.key)
    return result/amountOfWordsInTreap

print(mittlereTiefe(dreiMusketiereWords[0], n), mittlereTiefe(dreiMusketiereWords[1], n))
print(mittlereTiefe(helmholtz[0], n), mittlereTiefe(helmholtz[1], n))
print(mittlereTiefe(casanova[0], n), mittlereTiefe(casanova[1], n))

def mittlereZugriffzeit(treap, amountOfWordsInText):
    result = 0
    allNodes = getAllNodes(treap.root)
    for i in range(len(allNodes)):
        node = allNodes[i]
        result += getDepthOfNode(node, node.key)
    return result/amountOfWordsInText

print(mittlereZugriffzeit(dreiMusketiereWords[0],N1), mittlereZugriffzeit(dreiMusketiereWords[1],N1))
print(mittlereZugriffzeit(helmholtz[0],N2), mittlereZugriffzeit(helmholtz[1],N2))
print(mittlereZugriffzeit(casanova[0],N3), mittlereZugriffzeit(casanova[1],N3))

# Die dynamische Treap hat eine geringere Zugriffzeit als die randomisierte Treap


import unittest

class TestTreap(unittest.TestCase):
    def setUp(self):
        self.rt = RandomTreap()
        self.rt2 = RandomTreap()
        self.dt = DynamicTreap()
        self.dt2 = DynamicTreap()

    def test_insert(self):
        self.rt.root = Node(2)
        self.rt.root.left = Node(1)
        self.rt.root.right = Node(0)
        self.rt.root.left.left = Node(-1)
        self.rt.root.left.right = Node(20)

        # assert self.rt.root.key == 1
        # assert self.rt.root.right.key == 3
        # assert self.rt.root.left.key == -1
        # assert self.rt.root.left.right == None
        # assert self.rt.root.left.left.key == -4

    def test_treapEqual(self):
        self.dt.insert(1)
        self.dt.insert(-1)
        self.dt.insert(3)
        self.dt.insert(-4)

        self.dt2.insert(1)
        self.dt2.insert(-1)
        self.dt2.insert(3)
        self.dt2.insert(-4)

        self.assertTrue(treapEqual(self.rt.root, self.rt2.root))


if __name__ == '__main__':
    unittest.main()

# AssertNodeValid, assertNodeEqual, assertTreapValid