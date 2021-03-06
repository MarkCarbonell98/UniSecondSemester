
class UniversalContainer:
    def __init__(self):
        self.capacity_ = 1
        self.data_ = [None]*self.capacity_
        self.size_ = 0

    def printData(self):
        print(self.data_)


    def size(self):
        return self.size_


    def capacity(self):
        return self.capacity_

    def push(self, item):
        if self.capacity_ == self.size_: #internal memory is full
            oldData = self.data_
            self.capacity_ *= 2
            self.data_ = [None]*self.capacity_
            for i in range(len(oldData)):
                self.data_[i] = oldData[i]

        self.data_[self.size_] = item
        self.size_ += 1

        return self.size_

    def popLast(self):
        if self.size_ == 0:
            raise RuntimeError("popLast() on empty container!")
        self.data_[self.size_ - 1] = None
        self.size_ -= 1
        return self.data_


    def popFirst(self):
        if self.size_ == 0:
            raise RuntimeError("popFirst() on empty container!")
        
        for i in range(len(self.data_) - 1):
            self.data_[i] = self.data_[i + 1]

        self.size_ -= 1

        return self.data_

        

    def __getitem__(self, index): #implements v = c[index]
        if index < 0 or index >= self.size_:
            raise RuntimeError("Index out of range")

        return self.data_[index]

    def __setitem__(self, index,v): #implements c[index] = v
        if index < 0 or index >= self.size_:
            raise RuntimeError("Index out of range")

        self.data_[index] = v
        return v

    def first(self):
        return self.data_[0]

    def last(self):
        return self.data_[self.size_ - 1]


a,b,s,d,e,k = 25,1, "hellou","hellou", {"name": True}, 2
c = UniversalContainer()
print("c.size() ",c.size())
print("c.capacity() ", c.capacity())

print(c.push(a))
print(c.push(b))
print(c.push(s))
print(c.push(d))
print(c.push(e))

c.printData()

print(c.popFirst())
c.printData()
print(c.popLast())
c.printData()
v = c[k]
print("v = ", v)

c[k] = v
print("c[k] = ", v)

print(v)
v = c.first()
print(v)
v = c.last()
print(v)

from copy import deepcopy

def testContainer(c):
    assert(c.size() <= c.capacity()) # zu jeder Zeit gilt c.size() <= c.capacity()

    # push tests
    testValue, previousSize, copy = "TEST", c.size(), deepcopy(c)
    c.push(testValue)

    newSize = c.size()
    assert(previousSize + 1 == newSize) # i

    print(c.last())
    assert(testValue == c.last()) # ii

    newContainer = UniversalContainer()
    assert(newContainer.size() == 0) # Ein neuer Container hat die Grosse 0
    newContainer.push(testValue)
    assert(newContainer.first() == newContainer.last()) # iii

    c.popLast() # v
    assert(c.data_ == copy.data_) # iv

    #setitem tests
    c[k] = testValue
    assert(c.size() == previousSize) # i
    assert(c[k] == testValue) # ii
    for i in range(c.size()):
        if i != k:
            assert(copy[i] == c[i]) #iii

    # nach c.popLast()
    previousSize, copy = c.size(), deepcopy(c)
    c.popLast()
    assert(previousSize - 1 == c.size()) # i
    for i in range(c.size() - 1):
        if i != k:
            assert(copy[i] == c[i]) # ii\

    # nach c.popFirst()
    previousSize, copy = c.size(), deepcopy(c)
    c.popFirst()
    assert(previousSize - 1 == c.size()) # i
    for i in range(c.size() - 1):
        if i != k:
            assert(copy[i + 1] == c[i]) # ii\

    if(c.size() > 0):
        assert(c.first() == c[0])
        assert(c.last() == c[c.size() - 1])

testContainer(c)



