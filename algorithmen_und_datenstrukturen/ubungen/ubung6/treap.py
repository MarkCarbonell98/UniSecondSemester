import random

#Funktionen rotateLeft und rotateRight hinzugefuegt

def rotateLeft(rootnode):
    newRoot = rootnode.right
    rootnode.right = newRoot.left
    newRoot.left = rootnode
    return newRoot



def rotateRight(rootnode):
    newRoot = rootnode.left
    rootnode.left = newRoot.right
    newRoot.right = rootnode
    return newRoot


#Node aus Uebung 5 uebernommen und priority hinzugefuegt

class NodeRandom:
    def __init__(self, key, value):
        self.key = key
        self.priority = 0  #piority-Attribut hinzugefuegt und auf 0 gesetzt
        
        #Sicherstellen, dass keine Nummern bei der Prioritaet doppelt vergeben werden und Werte loeschen
        
        #Zufallszahl
        randomKey = random.randin(1,10000)
        
        #Ist sie bereits in RandomNumbersTaken? Wenn Ja, neue Zufallszahl
        while randomKey in RandomNumbersTaken:
            randomKey = random.randin(1,10000)
            
        
        #Noch nicht verwendete Zufallszahl in RandomNumbersTaken einfuegen
        RandomNumbersTaken.append(randomKey)
        
        #Prioritaet auf Zufallsnummer setzen
        self.priority = randomKey    
        
        self.left = self.right = None


#Node aus Uebung 5 uebernommen und priority hinzugefuegt
class NodeDynamic:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.priority = 1 #piority-Attribut hinzugefuegt und auf 1 gesetzt
        self.left = self.right = None

        
        


class RandomTreap:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

     #Array zum Speichern der bereits gewählten Zufallszahlen
    RandomNumbersTaken = []
    
    def insert(self,key, value):
        newNode = NodeRandom(key, value)
        if not self.root:
            self.root = newNode
            self.size += 1
            return self
        
        i = self.root
        while True:
            if key == i.key: 
                i.value = value
                return self
            if key < i.key:
                if i.left == None:
                    i.left = newNode
                    self.size += 1
                    return self
                i = i.left
            else:
                if i.right == None:
                    i.right = newNode
                    self.size += 1
                    return self
                i = i.right
       

    def minRightKeyNode(self, node):
        node = node.left
        while node.right != None:
            node = node.right
        return node


    def BFTraversal(self):
        if not self.root:
            return None
        i = self.root
        queue, visited = [i], []
        while(len(queue)):
            i = queue.pop(0)
            visited.append((i.key, i.value))
            if i.left:
                queue.append(i.left)
            if i.right:
                queue.append(i.right)
        return visited

    def depth(self, node = None, count = 0):
        if node == None and count == 0:
            node = self.root
        if node == None: return 0
        left = self.depth(node.left, count + 1)
        right = self.depth(node.right, count + 1)
        return max(left, right) + 1

    def remove(self, key, node = None, counter = 0):
        if self.find(key) == None: raise KeyError("The key " + key + " was not found in this tree")
        if node == None and counter == 0:
            node = self.root
        if node is None:
            return node
        if key < node.key:
            node.left = self.remove(key, node.left, counter + 1)
        elif key > node.key:
            node.right = self.remove(key, node.right, counter + 1)
        else:

            if node.left == None and node.right == None:
                node = None
            elif node.left == None:
                node = node.right
            elif node.right == None:
                node = node.left
            else:
                minRightSubtreeNode = self.minRightKeyNode(node)
                node.key = minRightSubtreeNode.key
                node.value = minRightSubtreeNode.value
                node.left = self.remove(minRightSubtreeNode.key, node.left,  counter + 1)
        return node

    def find(self, key):
        if not self.root:
            return None
        i = self.root
        while True:
            if not i: return None
            if key < i.key:
                i = i.left
                
            elif key > i.key:
                i = i.right
                
            else:
                return i





class DynamicTreap:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    
    def insert(self,key, value):
        newNode = NodeDynamic(key, value)
        if not self.root:
            self.root = newNode
            self.size += 1
            return self
        
        i = self.root
        while True:
            if key == i.key: 
                i.value = value
                return self
            if key < i.key:
                if i.left == None:
                    i.left = newNode
                    self.size += 1
                    return self
                i = i.left
            else:
                if i.right == None:
                    i.right = newNode
                    self.size += 1
                    return self
                i = i.right

 
 #zweiter Suchdurchlauf, um den Parent zu finden, um ggf. zu tauschen; bin mir nicht sicher, ob das so notwendig ist
        j = self.root
        while priority != j.left.priority and priority != j.right.priority:
            
            if key < j.key:
                j = j.left
            
            if key > j.key:
                j = j.right
            
        
            while priority == j.left.priority:
                rotateRight(self)
            
        
            while priority == j.right.priority:
                rotateLeft(self)

    def minRightKeyNode(self, node):
        node = node.left
        while node.right != None:
            node = node.right
        return node


    def BFTraversal(self):
        if not self.root:
            return None
        i = self.root
        queue, visited = [i], []
        while(len(queue)):
            i = queue.pop(0)
            visited.append((i.key, i.value))
            if i.left:
                queue.append(i.left)
            if i.right:
                queue.append(i.right)
        return visited

    def depth(self, node = None, count = 0):
        if node == None and count == 0:
            node = self.root
        if node == None: return 0
        left = self.depth(node.left, count + 1)
        right = self.depth(node.right, count + 1)
        return max(left, right) + 1

    def remove(self, key, node = None, counter = 0):
        if self.find(key) == None: raise KeyError("The key " + key + " was not found in this tree")
        if node == None and counter == 0:
            node = self.root
        if node is None:
            return node
        if key < node.key:
            node.left = self.remove(key, node.left, counter + 1)
        elif key > node.key:
            node.right = self.remove(key, node.right, counter + 1)
        else:

            if node.left == None and node.right == None:
                node = None
            elif node.left == None:
                node = node.right
            elif node.right == None:
                node = node.left
            else:
                minRightSubtreeNode = self.minRightKeyNode(node)
                node.key = minRightSubtreeNode.key
                node.value = minRightSubtreeNode.value
                node.left = self.remove(minRightSubtreeNode.key, node.left,  counter + 1)
        return node

    def find(self, key):
        if not self.root:
            return None
        i = self.root
        while True:
            if not i: return None
            if key < i.key:
                i = i.left
                continue
            elif key > i.key:
                i = i.right
                continue
            else:
                return i
<<<<<<< HEAD:algorithmen_und_datenstrukturen/ubungen/ubung6/treap.py









#c)
filename = die-drei-musketiere.txt
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
    
    



def compareTrees(tree1, tree2):
    if tree1 == None and tree2 is None:
        return True
    elif tree1 != None and tree2 != None:
        return tree1.priority == tree2.priority and compareTrees(tree1.left, tree2.left) and compareTrees(tree1.right, tree2.right)
    else:
        return False

=======
>>>>>>> fbf87d5f44810d113a046f9d24b22f0fb1a7cb20:algorithmen_und_datenstrukturen/ubungen/ubung6/treap.py
