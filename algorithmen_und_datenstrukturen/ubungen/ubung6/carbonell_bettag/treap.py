
import unittest, random

# Aufgabe a

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

#aufgabe b

class NodeRandom:
    def __init__(self, key):
        self.key = key
        self.priority = random.randint(-100,100)
        self.left = self.right = None

class NodeDynamic:
    def __init__(self,key):
        self.key = key
        self.priority = 1
        self.left = self.right = None

class RandomTreap:
    def __init__(self):
        self.root = None
        self.size = 0

    def getParentNode(self, child):
        if not self.root:
            return None
        if child.key == self.root.key:
            return child
        
        i = self.root
        while i.key != child.key and i:
            if child.key == i.key: return i
            if child.key < i.key and i.left:
                if i.left.key == child.key:
                    return i
                i = i.left
            elif child.key > i.key and i.right:
                if child.key == i.right.key:
                    return i
                i = i.right
            else:
                return i
        
    def reheap(self, root):
        if root.left and root.right:
            if root.left.priority > root.priority:
                root = rotateRight(root)
            elif root.right.priority > root.priority:
                root = rotateLeft(root)
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

    def getParentNode(self, child):
        if not self.root:
            return None
        if child.key == self.root.key:
            return child
        
        i = self.root
        while i.key != child.key and i:
            if child.key == i.key: return i
            if child.key < i.key and i.left:
                if i.left.key == child.key:
                    return i
                i = i.left
            elif child.key > i.key and i.right:
                if child.key == i.right.key:
                    return i
                i = i.right
            else:
                return i

    # aufgabe e
    def top(self ,min_priority):
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
    
    def reheap(self, root):
        if root.left and root.right:
            if root.left.priority > root.priority:
                root = rotateRight(root)
            elif root.right.priority > root.priority:
                root = rotateLeft(root)
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
                return i
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

dynamicTreap = DynamicTreap()
dynamicTreap.insert(99)
dynamicTreap.insert(100)
dynamicTreap.insert(101)
dynamicTreap.insert(101)
dynamicTreap.root.priority = 101
dynamicTreap.root.right.priority = 101

#c)
def fileToTreaps(name):
    filename = name
    s = open(filename, encoding="latin-1").read()
    for k in ',;.:-"\'!?':
        s = s.replace(k, '')

    s = s.lower()
    text = s.split()
    rt = RandomTreap()
    dt = DynamicTreap()

    for word in text:
        rt.insert(word)
        dt.insert(word)
    return rt, dt

print(dynamicTreap.top(100))


dieDreiMusketiereTreaps = fileToTreaps('die-drei-musketiere.txt')
casanovaErinnerungenBand2Treaps = fileToTreaps('casanova-erinnerungen-band-2.txt')
helmholtzNaturwissenschaftenTreaps = fileToTreaps('helmholtz-naturwissenschaften.txt')

def compareTrees(tree1, tree2):
    if tree1 == None and tree2 is None:
        return True
    elif tree1 != None and tree2 != None:
        return tree1.priority == tree2.priority and compareTrees(tree1.left, tree2.left) and compareTrees(tree1.right, tree2.right)
    else:
        return False

print(compareTrees(dieDreiMusketiereTreaps[0].root, dieDreiMusketiereTreaps[1].root))
print(compareTrees(casanovaErinnerungenBand2Treaps[0].root, casanovaErinnerungenBand2Treaps[1].root))
print(compareTrees(helmholtzNaturwissenschaftenTreaps[0].root, helmholtzNaturwissenschaftenTreaps[1].root))

#tests laufen nicht :(
class TestTreaps(unittest.TestCase):    
    
    def buildRandomTreap(self):
        t = RandomTreap()
        t.insert(1)
        t.insert(2)
        t.insert(3)
        t.insert(4)
        return t

    def  buildDynamicTreap(self):
        t = DynamicTreap()
        t.insert(1)
        t.insert(2)
        t.insert(3)
        t.insert(4)
        return t

    def test_insert(self):
        t=self.buildDynamicTreap()
        self.assertEqual(t.root.key, 1)
        self.assertEqual(t.root.left.key, 2)
        self.assertEqual(t.root.right.key, 3)
        self.assertEqual(t.root.right.key, 4)

if __name__ == '__main__':
    unittest.main()




