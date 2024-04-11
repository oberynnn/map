from CurtinMap import *
import time

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
                graph.addEdge(cell[1], cell[0], int(cell[2]))
        # return graph because we're going to store all the edges, or paths in this case, in the graph
        return graph

if __name__=="__main__":

    # create choice variable
    choice = 0

    # because choice 7 is for exit
    while choice != 7:
        # print out all available options for the user to choose
        # title
        print("*" * 30)
        print("CURTIN MAP TEST HARNESS")
        print("*" * 30)
        print("LIST OF OPTIONS:")
        print("1. Add new location(s) (read the file provided to add locations to the map)")
        print("2. Add path(s) (read file to add paths between the inserted locations)")
        print("3. Print all locations")
        print("4. Print all paths (print path name/label distance connections i.e., the path is between which two locations)")
        print("5. PathBetween (print path between two given locations with total distance/weight)")
        print("6. PathMin (Smallest path between locations)")
        print("7. Exit")

        # here, user will input their choice as an integer 
        choice = int(input("Enter choice..."))

        #  functions according the number that the user inputted
        if (choice == 1):
            # Add new location(s) (read the file provided to add locations to the map)
            graph.addLocation("/home/viserys/Desktop/DSA1002/Assignment1/Vertices.csv")
            time.sleep(0.5)
            print("Add new locations successful")
        elif (choice == 2):
            # Add path(s) (read file to add paths between the inserted locations)
            graph.addPaths("/home/viserys/Desktop/DSA1002/Assignment1/Edges.csv")
            time.sleep(0.5)
            print("Add new paths from file successful")
        elif (choice == 3):
            # Print all locations that the user added in function number 1
            graph.printAllLoc()
        elif (choice == 4):
            # Print all paths (print path name/label distance connections i.e., the path is between which two locations) with distance
            graph.printAllEdge()
        elif (choice == 5):
            # PathBetween (print path between two given locations with total distance/weight)
            # user inputs the label for both locations
            loc1 = input("Enter first location label: ")
            loc2 = input("Enter second location label: ")
            graph.printAllPaths(loc1, loc2)
        elif (choice == 6):
            loc1 = input("Enter first location label: ")
            loc2 = input("Enter second location label: ")
            graph.minPath(loc1, loc2)
        elif (choice == 7):
            # exit program
            print("Bye bye!")