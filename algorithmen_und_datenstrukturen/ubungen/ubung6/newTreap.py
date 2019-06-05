

import random
#Funktionen rotateLeft und rotateRight hinzugefuegt

def rotateLeft(rootnode):
    newRoot = rootnode.right
    rootnode.right = newRoot.left
    newRoot.left = rootnode
    return newRoot



def rotateRight(rootnode):
    newRoot = rootnode.left
    rootnode.left = newRoot.right
    newRoot.right = rootnode
    return newRoot


#Node aus Uebung 5 uebernommen und priority hinzugefuegt
class NodeRandom:
    def __init__(self, key):
        self.key = key
        self.priority = random.randint(-100, 100)
        self.left = self.right = None

    def __repr__(self):
        return "NodeRandom(" + str(self.key)  + ", " + str(self.priority) + ")"


class NodeDynamic:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority #piority-Attribut hinzugefuegt und auf 1 gesetzt
        self.left = self.right = None


class RandomTreap:
    def __init__(self):
        self.root = None
        self.size = 0

    def getParentNode(self, child, parent = None, count = 0):
        if not self.root:
            return None
        if parent == None and count == 0:
            parent = self.root
        if child.key == self.root.key:
            return child
        if parent.left:
            if parent.left.key == child.key:
                return ("L", parent)
        elif parent.right:
            if parent.right.key == child.key:
                return ("R", parent)
        else:
            self.getParentNode(child, parent.left, count + 1)
            self.getParentNode(child, parent.right, count + 1)


    def __find(self, node, key):
        if node is None:
            return None
        elif key < node.key:
            return self.__find(node.left, key)
        elif key > node.key:
            return self.__find(node.right, key)
        elif key == node.key:
            return node
        else:
            raise RuntimeError(f'Keys {key} and {node.key} do not compare')

    def find(self, key):
        return self.__find(self.root, key)

    def insert(self,key):
        newNode = NodeRandom(key)
        if not self.root:
            self.root = newNode
            self.size += 1
            return self
        
        fatherNode = None
        
        i = self.root
        while True:
            if key == i.key: 
                break
            if key < i.key:
                if i.left == None:
                    i.left = newNode
                    self.size += 1
                    # self.reheapTree(i)
                    break;
                    return (i, i.left)
                i = i.left
            else:
                if i.right == None:
                    i.right = newNode
                    self.size += 1
                    # self.reheapTree(i)
                    return (i, i.right)
                i = i.right

    def depth(self, node = None, count = 0):
        if node == None and count == 0:
            node = self.root
        if node == None: return 0
        left = self.depth(node.left, count + 1)
        right = self.depth(node.right, count + 1)
        return max(left, right) + 1


class DynamicTreap:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def insert(self,key, priority):
        newNode = NodeDynamic(key, priority)
        if not self.root:
            self.root = newNode
            self.size += 1
            return self
        
        i = self.root
        while True:
            if key == i.key: 
                i.priority += 1
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


    def depth(self, node = None, count = 0):
        if node == None and count == 0:
            node = self.root
        if node == None: return 0
        left = self.depth(node.left, count + 1)
        right = self.depth(node.right, count + 1)
        return max(left, right) + 1





#c)
# filename = "die-drei-musketiere.txt"
# s = open(filename, encoding="latin-1").read()
# for k in ',;.:-"\'!?':
#     s = s.replace(k, '')

# s = s.lower()
# text = s.split()

# rt = RandomTreap()
# dt = DynamicTreap()

# for word in text:
#     rt.insert(word)
#     dt.insert(word)
    
    



def compareTrees(tree1, tree2):
    if tree1 == None and tree2 is None:
        return True
    elif tree1 != None and tree2 != None:
        return tree1.priority == tree2.priority and compareTrees(tree1.left, tree2.left) and compareTrees(tree1.right, tree2.right)
    else:
        return False

randomTreap = RandomTreap()
randomTreap.insert(1)
randomTreap.insert(-1)
randomTreap.insert(2)
randomTreap.insert(5)
randomTreap.insert(-20)
randomTreap.insert(-40)
print(randomTreap.find(1))
print(randomTreap.find(-1))
print(randomTreap.find(-40))
print(randomTreap.getParentNode(randomTreap.find(1)))
print(randomTreap.getParentNode(randomTreap.find(-1)))
print(randomTreap.getParentNode(randomTreap.find(-40)))

dynamicTreap = DynamicTreap()
dynamicTreap.insert(1, 4)
dynamicTreap.insert(2, 10)
dynamicTreap.insert(-1, -10)
dynamicTreap.insert(10, -10)




