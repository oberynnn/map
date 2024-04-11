from CurtinMap import *

# create graph object
graph = CurtinMap()

class PathIO():

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
                # parse by column
                graph.addVertex(cell[0])
                graph.addVertex(cell[1])
                # addEdge method to add paths
                graph.addEdge(cell[0], cell[1], int(cell[2]))
        # return graph because we're going to store all the edges, or paths in this case, in the graph
        return graph

# test        
paths = PathIO("/home/viserys/Desktop/DSA1002/Assignment1/Edges.csv")
paths.readGraph()
graph.printAllEdge()
graph.printAllPaths("B420", "B411")