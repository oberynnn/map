# please don't break my code
# i already try to follow the pseudocode
# :v

# import all required classes
from LinkedList import *
from MapLocation import *
from MapPath import *
from DSAStack import *
from DSAQueue import *

# curtin map class
class CurtinMap():

    # initiate both locations and paths using linked list
    def __init__(self):
        self.locations = DSALinkedList()
        self.paths = DSALinkedList()

    # returns linked list that contains all vertices
    def getVertices(self):
        return self.locations

    # return linked list that contains all edges
    def getPaths(self):
        return self.paths
    
    # add new vertex function -> makes a new vertex
    def addVertex(self, label):
        # initiate a DSAMapLocation item which is going to take 'label' as a value
        newVertex = DSAMapLocation(label)
        # insert new vertex to the vertex linked list
        self.locations.insertLast(newVertex)

    # add new edge function -> makes a new edge between two existing vertices
    def addEdge(self, label1, label2, value):
        # get vertex for the first label
        loc1 = self.getVertex(label1)
        l1 = loc1.label
        # get vertex for the second label
        loc2 = self.getVertex(label2)
        l2 = loc2.label
        # the first vertex will add the second vertex into its adjacency list, which is a linked list
        loc1.addEdge(loc2)
        # the second will do the same towards the first vertex
        loc2.addEdge(loc1)
        # initiate a new DSAMapPath object
        newEdge = DSAMapPath(label1, label2, value)
        # insert new path to edge linked list
        self.paths.insertLast(newEdge)

    # get vertex function -> returns a vertex according the label that acts as a parameter to the function
    def getVertex(self, label):
        # find vertex first
        if self.hasVertex(label) == True:
            # iterate through the vertex linked list until we found the vertex that we need
            curr = self.locations.head
            while curr != None:
                location = curr
                if location.getValue().getLabel() == label:
                    return location.getValue()
                curr = curr.getNext()
        # if not found scenario
        return None

    # print all paths function -> print all paths between two locations
    def printAllPaths(self, label1, label2):
        # dfs first
        print("By depth first search: ")
        self.findPath(label1, label2)
        # then bfs
        print("By breadth first search: ")
        self.breadthFirstSearch(label1, label2)

    # has vertex function -> check if a vertex exists according to the provided label
    def hasVertex(self, label):
        # iterate through the vertex linked list until it finds the vertex
        curr = self.locations.head
        while curr != None:
            if (curr.getValue().getLabel() == label):
                return True
            curr = curr.getNext()
        # if not found scenario
        return False

    # get vertex count function -> returns the number of vertex in vertex linked list
    def getVertexCount(self):
        return self.locations.getCount()

    # get edge count function -> returns the number of edges in edge linked list
    def getEdgeCount(self):
        return self.paths.getCount()

    # get edge function -> iterates through a vertex's adjacency list and print the vertex's adjacent nodes one by one
    def getEdge(self, label):
        loc = self.getVertex(label)
        for vtx in loc.getAdjacent():
            print(vtx.getLabel())

    # get path function -> returns the path between two vertices
    def getPath(self, label1, label2):
        vtx1 = self.getVertex(label1)
        vtx2 = self.getVertex(label2)
        # iterate through edges linked list
        for path in self.paths:
            if ((path.fromVertex == label1) and (path.toVertex == label2)):
                # if found scenario
                return path

    # get path distance function -> returns a path's weight or distance
    def getPathDistance(self, label1, label2):
        # find path first
        edge = self.getPath(label1, label2)
        # then return the weight as a distance
        return edge.getWeight()

    # get adjacent function -> returns a vertex's adjacent nodes
    def getAdjacent(self, label):
        # find and get the vertex first
        vertex = self.getVertex(label)
        if vertex is not None:
            # returns the adjacent nodes
            vertex.displayEdge()
            return vertex.getAdjacent()
        # if not found
        return None

    # get adjacent edge(?) function -> the same as get adjacent function    
    def getAdjacentE(self, label):
        location = self.getVertex(label)
        if location is not None:
            return location.links

    # print all loc function -> prints out all vertices
    def printAllLoc(self):
        self.locations.display()

    # print all edge function -> prints out all paths that are added
    def printAllEdge(self):
        self.paths.display()

    # depth first search function -> traverse and search the graph by depth
    def depthFirstSearch(self, startLabel, endLabel):
        # initiate stack object
        S = DSAStack()
        # initiate a linked list object
        T = DSALinkedList()
        # iterate through the vertices list
        for vertex in self.getVertices():
            # mark all vertices as new
            vertex.clearVisited()
        # find and get the vertex that has the start label as its label
        startVtx = self.getVertex(startLabel)
        # mark start vertex as old
        startVtx.setVisited()
        # push start vertex to stack
        S.push(startLabel)
        # initiate total distance variable
        totalDistance = 0
        # while loop if stack is not empty
        while not S.isEmpty():
            # iterate through start vertex adjacent nodes
            for vtx in startVtx.getAdjacent():
                # if the node is still new
                if vtx.getVisited() == False:
                    # insert both start vertex and the adjacent vertex to the linked list
                    T.insertLast((startVtx.getLabel(), vtx.getLabel()))
                    # mark adjacent vertex as old
                    vtx.setVisited()
                    # push adjacent vertex to stack
                    S.push(vtx.getLabel())
                    # add total distance from get path distance function
                    totalDistance += self.getPathDistance(startVtx.getLabel(), vtx.getLabel())
                    # display the linked list just to check
                    T.display()
                    # print out cumulative distance
                    print("cumulative distance is now: {0}".format(totalDistance))
                    # switch vertices
                    startVtx = vtx 
            # pop stack
            startLabel = S.pop()
            startVtx = self.getVertex(startLabel)
            # print pop just to check
            print("popped ", startLabel)
            # if vertex label is the same as the end label
            if (startLabel == endLabel):
                # end
                break
        # display tree
        print("Overall tree:")
        T.display()
        # prints total distance
        print("Total distance from by dfs is {0}".format(totalDistance))
        # return total distance for min path function
        return totalDistance

    # find path function -> similar to depth first search function, just without returning the total distance
    def findPath(self, startLabel, endLabel):
        S = DSAStack()
        T = DSALinkedList()
        for vertex in self.getVertices():
            vertex.clearVisited()
        startVtx = self.getVertex(startLabel)
        self.getVertex(startLabel).setVisited()
        S.push(startLabel)
        totalDistance = 0
        while not S.isEmpty():
            for vtx in startVtx.getAdjacent():
                if vtx.getVisited() == False:
                    T.insertLast((startVtx.getLabel(), vtx.getLabel()))
                    vtx.setVisited()
                    S.push(vtx.getLabel())
                    T.display()
                    totalDistance += self.getPathDistance(startVtx.getLabel(), vtx.getLabel())
                    print("cumulative distance is now: {0}".format(totalDistance))
                    startVtx = vtx 
            startLabel = S.pop()
            startVtx = self.getVertex(startLabel)
            print("popped ", startLabel)
            if (startLabel == endLabel):
                break
        print("Overall tree:")
        T.display()
        print("Total distance by dfs is {0}".format(totalDistance))
        return totalDistance

    # breadth first search function -> traverse and search the graph by breadth
    def breadthFirstSearch(self, startLabel, endLabel):
        # initiate queue object
        Q = DSAQueue()
        # initiate linked list object
        T = DSALinkedList()
        # initiate total distance object
        totalDistance = 0
        # iterate through vertices list
        for vertex in self.getVertices():
            # mark all vertices as new
            vertex.clearVisited()
        # find and get vertex that has the same label as start label
        startVtx = self.getVertex(startLabel)
        # mark start vertex as old
        startVtx.setVisited()
        # enqueue start vertex to queue
        Q.enqueue(startLabel)
        # while queue is not empty loop
        while not Q.isEmpty():
            # dequeue queue
            startVtx = Q.dequeue()
            # iterate through start vertex's adjacency list
            for vtx in self.getVertex(startVtx).getAdjacent():
                # if vertex is still new
                if vtx.getVisited() != True:
                    # insert both start vertex and vertex to linked list
                    T.insertLast((self.getVertex(startVtx).getLabel(), vtx.getLabel()))
                    # mark vertex as old
                    vtx.setVisited()
                    # enqueue vertex to old
                    Q.enqueue(vtx.getLabel())
                    # display list to check
                    T.display()
                    # accumulate total distance
                    totalDistance += self.getPathDistance(self.getVertex(startVtx).getLabel(), vtx.getLabel())
                    # print cumulative distance just to check
                    print("cumulative distance is now: {0}".format(totalDistance))
            # if vertex's label is the same as end label
            if (startVtx == endLabel):
                # break while loop
                break
        # display list
        print("Overall tree:")
        T.display()
        # print total distance
        print("Total distance from {0} to {1} by bfs is {2}".format(startLabel, endLabel, totalDistance))
        # return total distance for min path function
        return totalDistance

    # min path function -> compare total distance based on depth first search and breadth first search
    def minPath(self, label1, label2):
        print("Using depth first search: ")
        # depth first search on the labels
        self.depthFirstSearch(label1, label2)
        byDfs = self.findPath(label1, label2)
        print("Using breadth first search: ")
        # breadth first search on the labels
        self.breadthFirstSearch(label1, label2)
        byBfs = self.breadthFirstSearch(label1, label2)
        # compare the returned total distance, if smaller, it will get printed out
        if (byBfs > byDfs):
            print("Shortest distance is by depth first search: {0}".format(byDfs))
        elif (byBfs < byDfs):
            print("Shortest distance is by breadth first search: {0}".format(byBfs))
        elif (byBfs == byDfs):
            print("Distance is the same by using both breadth first search and depth first search")

    def addLocation(self, fileName):
        # open and read file
        with open(fileName, "r") as file:
            # parse the file
            for line in file:
                # split commas because its csv file
                cell = line.strip().split(",")
                # addVertex method
                if (self.hasVertex(cell[0] == False)):
                    self.addVertex(cell[0])
        # return the graph because we need to store the vertices, or locations in this case to the graph
        return self

    def addPaths(self, fileName):
        with open(fileName, "r") as file:
            for  line in file:
                # split commas because its csv file
                cell = line.strip().split(",")
                # parse by column
                # check if there is double vertices in the file, if not, then add
                if (self.hasVertex(cell[0]) == False):
                    self.addVertex(cell[0])
                if (self.hasVertex(cell[1]) == False):
                    self.addVertex(cell[1])
                # addEdge method to add paths
                self.addEdge(cell[0], cell[1], int(cell[2]))
                self.addEdge(cell[1], cell[0], int(cell[2]))
        # return graph because we're going to store all the edges, or paths in this case, in the graph
        return self

# test is in curtinmap_test.py file

map = CurtinMap()
# map.addLocation("/home/viserys/Desktop/DSA1002/Assignment1/Vertices.csv")
# map.printAllLoc()
map.addPaths("/home/viserys/Desktop/DSA1002/Assignment1/Edges.csv")
# map.printAllEdge()
map.printAllLoc()
# print("\n")
# print(map.getAdjacent("B407").display())
# print("\n")
map.depthFirstSearch("B420", "B407")