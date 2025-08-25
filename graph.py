import numpy as np
import sys

class graph:
    def __init__(self, size):
        self.size = size
        self.adj = np.zeros((size, size))
        self.numNodes = 0

    def addNode(self, weight):
        #TODO: i think theres a weird off by 1 error here im not sure
        if (self.size <= self.numNodes + 1):
            print("too many nodes in graph!")
            return
        self.numNodes += 1
        for i in range(self.numNodes):
            self.adj[i][self.numNodes] = weight
            self.adj[self.numNodes][i] = weight
    def debug(self):
        print(self.adj)

    def prims(self):
        sol = {} 
        vis = [0]
        toVis = [i for i in range(0, self.numNodes)]
        #we've already visited the first node
        toVis[0] = -1

        while (len(vis) < self.numNodes):
            lc = np.inf
            start = -1
            end = -1
            print(f"vis: {vis}")
            print(f"tovis: {toVis}")
            for i in vis:
                for j in toVis:
                    if j == -1:
                        continue
                    cost = self.adj[i][j]
                    print(cost)
                    if (cost < lc):
                        lc = cost
                        start = i
                        end = j
            toVis[end] = -1
            vis.append(end)
            if start in sol:
                sol[start].append(end)
            else:
                sol[start] = [end]
        return sol
test = graph(14)
for i in range(1, 14):
    test.addNode(i)
np.set_printoptions(threshold=sys.maxsize)
test.debug()
# print(test.prims())
