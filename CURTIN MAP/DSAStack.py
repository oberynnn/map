import numpy as np

class DSAStack():
    DEFAULT_CAPACITY = 100

    def __init__(self, maxCapacity=DEFAULT_CAPACITY):
        self.stack = np.full(maxCapacity, None, dtype=object)
        self.count = 0

    def getCount(self):
        return self.count

    def isEmpty(self):
        if self.count == 0:
            return True
        else:
            return False

    def isFull(self):
        if self.count == self.DEFAULT_CAPACITY:
            return True
        else:
            return False

    def push(self, value):
        if self.isFull():
            raise Exception("Stek full not stonks")
        else:
            self.stack[self.count] = value
            self.count += 1

    def pop(self):
        topVal = self.top()
        self.count -= 1
        return topVal

    def top(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        else:
            return self.stack[self.count - 1]

    def display(self):
        print(self.stack)