import sys

from sys import stdout, stdin
from io import IOBase, BytesIO
from os import read, write, fstat
 
BUFSIZE = 8192
 
 
class FastIO(IOBase):
    newlines = 0
 
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = read(self._fd, max(fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self, size: int = ...):
        while self.newlines == 0:
            b = read(self._fd, max(fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
 
 
def print(*args, **kwargs):
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop("sep", " "), kwargs.pop("file", stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(kwargs.pop("end", "\n"))
    if kwargs.pop("flush", False):
        file.flush()
 
 
stdin, stdout = IOWrapper(stdin), IOWrapper(stdout)
input = lambda: stdin.readline().rstrip("\r\n")




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
                self.setValueUpdates[leftChild] \
                    = self.setValueUpdates[rightChild] \
                    = self.setValueUpdates[v]
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

    def __init__(self):
        self.tree = SegmentTree()

    def solveCommands(self, string):
        commands = list(filter(lambda x: x != '', string.split("\n")))
        a =  list(map(int, commands[1].split()))
        self.tree.build(a)
        answers = []
        for line in commands[2:]:
            values = line.split()
            command = values[0]
            if command == 'min':
                l, r = int(values[1]) - 1, int(values[2]) - 1
                answers.append(self.tree.rmq(0, 0, self.tree._n - 1, l, r))
            elif command == 'add':
                l, r, add = int(values[1]) - 1, int(values[2]) - 1, int(values[3])
                self.tree.addValue(0, 0, self.tree._n - 1, l, r, add)
            elif command == 'set':
                l, r, valueForSet = int(values[1]) - 1, int(values[2]) - 1, int(values[3])
                self.tree.setValue(0, 0, self.tree._n - 1, l, r, valueForSet)
        return answers

    def solve(self):
        _ = input()
        a = list(map(int, input().split()))
        n = len(a)
        self.tree.build(a)

        for line in stdin:
            values = line.split()
            command = values[0]
            if command == 'min':
                l, r = int(values[1]) - 1, int(values[2]) - 1
                print(self.tree.rmq(0, 0, self.tree._n - 1, l, r))
            elif command == 'add':
                l, r, add = int(values[1]) - 1, int(values[2]) - 1, int(values[3])
                self.tree.addValue(0, 0, self.tree._n - 1, l, r, add)
            elif command == 'set':
                l, r, valueForSet = int(values[1]) - 1, int(values[2]) - 1, int(values[3])
                self.tree.setValue(0, 0, self.tree._n - 1, l, r, valueForSet)

Solver().solve()
# assert(Solver().solveCommands(
# """
# 5
# 1 2 3 4 5
# min 2 5
# min 1 5
# min 1 4
# min 2 4
# set 1 3 10
# add 2 4 4
# min 2 5
# min 1 5
# min 1 4
# min 2 4
# """
# ) == [2,1,1,2,5,5,8,8])

# assert(Solver().solveCommands(
# """
# 1
# 10
# min 1 1
# set 1 1 -2
# min 1 1
# set 1 1 3
# min 1 1
# add 1 1 1
# min 1 1
# add 1 1 0
# min 1 1
# set 1 1 123
# min 1 1 123
# """
# ) == [10, -2, 3, 4, 4, 123])

# assert(Solver().solveCommands(
# """
# 2
# 1 2
# min 1 2
# set 1 1 3
# set 2 2 4
# min 1 2
# set 1 2 10
# min 1 2
# add 1 2 10
# min 1 2
# add 1 1 1
# min 1 2
# """
# ) == [1, 3, 10, 20, 20])

# assert(Solver().solveCommands(
# """
# 4
# 4 3 2 1
# min 1 1
# min 1 2
# min 1 3
# min 1 4
# add 2 4 10
# min 1 1
# min 1 2
# min 1 3
# min 1 4
# min 3 4
# """
# ) == [4, 3, 2, 1, 4, 4, 4, 4, 11])