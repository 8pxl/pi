import numpy as np

class graph:
    def __init__(self, size):
        self.size = size
        self.adj = np.zeros((size, size))
        self.numNodes = 0
        print (self.adj)

    def addEdge(self, i, j, weight):
        self.adj[i][j] = weight

    def addNode(self, weight):
        if (self.size >= self.numNodes + 1):
            print("too many nodes in graph!")
            return
        self.numNodes += 1
        


    def prims(self):
        curr = 0


test = graph(50)
