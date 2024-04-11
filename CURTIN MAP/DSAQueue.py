import numpy as np

class DSAQueue():
    DEFAULT_CAPACITY = 100

    def __init__(self, maxCapacity=DEFAULT_CAPACITY):
        self.queue = np.full(maxCapacity, None, dtype=object)
        self.count = 0

    def getCount(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == len(self.queue)

    def enqueue(self, value):
        if self.isFull():
            raise Exception("Queue is full")
        else:
            self.queue[self.count] = value
            self.count += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        else:
            frontVal = self.queue[0]
            for i in range(self.count - 1):
                self.queue[i] = self.queue[i + 1]
            self.count -= 1
            return frontVal

    def peek(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        else:
            return self.queue[0]

    def display(self):
        print(self.queue)