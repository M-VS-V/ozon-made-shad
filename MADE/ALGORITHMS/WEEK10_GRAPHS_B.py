import sys

class Graph:


    def __init__(self, n, edges):
        self.links = [[] for i in range(n)]
        self.n = n

        for e in edges:
            self.__addEdge(e)


    def __addEdge(self, e):
        self.links[e[0]].append(e[1])


    def dfs(self, v, used, depth, maxDepth):
        used.add(v)
        maxDepth[0] = max(maxDepth[0], depth)
        for neighbour in self.links[v]:
            if neighbour not in used:
                self.dfs(neighbour, used, depth + 1, maxDepth)


    def getMaxDepth(self):
        maxDepth = [0]
        used = set()
        self.dfs(0, used, 0, maxDepth)
        return maxDepth[0] + 1



class Solver():

    def solve(self):
        _ = int(input())
        edges = []
        dic = {
            "polycarp" : 0
        }
        index = 1
        for line in sys.stdin:
            v1, _, v2 = line.split()
            v1 = v1.lower()
            v2 = v2.lower()
            if v1 not in dic:
                dic[v1] = index
                index += 1

            if v2 not in dic:
                dic[v2] = index
                index += 1
            
            edges.append((dic[v2], dic[v1]))

        self.solveByParams(len(dic), edges)

    def solveByParams(self, n, edges):
        print(Graph(n, edges).getMaxDepth())


Solver().solve()


