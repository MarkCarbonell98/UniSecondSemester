
import unittest, random

def rotateLeft(node):
    newRoot = node.right
    node.right = newRoot.left
    newRoot.left = node
    return newRoot

def rotateRight(node):
    newRoot = node.left
    node.left = newRoot.right
    newRoot.right = node
    return newRoot

class NodeRandom:
    def __init__(self, key):
        self.key = key
        self.priority = random.randint(-100,100)
        self.left = self.right = None

class NodeDynamic:
    def __init__(self,key,priority):
        self.key = key
        self.priority = priority
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
                return
            elif key > i.key:
                if i.right == None:
                    i.right = newNode
                    self.size += 1
                    self.reheap(i)
                    return self
                i = i.right
            elif key < i.key:
                if i.left == None:
                    i.left = newNode
                    self.reheap(i)
                    self.size += 1
                    return self
                i = i.left

randomTreap = RandomTreap()
randomTreap.insert(1)
randomTreap.insert(2)
randomTreap.insert(3)
randomTreap.insert(4)
print(randomTreap.inorderTraversal())

dynamicTreap = DynamicTreap()
dynamicTreap

