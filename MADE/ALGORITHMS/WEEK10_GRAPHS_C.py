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


    def dfs(self, v, colors, topologicalArray, hasCycleWrapper):
        if hasCycleWrapper.value:
            return

        colors[v] = 1
        for neighbour in self.links[v]:
            if colors[neighbour] == 0:
                self.dfs(neighbour, colors, topologicalArray, hasCycleWrapper)
            elif colors[neighbour] == 1:
                hasCycleWrapper.value = True
                return

        if hasCycleWrapper.value:
            return

        colors[v] = 2
        topologicalArray.append(v)

    def getTopologicalOrdered(self):
        colors = [0] * self.n
        topologicalArray = []
        hasCycleWrapper = Wrapper(False)

        for i in range(self.n):
            if colors[i] == 0:
                self.dfs(i, colors, topologicalArray, hasCycleWrapper)

        return None if hasCycleWrapper.value else reversed(topologicalArray)
    

class Solver():

    def solve(self):
        n, _ = map(int, input().split())
        edges = []
        used = set()
        for line in sys.stdin:
            v1, v2 = map(int, line.split())
            v1 -= 1; v2 -=1
            if (v1, v2) not in used:
                edges.append((v1, v2))
                used.add((v1, v2))
            
            if v1 == v2:
                print(-1)
                return
        
        self.solveByParams(n, edges)

    def solveByParams(self, n, edges):
        graph = Graph(n, edges)
        result = graph.getTopologicalOrdered()
        if result is None:
            print(-1)
        else:
            [print(x + 1, end = ' ') for x in result]
        



def main():
    Solver().solve()

    
sys.setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26) 
threading.Thread(target=main).start()