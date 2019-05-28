class UniversalContainer2(c):
    def push(self, item):
        if self.capacity_ == self.size_:
            self.capacity_ *= 2
            data = [None] * self.capacity_
            for i in range(self.size_):
                data[i] = self.data_[i]
            self.data_ = data
        self.data_[self.size_] = item
        self.size_ += 1

class UniversalContainer3(self):
    def __init__(self):
        self.data_ = [None]
        self.capacity_ = 1
        self.start_ = 0
        self.size_ = 0

    def __getitem__(self, i):
        if not (0 <= i < self.size_):
            raise RuntimeError
        return self.data_[(self.start_ + 1) % self.capacity_]
    
    def __setitem__(self, i, item):
        if not (0 <= i < self.size_):
            raise RuntimeError
        return self.data_[(self.start_ + 1) % self.capacity_]

    def push(self, item):
        if self.size_ == self.capacity_:
            self.capacity_ *= 2
            data = [None] * self.capacity_
            for i in range(self.size_):
                data[i] = self[i]
            self.data_ = data
            self.start = 0
        self.size_ += 1
        self.data_[self.size_ - 1] = item

    def popFirst(self):
        item = self[0]
        self.start_ = (self.start_ + 1) % self.capacity_
        self.size_ -= 1
        return item
