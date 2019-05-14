# fixture is the preparation needed to run a certain test
# test case is a single unit of testing
# test suite is a collection of test cases
# test runner is a program that executes tests and sends the results to the user

import unittest

class TestStringMethods(unittest.TestCase):
    
    def test_upper(self):
        self.assertEqual("foo".upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)
        print("this test ran")

if __name__ == '__main__':
    unittest.main()