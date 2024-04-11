class DSAListNode():

    def __init__(self, inValue):
        self.value = inValue
        self.next = None
        self.prev = None
    
    def getValue(self):
        return self.value
    
    def setValue(self, inValue):
        self.value = inValue

    def getNext(self):
        return self.next
    
    def setNext(self,newNext):
        self.next = newNext

    def getPrev(self):
        return self.prev
    
    def setPrev(self,newPrev):
        self.prev = newPrev