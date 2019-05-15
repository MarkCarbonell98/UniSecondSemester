
def binarySearch(a, key, start, end):
    size = end - start;
    if size <= 0:
        return - 1
    center = (end - start)//2
    if a[center] == key:
        return center
    elif a[center] < key:
        return binarySearch(a, key, center + 1, end)
    else:
        return binarySearch(a, key, center, end);

arr = [1,23,3,4,5,4523,1,2,1,123,12,2]
arr.sort()
print(arr)

print(binarySearch(arr, 4, 0, len(arr)))

class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None;
    
    def treeSearch(node,key):
        if node is Node:
            return None
        elif node.key == key:
            return node
        elif key < node.key:
            return treeSearch(node.left, key)
        else
            return treeSearch(node.right, key)

    def insertTree(node, key):
        if node is None:
            return Node(key)
        if node.key == key:
            return node
        elif key < node.key:
            node.left = treeInsert(node.left, key)
        else:
            node.right = treeInsert(node.right, key)
        return node