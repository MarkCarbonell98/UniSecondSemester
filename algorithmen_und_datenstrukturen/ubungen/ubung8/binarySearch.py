import unittest

def binarySearch(a, key, start, end):
    key = int(key)
    size = end - start
    if size <= 0:
        return None
    center = start + end // 2
    if(key == a[center]):
        return center
    elif key < center:
        return binarySearch(a, key, start, center)
    else:
        return binarySearch(a, key, center+1, end)


class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.testArrays = [
            [],
            [0],
            [1]
            [-1, 1],
            [1,2,3,4],
            [0,2,10,15,20],
            [-20, -10, -5, -1],
            [1,1],
            [0,0,0,0,0,1],
            [-1, 0,0,0,0,0,1],
            [-2,-1,0]
        ]

        self.testNumbers = [1, 0, -1, 4, 0, -10, 1, 1, -1, -2]

    def test_binarySearch(self):
        self.assertEqual(self.test)




