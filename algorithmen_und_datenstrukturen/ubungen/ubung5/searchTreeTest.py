import unittest
import random
import string

from searchTree import Node, SearchTree

class TestSearchTree(unittest.TestCase):

    def setUp(self):
        tree = SearchTree()
        someNumber = random.randin(1,20)
        for i in range(someNumber):
            tree.insert(random.randint(-1000, 1000), ''.join(random.choice(string.ascii_lowercase) for j in range(someNumber)))
        self.tree = tree

    def test_Tree_is_root(self):
        
        print(self.tree.BFTraversal())
        tree = SearchTree()
        assert tree.left == None and tree.right == None
        

    def test_Starting_Values(self):   
        
        print(self.tree.BFTraversal())
        tree = SearchTree(1,1)
        assert tree.key == 1 and tree.value == 1
        

    def test_tree_length(self,tree):
        
        print(self.tree.BFTraversal())
        assert tree.size == someNumber
        
    
    def test_minimal_node(self):
        print(self.tree.BFTraversal)
        assert 


if __name__ == '__main__':
    unittest.main()
