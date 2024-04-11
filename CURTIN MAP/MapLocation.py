from LinkedList import DSALinkedList

class DSAMapLocation():

    def __init__(self, inLabel):
        self.label = inLabel
        self.links = DSALinkedList()
        self.visited = False
        self.next = None
        self.prev = None

    def __str__(self):
        label = self.label
        return ("{0}:{1}".format(label, [a.label for a in self.getAdjacent()]))

    def getLabel(self):
        return self.label

    def getAdjacent(self):
        return self.links

    def addEdge(self, vertex):
        self.links.insertLast(vertex)

    def displayEdge(self):
        self.links.display()

    def setVisited(self):
        self.visited = True

    def getVisited(self):
        return self.visited

    def clearVisited(self):
        self.visited = False

    def getNext(self):
        return self.next
    
    def setNext(self,newNext):
        self.next = newNext

    def getPrev(self):
        return self.prev
    
    def setPrev(self,newPrev):
        self.prev = newPrev