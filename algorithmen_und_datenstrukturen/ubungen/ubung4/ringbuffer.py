import copy

# aufgabe 4a

class UniversalContainer1:
    def __init__(self): # constructor for empty container
        self.capacity_ = 1 # we reserve memory for at least one item
        self.data_ = [None]*self.capacity_ # the internal memory
        self.size_ = 0 # no item has been inserted yet

    def size(self):
        return self.size_

    def capacity(self):
        return self.capacity_

    def push(self, item): # add item at the end
        if self.capacity_ == self.size_:
            self.capacity_ += 1
            self.data_ += [None]
        self.data_[self.size_] = item
        self.size_ += 1

    def popFirst(self):
        if self.size_ == 0:
            raise RuntimeError("popFirst() on empty container")
        self.size_ -= 1
        for i in range(self.size_):
            self.data_[i] = self.data_[i+1]

    def popLast(self):
        if self.size_ == 0:
            raise RuntimeError("popLast() on empty container")
        self.size_ -= 1

    def __getitem__(self, index): # __getitem__ implements v = c[index]
        if index < 0 or index >= self.size_:
            raise RuntimeError("index out of range")
        return self.data_[index]

    def __setitem__(self, index, v): # __setitem__ implements c[index] = v
        if index < 0 or index >= self.size_:
            raise RuntimeError("index out of range")
        self.data_[index] = v

    def first(self):
        return self.__getitem__(0)

    def last(self):
        return self.__getitem__(self.size_ - 1)

def containersEqual(left, right):
    if left.size() != right.size():
        return False
    for i in range(left.size()):
        if left[i] != right[i]:
            return False
    return True

def testContainer1():
    # teste leeren Container
    c = UniversalContainer1()
    assert c.size() == 0
    assert c.size() <= c.capacity()

    # teste push() in leeren Container
    c.push(1)
    assert c.size() == 1
    assert c.size() <= c.capacity()
    assert c.first() == 1
    assert c.last() == 1
    assert c[0] == 1
    assert c[0] == c.first() and c[c.size()-1] == c.last()

    # teste popLast() bei size==1
    c.popLast()
    assert c.size() == 0
    assert c.size() <= c.capacity()

    # teste push() von zwei Elementen, gefolgt von popLst()
    c.push(1)
    c_old = copy.deepcopy(c)
    c.push(2)
    assert c.size() == 2
    assert c.size() <= c.capacity()
    assert c.first() == 1
    assert c.last() == 2
    assert c[0] == 1
    assert c[1] == 2
    assert c[0] == c.first() and c[c.size()-1] == c.last()
    c.popLast()
    assert containersEqual(c, c_old)

    # teste popFirst() bei zwei Elementen
    c.push(2)
    c.popFirst()
    assert c.size() == 1
    assert c.size() <= c.capacity()
    assert c.first() == 2
    assert c.last() == 2
    assert c[0] == 2
    assert c[0] == c.first() and c[c.size()-1] == c.last()
    c.popFirst()
    assert c.size() == 0
    assert c.size() <= c.capacity()

    # teste c[k] = v bei vier Elementen
    c.push(2)
    c.push(3)
    c.push(4)
    c.push(5)
    for k in range(c.size()):
        c_old = copy.deepcopy(c)
        c[k] = k + 6
        for i in range(c.size()):
            if i != k:
                assert c[i] == c_old[i]
            else:
                assert c[i] == k + 6
        assert c[0] == c.first() and c[c.size()-1] == c.last()

    # teste popFirst() bei vier Elementen
    c_old = copy.deepcopy(c)
    c.popFirst()
    assert c.size() == 3
    assert c.size() <= c.capacity()
    assert c.first() == 7
    assert c.last() == 9
    for i in range(c.size()):
        assert c[i] == c_old[i+1]
    assert c[0] == c.first() and c[c.size()-1] == c.last()

    # teste popFirst() bei drei Elementen
    c_old = copy.deepcopy(c)
    c.popLast()
    assert c.size() == 2
    assert c.size() <= c.capacity()
    assert c.first() == 7
    assert c.last() == 8
    for i in range(c.size()):
        assert c[i] == c_old[i]
    assert c[0] == c.first() and c[c.size()-1] == c.last()

    print("All tests succeeded")


class UniversalContainer2:
    def __init__(self): # constructor for empty container
        self.capacity_ = 1 # we reserve memory for at least one item
        self.data_ = [None]*self.capacity_ # the internal memory
        self.size_ = 0 # no item has been inserted yet

    def size(self):
        return self.size_

    def capacity(self):
        return self.capacity_

    def push(self, item): # add item at the end
        if self.capacity_ == self.size_: # internal memory is full
            self.capacity_ *= 2
            new_data = [None]*self.capacity_
            for i in range(self.size_):
                new_data[i] = self.data_[i]
            self.data_ = new_data
        self.data_[self.size_] = item
        self.size_ += 1

    def popFirst(self):
        if self.size_ == 0:
            raise RuntimeError("popFirst() on empty container")
        self.size_ -= 1
        for i in range(self.size_):
            self.data_[i] = self.data_[i+1]

    def popLast(self):
        if self.size_ == 0:
            raise RuntimeError("popLast() on empty container")
        self.size_ -= 1

    def __getitem__(self, index): # __getitem__ implements v = c[index]
        if index < 0 or index >= self.size_:
            raise RuntimeError("index out of range")
        return self.data_[index]

    def __setitem__(self, index, v): # __setitem__ implements c[index] = v
        if index < 0 or index >= self.size_:
            raise RuntimeError("index out of range")
        self.data_[index] = v

    def first(self):
        return self.__getitem__(0)

    def last(self):
        return self.__getitem__(self.size_ - 1)

def testContainer2():
    # teste leeren Container
    c = UniversalContainer2()
    assert c.size() == 0
    assert c.size() <= c.capacity()

    # teste push() in leeren Container
    c.push(1)
    assert c.size() == 1
    assert c.size() <= c.capacity()
    assert c.first() == 1
    assert c.last() == 1
    assert c[0] == 1
    assert c[0] == c.first() and c[c.size()-1] == c.last()

    # teste popLast() bei size==1
    c.popLast()
    assert c.size() == 0
    assert c.size() <= c.capacity()

    # teste push() von zwei Elementen, gefolgt von popLst()
    c.push(1)
    c_old = copy.deepcopy(c)
    c.push(2)
    assert c.size() == 2
    assert c.size() <= c.capacity()
    assert c.first() == 1
    assert c.last() == 2
    assert c[0] == 1
    assert c[1] == 2
    assert c[0] == c.first() and c[c.size()-1] == c.last()
    c.popLast()
    assert containersEqual(c, c_old)

    # teste popFirst() bei zwei Elementen
    c.push(2)
    c.popFirst()
    assert c.size() == 1
    assert c.size() <= c.capacity()
    assert c.first() == 2
    assert c.last() == 2
    assert c[0] == 2
    assert c[0] == c.first() and c[c.size()-1] == c.last()
    c.popFirst()
    assert c.size() == 0
    assert c.size() <= c.capacity()

    # teste c[k] = v bei vier Elementen
    c.push(2)
    c.push(3)
    c.push(4)
    c.push(5)
    for k in range(c.size()):
        c_old = copy.deepcopy(c)
        c[k] = k + 6
        for i in range(c.size()):
            if i != k:
                assert c[i] == c_old[i]
            else:
                assert c[i] == k + 6
        assert c[0] == c.first() and c[c.size()-1] == c.last()

    # teste popFirst() bei vier Elementen
    c_old = copy.deepcopy(c)
    c.popFirst()
    assert c.size() == 3
    assert c.size() <= c.capacity()
    assert c.first() == 7
    assert c.last() == 9
    for i in range(c.size()):
        assert c[i] == c_old[i+1]
    assert c[0] == c.first() and c[c.size()-1] == c.last()

    # teste popFirst() bei drei Elementen
    c_old = copy.deepcopy(c)
    c.popLast()
    assert c.size() == 2
    assert c.size() <= c.capacity()
    assert c.first() == 7
    assert c.last() == 8
    for i in range(c.size()):
        assert c[i] == c_old[i]
    assert c[0] == c.first() and c[c.size()-1] == c.last()

    print("All tests succeeded")

class UniversalContainer3:
    def __init__(self): # constructor for empty container
        self.capacity_ = 1 # we reserve memory for at least one item
        self.data_ = [None]*self.capacity_ # the internal memory
        self.startIndex_ = 0
        self.endIndex_ = 0
        self.size_ = 0

    def size(self):
        return self.size_
        
        # if self.endIndex_ <= self.startIndex_


    def capacity(self):
        return self.capacity_

    def push(self, item): # add item at the end
        if self.size_ == self.capacity_:
            self.capacity_ *= 2
            data = [None] * self.capacity_
            for i in range(self.size_):
                data[i] = self[i]
            self.data_ = data
            self.start = 0
        self.size_ += 1
        self.data_[self.size_ - 1] = item

        # if self.capacity_ == self.size_: # internal memory is full
        #     self.capacity_ *= 2
        #     new_data = [None]*self.capacity_
        #     for i in range(self.size_):
        #         new_data[i] = self.data_[i]
        #     self.data_ = new_data
        # self.data_[self.size_] = item
        # self.size_ += 1

    def popFirst(self):
        # if self.size_ == 0:
        #     raise RuntimeError("popFirst() on empty container")
        self.startIndex_ = (self.startIndex_ + 1) % (self.capacity_)
        self.size_ -= 1

    def popLast(self):
        # if self.size__ == 0:
        #     raise RuntimeError("popLast() on empty container")
        self.endIndex_  = (self.endIndex_ - 1) % (self.capacity_)
        self.size_ -= 1

    def __getitem__(self, index): # __getitem__ implements v = c[index]
        # if index < 0 or index >= self.size():
            # raise RuntimeError("index out of range")
        return self.data_[(index + self.startIndex_) % (self.capacity_)]

    def __setitem__(self, index, v): # __setitem__ implements c[index] = v
        # if index < 0 or index >= self.size_:
            # raise RuntimeError("index out of range")
        self.data_[(index + self.startIndex_) % (self.capacity_)] = v

    def first(self):
        return self.__getitem__(0)

    def last(self):
        return self.__getitem__(self.size() - 1)


def testContainer3():
    # teste leeren Container
    c = UniversalContainer3()
    assert c.size() == 0
    assert c.size() <= c.capacity()

    # teste push() in leeren Container
    c.push(1)
    print(c.data_, c.startIndex_, c.endIndex_)
    assert c.size() == 1
    assert c.size() <= c.capacity()
    assert c.first() == 1
    assert c.last() == 1
    assert c[0] == 1
    assert c[0] == c.first() and c[c.size()-1] == c.last()

    # teste popLast() bei size==1
    c.popLast()
    assert c.size() == 0
    assert c.size() <= c.capacity()

    # teste push() von zwei Elementen, gefolgt von popLast()
    c.push(1)
    c_old = copy.deepcopy(c)
    c.push(2)
    assert c.size() == 2
    assert c.size() <= c.capacity()
    assert c.first() == 1
    assert c.last() == 2
    assert c[0] == 1
    assert c[1] == 2
    assert c[0] == c.first() and c[c.size()-1] == c.last()
    c.popLast()
    assert containersEqual(c, c_old)

    # teste popFirst() bei zwei Elementen
    c.push(2)
    c.popFirst()
    assert c.size() == 1
    assert c.size() <= c.capacity()
    assert c.first() == 2
    assert c.last() == 2
    assert c[0] == 2
    assert c[0] == c.first() and c[c.size()-1] == c.last()
    c.popFirst()
    assert c.size() == 0
    assert c.size() <= c.capacity()

    # teste c[k] = v bei vier Elementen
    c.push(2)
    c.push(3)
    c.push(4)
    c.push(5)
    for k in range(c.size()):
        c_old = copy.deepcopy(c)
        c[k] = k + 6
        for i in range(c.size()):
            if i != k:
                assert c[i] == c_old[i]
            else:
                assert c[i] == k + 6
        assert c[0] == c.first() and c[c.size()-1] == c.last()

    # teste popFirst() bei vier Elementen
    c_old = copy.deepcopy(c)
    c.popFirst()
    assert c.size() == 3
    assert c.size() <= c.capacity()
    assert c.first() == 7
    assert c.last() == 9
    for i in range(c.size()):
        assert c[i] == c_old[i+1]
    assert c[0] == c.first() and c[c.size()-1] == c.last()

    # teste popFirst() bei drei Elementen
    c_old = copy.deepcopy(c)
    c.popLast()
    assert c.size() == 2
    assert c.size() <= c.capacity()
    assert c.first() == 7
    assert c.last() == 8
    for i in range(c.size()):
        assert c[i] == c_old[i]
    assert c[0] == c.first() and c[c.size()-1] == c.last()
    print("All tests succeeded")


testContainer1()
testContainer2()
testContainer3()

''' 

aufgabe 4b

'''

import timeit 

c2 = UniversalContainer2()
c3 = UniversalContainer3()
c4 = list()

N = 1000
repeats = 10

def runTestsPush(container, method):
    init = f'''
c = {container}()
    '''

    code = f'''
for i in range({N}):
    c.{method}(i)
    '''

    t = timeit.Timer(code, init, globals=globals())
    time = min(t.repeat(repeats, 1))
    print(f"Execution time {container}() = ", (time * 1000), "ms")

runTestsPush("UniversalContainer1", "push")
runTestsPush("UniversalContainer2", "push")
runTestsPush("UniversalContainer3", "push")
runTestsPush("list", "append")

# Nach dem messungen ist die amortisierte Komplexitat von UniversalContainer1() O(N), die von UniversalContainer2() O(1), die von UniversalContainer3() (in mein fall falsch implementiert) sollte von O(1) auch sein, ist grosser als O(N). Die von die Python Liste betragt nach unsere Einschatzung O(N) als amortisierte Komplexitat.



''' 

    aufgabe 4c

''' 


def runTestsPop(container, pushMethod, popMethod):

    t2 = timeit.Timer(f"for i in range(N): c.{pushMethod}(i)", f"c = {container}()", globals=globals())
    timePush = min(t2.repeat(repeats, 1))

    init = f'''
c = {container}()
for i in range({N}):
    c.{pushMethod}(i)
    '''


    code = f'''
for i in range({N}):
    c.{popMethod}()
    '''

    t = timeit.Timer(code, init, globals=globals())
    time = min(t.repeat(repeats, 1))
    print(f"Execution time {container}() = ", (abs(time - timePush) * 1000), "ms")

runTestsPop("UniversalContainer1", "push", "popFirst")
runTestsPop("UniversalContainer2", "push", "popFirst")
runTestsPop("UniversalContainer3", "push", "popFirst")
runTestsPop("list", "append", "pop")













    



    


    




