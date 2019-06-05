
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

    def getParentNode(self, child, root = None, count = 0):
        if not self.root:
            return None
        if self.root.key == child.key:
            return self.root
        if root == None and count == 0:
            root = self.root
        
        if root.left:
            if root.left.key == child.key:
                return root.left
        if root.right:
            if root.right.key == child.key:
                return root.right

        if not root.right or not root.left:
            return root

        self.getParentNode(child,root.left, count + 1)
        self.getParentNode(child,root.right, count + 1)
        
    def reheap(self, root):
        if root.left and root.right:
            if root.left.priority > root.priority:
                rotateRight(root)
            elif root.right.priority > root.priority:
                rotateLeft(root)
        parent = self.getParentNode(root)
        if parent.priority < root.priority and root.key != self.root.key:
            self.reheap(parent)

    def inorderTraversal(self, node = None,arr = [], count = 0):
        if node == None and count == 0:
            node = self.root
        elif node == None:
            return arr
        self.inorderTraversal(node.left, arr, count + 1)
        arr.append((node.key, node.priority))
        print(arr)
        self.inorderTraversal(node.right, arr, count + 1)
    
    def insert(self, key):
        newNode = NodeRandom(key)
        if self.root == None:
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

class DynamicTreap:
    def __init__(self):
        self.root = None
        self.size = 0

    def getParentNode(self, child, root = None, count = 0):
        if not self.root:
            return None
        if self.root.key == child.key:
            return self.root
        if root == None and count == 0:
            root = self.root
        
        if root.left:
            if root.left.key == child.key:
                return root.left
        if root.right:
            if root.right.key == child.key:
                return root.right

        if not root.right or not root.left:
            return root

        self.getParentNode(child,root.left, count + 1)
        self.getParentNode(child,root.right, count + 1)
        
    def reheap(self, root):
        if root.left and root.right:
            if root.left.priority > root.priority:
                rotateRight(root)
            elif root.right.priority > root.priority:
                rotateLeft(root)
        parent = self.getParentNode(root)
        if parent.priority < root.priority and root.key != self.root.key:
            self.reheap(parent)

    def inorderTraversal(self, node = None,arr = [], count = 0):
        if node == None and count == 0:
            node = self.root
        elif node == None:
            return arr
        self.inorderTraversal(node.left, arr, count + 1)
        arr.append((node.key, node.priority))
        print(arr)
        self.inorderTraversal(node.right, arr, count + 1)
    
    def insert(self, key):
        newNode = NodeRandom(key)
        if self.root == None:
            self.root = newNode
            self.size += 1
            return self
        
        i = self.root
        while True:
            if key == i.key:
                i.priority += 1
                parent = self.getParentNode(i)
                self.reheap(parent)
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
dynamicTreap.insert(1)
dynamicTreap.insert(2)
dynamicTreap.insert(3)
dynamicTreap.insert(4)
print(dynamicTreap.inorderTraversal())



