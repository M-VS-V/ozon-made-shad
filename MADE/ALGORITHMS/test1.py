import sys
 
class SegmentTree:
    MIN_VALUE_NEUTRAL = 10**18 + 1
    ADD_VALUE_NEUTRAL = 0
    def __init__(self):
        self.t = []
        self.addValueUpdates = []
        self.setValueUpdates = []
 
    def build(self, a):
        x = 1
        n = len(a)
        
        while x < n:
            x *= 2
 
        self._n = x
    
        nodeCount = x * 2 - 1
        self.t = [self.MIN_VALUE_NEUTRAL] * nodeCount
        self.leftchilds = [None] * nodeCount
        self.rightchilds = [None] * nodeCount
        self.addValueUpdates = [self.ADD_VALUE_NEUTRAL] * nodeCount
        self.setValueUpdates = [None] * nodeCount
        firstIndexOfBottomLayer = x - 1
 
        for i in range(0, nodeCount):
            self.leftchilds[i] = 2 * i + 1
            self.rightchilds[i] = 2 * i + 2
       
        for i in range(0, n):
            self.t[firstIndexOfBottomLayer + i] = a[i]
        
        for v in range(x - 2, -1, -1):
            self.t[v] = min(self.t[self.leftchilds[v]], self.t[self.rightchilds[v]])
 
 
    #0, 0, n - 1
    #l, r - query range
    def rmq(self, v, tl, tr, l, r):
        if l > r:
            return self.MIN_VALUE_NEUTRAL
        if (l == tl and r == tr):
            return self.trueMinimum(v)
 
        self.push(v, tl, tr)
        tm = (tl + tr) // 2
 
        leftChild = self.leftchilds[v]
        rightChild = self.rightchilds[v]
        return min(self.rmq(leftChild, tl, tm, l, min(r, tm)), self.rmq(rightChild, tm + 1, tr, max(l, tm + 1), r))
 
 
    def trueMinimum(self, v):
        if self.setValueUpdates[v] is None:
            return self.t[v] + self.addValueUpdates[v]
        else:
            return self.setValueUpdates[v]
 
 
    def addValue(self, v, tl, tr, l, r, add):
        if l > r:
            return
        if l == tl and tr == r:
            self.pushAddValueIntoNode(v, add)
        else:
            self.push(v, tl, tr)
            tm = (tl + tr) // 2
            leftChild = self.leftchilds[v]
            rightChild = self.rightchilds[v]
            self.addValue(leftChild, tl, tm, l, min(r, tm), add)
            self.addValue(rightChild, tm + 1, tr, max(l, tm + 1), r, add)
            self.t[v] = min(self.trueMinimum(leftChild), self.trueMinimum(rightChild))
 
 
    def setValue(self, v, tl, tr, l, r, color):
        if l > r:
            return
        if l == tl and tr == r:
            if self.setValueUpdates[v] is None:
                self.setValueUpdates[v] = color
            self.addValueUpdates[v] = self.ADD_VALUE_NEUTRAL
        else:
            self.push(v, tl, tr)
            tm = (tl + tr) // 2
            
            leftChild = self.leftchilds[v]
            rightChild = self.rightchilds[v]
            self.setValue(leftChild, tl, tm, l, min(r, tm), color)
            self.setValue(rightChild, tm + 1, tr, max(l, tm + 1), r, color)
            self.t[v] = min(self.trueMinimum(leftChild), self.trueMinimum(rightChild))
 
    def pushAddValueIntoNode(self, v, addValue):
        if self.setValueUpdates[v] is None: 
            self.addValueUpdates[v] += addValue
        else:
            self.setValueUpdates[v] += addValue
            self.addValueUpdates[v] = self.ADD_VALUE_NEUTRAL
 
 
 
    def push(self, v, l, r):
        leftChild = self.leftchilds[v]
        rightChild = self.rightchilds[v]
        if l == r:
            self.t[v] = self.trueMinimum(v)
        else:
            if (self.setValueUpdates[v] is not None):
                if self.setValueUpdates[leftChild] is None:
                    self.setValueUpdates[leftChild] = self.setValueUpdates[v]
                if self.setValueUpdates[rightChild] is None:
                    self.setValueUpdates[rightChild] = self.setValueUpdates[v]
            else:
                addVal = self.addValueUpdates[v]
                self.pushAddValueIntoNode(leftChild, addVal)
                self.pushAddValueIntoNode(rightChild, addVal)
        self.t[v] = min(self.trueMinimum(leftChild), self.trueMinimum(rightChild))
        self.setValueUpdates[v] = None
        self.addValueUpdates[v] = self.ADD_VALUE_NEUTRAL
 
    
 
    def __leftChild(self, i):
        return 2 * i + 1
 
 
    def __rightChild(self, i):
        return 2 * i + 2
 
 
class Solver:
 
    def solveForQueries(self, n, queries):
        print("begin")
        a = [SegmentTree.MIN_VALUE_NEUTRAL] * n
        queries = sorted(queries, key = lambda x: -x[2])
        tree = SegmentTree()
        tree.build(a)
        for i, j, q in queries:
            tree.setValue(0, 0, tree._n - 1, i, j, q)
        possibleArray = [SegmentTree.MIN_VALUE_NEUTRAL] * n 
        print(possibleArray)
        for i in range(n):
            possibleArray[i] = tree.rmq(0, 0, tree._n - 1, i, i)
 
        checkerTree = SegmentTree()
        checkerTree.build(possibleArray)
        for i, j, q in queries:
            rmq = checkerTree.rmq(0, 0, checkerTree._n - 1, i, j)
            if rmq != q:
                return None
        return possibleArray
 
 
    def solve(self):
        n, m = list(map(int, input().split()))
        queries = []
 
        for i in range(m):
            i, j, q = list(map(int, input().split()))
            queries.append((i - 1, j - 1, q))
 
        result = self.solveForQueries(n,queries)
 
        if result is None:
            print('inconsistent')
        else:
            print('consistent')
            [print(x, end=' ') for x in result]
        
Solver().solve()
 
# import random
# import numpy as np
# np.random.seed(114)
 
# def answer(array, l, r):
#     return min(array[l:r+1])
 
 
# def generateAllQueries(array):
#     allQueries = []
#     for i in range(len(array)):
#         for j in range(i, len(array)):
#             allQueries.append((i, j, answer(array, i, j)))
#     return allQueries
 
 
# def testForArray(array):
#     allQueries = generateAllQueries(array)
#     for percent in [0.1, 0.2, 0.5, 1.0]:
#         queriesLen = int(percent * len(allQueries))
#         queries = random.sample(allQueries, queriesLen)
#         solutionArray = Solver().solveForQueries(len(array), queries)
#         for i, j, q in queries:
#             ans = answer(array, i, j)
#             pred = answer(solutionArray, i, j)
#             assert(ans == pred)
 
# for arrayLen in range(1, 100):
#     print(f'tested={arrayLen}')
#     randomArray = random.sample(range(-2**31, 2**31), arrayLen)
#     testForArray(randomArray)
 
# #print(random.sample([1,2,3,4,5,6,7,8,9,10], 3))
# # print(Solver().solveForQueries(3, [(0, 1, 1), (1, 2, 2)]))
# # print(Solver().solveForQueries(3, [(0, 1, 1), (0, 0, 2), (1,2,2)]))
 
# print(random.sample(range(10, 100), 2))