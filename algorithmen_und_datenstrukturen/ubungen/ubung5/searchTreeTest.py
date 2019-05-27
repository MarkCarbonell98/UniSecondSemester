import unittest

import random
import string
from searchTree import Node, SearchTree

class TestSearchTree(unittest.TestCase):

    def setUp(self):
        tree = SearchTree()
        for someNumber in range(random.randint(1,20)):
            tree.insert(random.randint(-1000, 1000), ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(1, 20))))
        self.tree = tree

    def isTreeValid(self, tree):
        # todo
        print(self.tree.BFTraversal())

    def testStartingValues(self):   
        
        #todo
        print(self.tree.BFTraversal())



if __name__ == '__main__':
    unittest.main()