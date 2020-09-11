import sys, threading

class Wrapper:
    def __init__(self, value):
        self.value = value

class Graph:

    def __init__(self, n, edges):
        self.links = [[] for i in range(n)]
        self.n = n

        for e in edges:
            self.__addEdge(e)


    def __addEdge(self, e):
        self.links[e[0]].append(e[1])


    def dfs(self, v, exitTimesOrderedVerticies, componentIndices, currentIndex):
        componentIndices[v] = currentIndex
        for neighbour in self.links[v]:
            if componentIndices[neighbour] is None:
                self.dfs(neighbour, exitTimesOrderedVerticies, componentIndices, currentIndex)

        exitTimesOrderedVerticies.append(v)


    def getComponentsAndExitTimesOrdered(self, vertecies):
        componentIndices = [None] * self.n
        exitTimesOrderedVerticies = []
        currentIndex = 1
        for i in vertecies:
            if componentIndices[i] is None:
                self.dfs(i, exitTimesOrderedVerticies, componentIndices, currentIndex)
                currentIndex += 1
        return (list(reversed(exitTimesOrderedVerticies)), componentIndices)


class Solver():

    def solve(self):
        n, _ = map(int, input().split())
        edges = []
        invertedEdges = []
        used = set()
        for line in sys.stdin:
            v1, v2 = map(int, line.split())
            v1 -= 1; v2 -=1
            if (v1, v2) not in used:
                edges.append((v1, v2))
                invertedEdges.append((v2, v1))
                used.add((v1, v2))
            
        self.solveByParams(n, edges, invertedEdges)

    def solveByParams(self, n, edges, invertedEdges):
        graph = Graph(n, edges)
        invertedGraph = Graph(n, invertedEdges)
        vertecies = graph.getComponentsAndExitTimesOrdered(range(n))[0]
        components = invertedGraph.getComponentsAndExitTimesOrdered(vertecies)[1]
        consolidateEdges = set()
        for edge in edges:
            c1, c2 = components[edge[0]], components[edge[1]]
            if c1 != c2:
                consolidateEdges.add((c1, c2))
        print(len(consolidateEdges))

def main():
    Solver().solve()

    
sys.setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26) 
threading.Thread(target=main).start()