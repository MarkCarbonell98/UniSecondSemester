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


    def BFTraversal(self):
        if not self.root:
            return None
        i = self.root
        queue, visited = [i], []
        while(len(queue)):
            i = queue.pop(0)
            visited.append((i.key, i.value))
            if i.left:
                queue.append(i.left)
            if i.right:
                queue.append(i.right)
        return visited

    def depth(self, node = None, count = 0):
        if node == None and count == 0:
            node = self.root
        if node == None: return 0
        left = self.depth(node.left, count + 1)
        right = self.depth(node.right, count + 1)
        return max(left, right) + 1

    def remove(self, key, node = None, counter = 0):
        if self.find(key) == None: raise KeyError(f"The key {key} was not found in this tree")
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
tree.insert(2, 'falcon')
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

#aufgabe c)
'''
    
'''


#aufgabe d)

'''
    Die Aussage ist leicht durch ein Gegenbeispiel widergelegt.

    Betrachten wir folgender BST, sei X = 12 und Y = 18

                10
        5               12 <== X
    4       7       11          20
                            19      30     
                    Y ==> 18

    im code realisiert
'''

beweis = SearchTree()
beweis.insert(10, '')
beweis.insert(5, '')
beweis.insert(12, '')
beweis.insert(4, '')
beweis.insert(7, '')
beweis.insert(11, '')
beweis.insert(20, '')
beweis.insert(19, '')
beweis.insert(30, '')
beweis.insert(18, '')
print(beweis.BFTraversal())
beweisCopy = deepcopy(beweis)
print("Beweis Baum am Anfang: ", beweisCopy.BFTraversal())

# beim entfernung von X ergibt sich folgendes

beweis.remove(12)
print(beweis.BFTraversal())

#beim entwernung von Y ergibt sich dann
beweis.remove(18)
print(beweis.BFTraversal()) 

#angenommen dass die aussage Wahr ist, dann sollte sich genau der selbe Baum ergeben im umgekehrter Reihenfolge...
# beim entfernung von X ergibt sich folgendes

beweisCopy.remove(18)
print(beweisCopy.BFTraversal())

#beim entwernung von Y ergibt sich dann
beweisCopy.remove(12)
print(beweisCopy.BFTraversal()) 









