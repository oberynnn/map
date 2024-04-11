from CurtinMap import *

# create a graph object
graph = CurtinMap()

class LocationsIO():

    def __init__(self, file_name):
        # Initiate csv file
        self.file_name = file_name

    def readGraph(self):
        # open and read file
        with open(self.file_name, "r") as file:
            # parse the file
            for line in file:
                # split commas because its csv file
                cell = line.strip().split(",")
                # addVertex method
                graph.addVertex(cell[0])
        # return the graph because we need to store the vertices, or locations in this case to the graph
        return graph

# test
locs = LocationsIO("/home/viserys/Desktop/DSA1002/Assignment1/Vertices.csv")
locs.readGraph()
graph.printAllLoc()