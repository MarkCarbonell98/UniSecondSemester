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

#aufgabe b
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
print(randomTreap.root)

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

print(dynamicTreap.root)







import unittest

class TestTreap(unittest.TestCase):
    def setUp(self):
        self.rt = RandomTreap()
        self.rt2 = RandomTreap()
        self.dt = DynamicTreap()
        self.dt2 = DynamicTreap()

    def test_insert(self):
        self.rt.insert(1)
        self.rt.insert(-1)
        self.rt.insert(3)
        self.rt.insert(-4)

        # assert self.rt.root.key == 1
        # assert self.rt.root.right.key == 3
        # assert self.rt.root.left.key == -1
        # assert self.rt.root.left.right == None
        # assert self.rt.root.left.left.key == -4

    def test_treapEquals(self):
        self.rt.insert(1)
        self.rt.insert(-1)
        self.rt.insert(3)
        self.rt.insert(-4)

        self.rt2.insert(1)
        self.rt2.insert(-1)
        self.rt2.insert(3)
        self.rt2.insert(-4)

        self.assertTrue(not treapEqual(self.rt.root, self.rt2.root))
        self.as

        self.dt.insert(1)
        self.dt.insert(-1)
        self.dt.insert(3)
        self.dt.insert(-4)

        self.dt2.insert(1)
        self.dt2.insert(-1)
        self.dt2.insert(3)
        self.dt2.insert(-4)

        self.assertTrue(treapEqual(self.dt.root, self.dt2.root))


if __name__ == '__main__':
    unittest.main()