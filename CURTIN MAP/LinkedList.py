from ListNode import DSAListNode

class DSALinkedList():

    def __init__(self):
        self.head = None

    def __iter__(self):
        currNd = self.head
        while currNd !=None:
            yield currNd.value
            currNd = currNd.next

    def insertFirst(self, newValue):
        newNd = DSAListNode(newValue)
        if self.isEmpty() == True:
            self.head = newNd
        else:
            newNd.setNext(self.head)
            self.head = newNd

    def insertLast(self, newValue):
        newNd = DSAListNode(newValue)
        if self.isEmpty() == True:
            self.head = newNd
        else:
            currNd = self.head
            while (currNd.getNext() != None):
                currNd = currNd.getNext()
            currNd.setNext(newNd)

    def isEmpty(self):
        if (self.head == None):
            return True
        else:
            return False

    def peekFirst(self):
        if self.isEmpty() == False:
            nodeValue = self.head.getValue()
            return nodeValue
        else:
            raise ValueError("Linked list is empty")

    def peekLast(self):
        if self.isEmpty() == False:
            currNd = self.head
            while (currNd.getNext(self) != None):
                currNd = currNd.getNext(self)
            currNd = currNd.getValue(self)
            return currNd
        else:
            raise ValueError("Linked list is empty")

    def removeFirst(self):
        if (self.isEmpty() == False):
            nodeValue = self.head.getValue()
            self.head = self.head.getNext()
        else:
            raise ValueError("Linked list is empty")
        return nodeValue

    def removeLast(self):
        if (self.isEmpty() == False):
            if (self.head.getNext() == None):
                nodeValue = self.head.getValue()
                self.head == None
            else:
                prevNd = None
                currNd = self.head
                while (currNd.getNext() != None):
                    prevNd = currNd
                    currNd = currNd.getNext()
                prevNd.setNext(None)
                nodeValue = currNd.getValue()
            return nodeValue
        else:
            raise ValueError("Linked list is empty")

    def display(self):
        curr = self.head
        while curr != None:
            print(curr.getValue())
            curr = curr.getNext()