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

    
    def getCutPoints(self):
        ROOT = -1
        visited = [False] * self.n
        up = [None] * self.n
        tin = [None] * self.n
        timeWrapper = Wrapper(0)
        cutpoints = []

        def dfs(v, p):
            timeWrapper.value += 1
            up[v] = tin[v] = timeWrapper.value
            visited[v] = True
            childCount = 0
            for u in self.links[v]:
                if u == p:
                    continue
                if visited[u]:
                    up[v] = min(up[v], tin[u])
                else:
                    dfs(u, v)
                    childCount += 1
                    up[v] = min(up[v], up[u])
                    if p != ROOT and up[u] >= tin[v]:
                        cutpoints.append(v + 1)

            if p == ROOT and childCount >= 2:
                cutpoints.append(v + 1)
        
        for i in range(self.n):
            if not visited[i]:
                dfs(i, ROOT)
        
        return sorted(set(cutpoints))
            




class Solver():

    def solve(self):
        n, _ = map(int, input().split())
        edges = []
        used = set()
        for line in sys.stdin:
            v1, v2 = map(int, line.split())
            v1 -= 1; v2 -=1
            if (v1, v2) not in used and v1 != v2:
                edges.append((v1, v2))
                edges.append((v2, v1))
                used.add((v1, v2))
            
        self.solveByParams(n, edges)

    def solveByParams(self, n, edges):
        graph = Graph(n, edges)
        cutPoints = graph.getCutPoints()
        print(len(cutPoints))
        [print(point, end = ' ') for point in cutPoints]

def main():
    Solver().solve()

sys.setrecursionlimit(10 ** 5)
threading.stack_size(2 ** 26) 
threading.Thread(target=main).start()