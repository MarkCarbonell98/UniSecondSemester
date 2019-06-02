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
