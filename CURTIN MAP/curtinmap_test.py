from CurtinMap import *

# test below

# create graph object
curtin = CurtinMap()

# addVertex test
curtin.addVertex("A")
curtin.addVertex("B")
curtin.addVertex("C")
curtin.addVertex("D")
curtin.addVertex("E")

# print all loc test
print("="*30)
print("PRINT ALL LOC TEST")
print("="*30)
curtin.printAllLoc()

# print has vertex test
print("="*30)
print("HAS VERTEX TEST")
print("="*30)
curtin.hasVertex("A")

# get vertex test
print("="*30)
print("GET VERTEX TEST")
print("="*30)
curtin.getVertex("A")

# add edge test
print("="*30)
print("ADD EDGE TEST")
print("="*30)
curtin.addEdge("A", "B", 10)
curtin.addEdge("B", "A", 10)
curtin.addEdge("B", "C", 30)
curtin.addEdge("C", "B", 30)
curtin.addEdge("A", "C", 20)
curtin.addEdge("C", "A", 20)
curtin.addEdge("B", "D", 40)
curtin.addEdge("D", "B", 40)
curtin.addEdge("C", "D", 50)
curtin.addEdge("D", "C", 50)
curtin.addEdge("D", "E", 60)
curtin.addEdge("E", "D", 60)

# get edge test
print("="*30)
print("GET EDGE TEST")
print("="*30)
curtin.getEdge("A")

# print all loc test (second time just to make sure it still works)
print("="*30)
print("PRINT ALL LOC TEST 2")
print("="*30)
curtin.printAllLoc()

# print all path test
print("="*30)
print("PRINT ALL PATH TEST")
print("="*30)
curtin.printAllEdge()

# dfs test
print("="*30)
print("DEPTH FIRST SEARCH TEST")
print("="*30)
curtin.depthFirstSearch("B", "E")

# bfs test
print("="*30)
print("BREADTH FIRST SEARCH TEST")
print("="*30)
curtin.breadthFirstSearch("A", "D")

# find path test
print("="*30)
print("FIND PATH TEST")
print("="*30)
curtin.findPath("A", "D")

# print all path test
print("="*30)
print("PRINT ALL PATH TEST")
print("="*30)
curtin.printAllPaths("A", "D")

# min path test
print("="*30)
print("MIN PATH TEST")
print("="*30)
curtin.minPath("A", "E")
