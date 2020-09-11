import sys, threading
from collections import deque

class Graph:

    def __init__(self, n, edges):
        self.links = [[] for i in range(n)]
        self.n = n

        for e in edges:
            self.__addEdge(e)


    def __addEdge(self, e):
        self.links[e[0]].append(e[1])


    def dfs(self, v, componentIndices, currentIndex):
        componentIndices[v] = currentIndex
        for neighbour in self.links[v]:
            if componentIndices[neighbour] is None:
                self.dfs(neighbour, componentIndices, currentIndex)


    def bfs(self, v, componentIndices, currentIndex):
        componentIndices[v] = currentIndex
        d = deque()
        d.append(v)
        while len(d) > 0:
            current = d.popleft()
            componentIndices[current] = currentIndex
            for neighbour in self.links[current]:
                if componentIndices[neighbour] is None:
                    d.append(neighbour)


    def getComponents(self):
        componentIndices = [None] * self.n
        currentIndex = 1
        for i in range(self.n):
            if componentIndices[i] is None:
                self.dfs(i, componentIndices, currentIndex)
                currentIndex += 1
        return componentIndices
    

class Solver():

    def solve(self):
        n, _ = map(int, input().split())
        edges = []
        for line in sys.stdin:
            v1, v2 = map(int, line.split())
            v1 -= 1; v2 -=1
            edges.append((v1, v2))
            edges.append((v2, v1))
        
        self.solveByParams(n, edges)

    def solveByParams(self, n, edges):
        graph = Graph(n, edges)
        components = graph.getComponents()
        print(len(set(components)))
        [print(x, end = ' ') for x in components]


def main():
    sys.setrecursionlimit(10 ** 9)
    threading.stack_size(2 ** 26)
    Solver().solve()


threading.Thread(target=main).start()


