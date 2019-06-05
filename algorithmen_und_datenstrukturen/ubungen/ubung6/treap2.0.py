import random

def rotationLeft(root):
    newRoot = root.right
    root.right = newRoot.left
    newRoot.left = root
    return newRoot

def rotateRight(root):
    newRoot = root.left
    root.left = newRoot.right
    newRoot.right = root
    return newRoot

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

    def getParentNode(self, node):
        if not self.root:
            return None
        
        if node.key == self.root.key:
            return node

        i = self.root
        queue, visited = [i], []
        while len(queue):
            i = queue.pop(0)
            visited.append(i)
            if i.left:
                queue.append(i.left)
                if i.left.key == node.key:
                    return i
            if i.right:
                queue.append(i.right)
                if i.right.key == node.key:
                    return i
        raise AttributeError("The parent node is not in the tree")

    def __insert(self,node,key):
        if node is None: 
            newNode = Node(key)
            newNode.priority = random.randint(-100, 100)
            return newNode
        if node.key == key:
            return node
        if key < node.key:
            node.left  = self.__insert(node.left, key)
        else:
            node.right = self.__insert(node.right, key)
        return node

    def insert(self, key):
        self.root = self.__insert(self.root, key)

    def reheap(self,node):
        if not self.root:
            return None

        if self.root.key == node.key:
            return self.root

        if node.left and node.right:
            if node.left.priority > node.priority:
                node = rotateRight(node)
            elif node.right.priority > node.priority:
                node = rotationLeft(node)
        
        parent = self.getParentNode(node)
        if parent.priority < node.priority:
            self.reheap(parent)
        return node

    def __repr__(self):
        return repr(self.root)
    
def treapEqual(t1, t2):
    if t1 == None and t2 == None:
        return True
    elif not t1 and t2 != None:
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
print(randomTreap.root)
# print(randomTreap.getParentNode(randomTreap.root))
# print(randomTreap.getParentNode(randomTreap.root.left))
# print(randomTreap.getParentNode(randomTreap.root.right))
# print(randomTreap.getParentNode(randomTreap.root.left.left))
# print(randomTreap.getParentNode(randomTreap.root.left.left.left))
# print(randomTreap.root.left.left.left)
print(randomTreap.reheap(randomTreap.root))
print(treapEqual(randomTreap.root, randomTreap.reheap(randomTreap.root)))


# print(randomTreap.reheap())

import unittest

class TestTreap(unittest.TestCase):
    def setUp(self):
        self.rt = RandomTreap()
        self.rt2 = RandomTreap()

    def test_insert(self):
        self.rt.insert(1)
        self.rt.insert(-1)
        self.rt.insert(3)
        self.rt.insert(-4)

        assert self.rt.root.key == 1
        assert self.rt.root.right.key == 3
        assert self.rt.root.left.key == -1
        assert self.rt.root.left.right == None
        assert self.rt.root.left.left.key == -4

    def test_treapEquals(self):
        self.rt.insert(1)
        self.rt.insert(-1)
        self.rt.insert(3)
        self.rt.insert(-4)

        self.rt2.insert(1)
        self.rt2.insert(-1)
        self.rt2.insert(3)
        self.rt2.insert(-4)

        self.assertTrue(treapEqual(self.rt, self.rt2))



if __name__ == '__main__':
    unittest.main()