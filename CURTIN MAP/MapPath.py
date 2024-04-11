from MapLocation import DSAMapLocation

class DSAMapPath():

    def __init__(self, fromVertex, toVertex, weight):
        self.fromVertex = fromVertex
        self.toVertex = toVertex
        self.weight = weight

    def __str__(self):
        return ("{0} - {1} : {2}".format(self.fromVertex, self.toVertex, self.weight))

    def getWeight(self):
        return self.weight

    def getFrom(self):
        return self.fromVertex

    def getTo(self):
        return self.toVertex

    def isDirected(self):
        return isinstance(self.fromVertex, DSAMapLocation) and isinstance(self.toVertex, DSAMapLocation)