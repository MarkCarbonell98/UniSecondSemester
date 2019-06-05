import unittest
import newTreap

class TreeTests(unittest.TestCase):

    def __init__(self, *args):
        super().__init__(*args)
        self.keyValue = 7              # Im Test soll key == value/keyValue sein 

    
    def buildDynamicTree(self):
        """baut einen Testbaum"""
        t = Node(3)
        t.priority = 1
        t.right = Node(5)
        t.right.priority = 5




    def buildTree1(self):
        """Baut einen Testbaum"""
        #Benutze kein treeInsert da wir dies explizit testen wollen
        t = Node(0)
        t.right = Node(4)
        t.right.right = Node(5)
        u = t.right.left = Node(2)
        u.left = Node(1)
        u.right = Node(3)
        return t

    def  buildRandomTree2(self):
        """build an unbalanced test tree"""
        
        t = Node(0)
        t.right = Node(1)
        t.right.right = Node(2)
        t.right.right.right = Node(3)
        t.right.right.right.right = Node(4)
        return t
        
    def  buildTree_native(self):
        t = SearchTree()
        t.insert(0)
        t.insert(4)   # Im Test soll key == value/keyValue sein 
        t.insert(2)
        t.insert(5)
        t.insert(1)
        t.insert(3)
        return t

    def test_insert(self):
        t=self.buildTree_native()
        self.assertEqual(0, t.root.key)
        self.assertEqual(None, t.root.left)
        self.assertEqual(4, t.root.right.key)
        
        self.assertEqual(2, t.root.right.left.key)
       
        self.assertEqual(5, t.root.right.right.key)
        
        self.assertEqual(None, t.root.right.right.right)
        self.assertEqual(None, t.root.right.right.left)
        self.assertEqual(1, t.root.right.left.left.key)
        
        self.assertEqual(3, t.root.right.left.right.key)
        

        self.assertEqual(None, t.root.right.left.left.left)
        self.assertEqual(None, t.root.right.left.left.right)
        self.assertEqual(None, t.root.right.left.right.left)
        self.assertEqual(None, t.root.right.left.right.right)

        self.assertTrue(treeEqual(t.root, self.buildTree1()))

    def test_remove1(self):
        t = self.buildTree_native()
        t.remove(5)
        t.remove(4)
        
        self.assertEqual(0, t.root.key)
        self.assertEqual(2, t.root.right.key)
        self.assertEqual(1, t.root.right.left.key)
        self.assertEqual(3, t.root.right.right.key)
        self.assertRaises(KeyError, t.remove, 10)
        
    def test_find(self):
        t = self.buildTree_native()
        for ii in range(6):
            node = t.find(ii)
            self.assertTrue(isinstance(node, Node),"did not find %u in tree" % ii)
            self.assertEqual(node.key, ii, "tree.find returned wrong node")
        for ii in range(6, 10):
            self.assertIs(t.find(ii), None, "found %u in tree" % ii)
        for ii in range(1, 10):
            self.assertIs(t.find(-ii), None, "found %d in tree" % -ii)

    def test_depth(self):
        t = self.buildTree_native()
        self.assertEqual(4, t.depth())
        self.assertEqual(0, SearchTree().depth())