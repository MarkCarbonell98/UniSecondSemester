
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

class Node:
    def __init__(self, key):
        self.key = key
        self.priority = random.randint(-100,100)
        self.left = self.right = None

class RandomTreap:
    def __init__(self):
        self.root = None
        self.size = 0

    def getParentNode(self, child):
        if not self.root:
            return None
        
        i = self.root
        while True:
            if child.key < i.key:
                if i.left and i.left.key == i.key:
                    return i
                i = i.left
            elif child.key > i.key:
                if i.right and i.right.key == i.key:
                    return i
                i = i.right
            else:
                return i


        

    def reheapRandomTreap(self, node):
        if node.left and node.right:
            if node.priority < node.left.priority:
                newRoot = rotateRight(node)
                node = newRoot
            elif node.priority < node.right.priority:
                newRoot = rotateLeft(node)
                node = newRoot
        
        parent = self.getParentNode(node)
        if parent.priority < node.priority and self.root and parent.key != self.root.key:
            self.reheapRandomTreap(parent)

    def insert(self,key):
        newNode = Node(key)
        if not self.root:
            self.root = newNode
            self.size += 1
            return self
        
        i = self.root
        while True:
            if key == i.key: 
                return
            if key < i.key:
                if i.left == None:
                    i.left = newNode
                    self.size += 1
                    self.reheapRandomTreap(i)
                    return self
                i = i.left
            else:
                if i.right == None:
                    i.right = newNode
                    self.size += 1
                    self.reheapRandomTreap(i)
                    return self
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

    def getParentNode(self, child):
        if not self.root:
            return None
        
        i = self.root
        while True:
            if child.key < i.key:
                if i.left and i.left.key == i.key:
                    return i
                i = i.left
            elif child.key > i.key:
                if i.right and i.right.key == i.key:
                    return i
                i = i.right
            else:
                return i

    def reheapDynamicTreap(self, node):
        if node.left and node.right:
            if node.priority < node.left.priority:
                newRoot = rotateRight(node)
                node = newRoot

            elif node.priority < node.right.priority:
                newRoot = rotateLeft(node)
                node = newRoot

        parent = self.getParentNode(node)
        if parent.priority < node.priority and self.root and parent.key != self.root.key:
            self.reheapDynamicTreap(parent)
    
    def insert(self,key):
        newNode = Node(key)
        if not self.root:
            self.root = newNode
            self.size += 1
            return self
        
        i = self.root
        while True:
            if key == i.key:
                i.priority += 1
                self.reheapDynamicTreap(i)
                return self
            elif key > i.key:
                if i.right == None:
                    i.right = newNode
                    self.size += 1
                    self.reheapDynamicTreap(i)
                    return self
                i = i.right
            elif key < i.key:
                if i.left == None:
                    i.left = newNode
                    self.reheapDynamicTreap(i)
                    self.size += 1
                    return self
                i = i.left
    def top(min_priority):
        pass

randomTreap = RandomTreap()
randomTreap.insert(1)
randomTreap.insert(2)
randomTreap.insert(3)
randomTreap.insert(4)

dynamicTreap = DynamicTreap()
dynamicTreap.insert(1)
dynamicTreap.insert(2)
dynamicTreap.insert(3)
dynamicTreap.insert(4)

