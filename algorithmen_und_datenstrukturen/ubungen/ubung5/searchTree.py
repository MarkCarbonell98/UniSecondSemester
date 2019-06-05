from copy import deepcopy

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = self.right = None

class SearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def insert(self,key, value):
        newNode = Node(key, value)
        if not self.root:
            self.root = newNode
            self.size += 1
            return self
        
        i = self.root
        while True:
            if key == i.key: 
                i.value = value
                return self
            if key < i.key:
                if i.left == None:
                    i.left = newNode
                    self.size += 1
                    return self
                i = i.left
            else:
                if i.right == None:
                    i.right = newNode
                    self.size += 1
                    return self
                i = i.right

    def minRightKeyNode(self, node):
        node = node.left
        while node.right != None:
            node = node.right
        return node



    def depth(self, node = None, count = 0):
        if node == None and count == 0:
            node = self.root
        if node == None: return 0
        left = self.depth(node.left, count + 1)
        right = self.depth(node.right, count + 1)
        return max(left, right) + 1

    def remove(self, key, node = None, counter = 0):
        if self.find(key) == None: raise KeyError("The key " + key + " was not found in this tree")
        if node == None and counter == 0:
            node = self.root
        if node is None:
            return node
        if key < node.key:
            node.left = self.remove(key, node.left, counter + 1)
        elif key > node.key:
            node.right = self.remove(key, node.right, counter + 1)
        else:

            if node.left == None and node.right == None:
                node = None
            elif node.left == None:
                node = node.right
            elif node.right == None:
                node = node.left
            else:
                minRightSubtreeNode = self.minRightKeyNode(node)
                node.key = minRightSubtreeNode.key
                node.value = minRightSubtreeNode.value
                node.left = self.remove(minRightSubtreeNode.key, node.left,  counter + 1)
        return node

    def find(self, key):
        if not self.root:
            return None
        i = self.root
        while True:
            if not i: return None
            if key < i.key:
                i = i.left
                continue
            elif key > i.key:
                i = i.right
                continue
            else:
                return i


#aufgabe a)
tree = SearchTree()
tree.insert(7, 'alpha')
tree.insert(4, 'beta')
tree.insert(5, 'charlie')
tree.insert(6, 'delta')
tree.insert(1, 'echo')
tree.insert(2, 'foxtrot')
tree.insert(4, 'golf')
tree.insert(10, 'halo')
tree.insert(12, 'india')
tree.insert(15, 'jackson')
tree.insert(-1, 'kilo')

#             7
#         4        10
#     1        5        12
#  -1       2    6          15


print(tree.BFTraversal())
tree.remove(15)
print(tree.BFTraversal())
tree.remove(7)
print(tree.BFTraversal())
tree.remove(-1)
print(tree.find(-1))


#aufgabe b)
print(tree.depth())

# coding=utf8
#aufgabe c)
# '''
#     Um ein balanciertes Baum mit minimaler Tiefe zu erhalten, konnen wir das Folgender Algorithmus verwenden um die Reihenfolge von der Schlüsseln zu bestimmen.
#     Ang. wir haben ein Abzaehlbares, endliches Interval von Zahlen mit x,y element der ganze Zahlen, dass unter der Ordnungsrelation <= sortiert sind, dann folgt

#     Daten = [x, x + 1, x + 2, ... , y - 1, y ]

#     Dann konnen wir eine Binäre Suche auf unsere Daten implementieren, sodass jeder ausgewählte Zahl nach unser Binäre Suchbaum hinzugefügt wird, dies entspricht unsere Reihenfolge

#     1) Eine Zahl aus der Mitte von unsere Daten wählen und ins BST hinzufügen

#     2) Das gleiche rekursiv mit der rechte und linke Seite der  Daten tun sodass

#         2.1) Nimm der Zahl in der Mitte der linke Hälfte von unsere Daten und fügt ihn in der Baum hinzu

#         2.2) Nimm der Zahl inder Mitte der rechte Hälfte der Daten, und addiere es ins Baum

#     Somit erzeugen wir eine Reihenfolge dass mit X anfängt ( in der mitte der Daten), sodass, der nachste hinzugefügte Zahl kleiner als X ist, und das nachste größer als X. Danach eine Zahl dass kleiner als der kleinste X ist, und dann einer dass größer als die kleinste X ist und auch größer als die würzel Und so weiter. Somit entsteht ein Baum mit minimaler Tiefe.
    
# '''


#aufgabe d)

#     Die Aussage ist leicht durch ein Gegenbeispiel widergelegt.

#     Betrachten wir folgender BST, sei X = 1 und Y = 2

#                 5
#               /
#             2 <== Y
#           /  \
#     x ==>1     4
#              /
#             3

#     Fall 1. Wir entfernen X zu erst, bleibt Y übrig


#                 5
#               /
#             2 <== Y
#              \
#               4
#              /
#             3

#     Jetzt entfernen wir Y, dass nur einen Child Node, hat und bleibt folgender baum übrig

#                 5 (*)
#               /
#               4
#              /
#             3


#     Fall 2. Wir entfernen zu erst Y, also 2, bleibt folgender Baum übrig

#                 5
#               /
#             3
#            /  \
#     x ==> 1    4


#     Wir entfernen jetzt aber X, also 1, bleibt folgender Baum übrig da X ein Blatt ist...

#                 5  (**)
#               /
#             3
#              \
#               4

#     Da (*) != (**), somit wird die Aussage widerlegt Q.E.D.

