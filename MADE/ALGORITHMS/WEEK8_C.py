import sys

class BST:
    class Node:
        def __init__(self, key, left = None, right = None):
            self.key = key
            self.left = left
            self.right = right
            self.height = 0
            self.nodeCount = 1


    def __init__(self):
        self.root = None


    def next(self, x):
        v, res = self.root, None
        while v is not None:
            if v.key > x:
                res = v
                v = v.left
            else:
                v = v.right
        return res


    def prev(self, x):
        v, res = self.root, None
        while v is not None:
            if v.key < x:
                res = v
                v = v.right
            else:
                v = v.left
        return res


    def insert(self, x):
        self.root = self.__insert(self.root, x)


    def delete(self, x):
        self.root = self.__delete(self.root, x)


    def search(self, x):
        return self.__search(self.root, x)


    def findMaximum(self, k):
        return self.__findMaximum(self.root, k)


    def __height(self, p):
        return p.height if p is not None else 0


    def __getNodeCount(self, v):
        return v.nodeCount if v is not None else 0


    def __findMaximum(self, v, k):
        assert(k >= 1)
        if v is None:
            return v

        rightCount = self.__getNodeCount(v.right)
        if k == rightCount + 1:
            return v
        elif k <= rightCount:
            return self.__findMaximum(v.right, k)
        else:
            return self.__findMaximum(v.left, k - (rightCount + 1))


    def __balanceFactor(self, p):
        if p is None:
            return 0
        return self.__height(p.right) - self.__height(p.left)


    def __fixHeight(self, p):
        if p is None:
            return
        hl = self.__height(p.left)
        hr = self.__height(p.right)
        if hl > hr:
            p.height = hl + 1
        else:
            p.height = hr + 1

    def __fixNodeCount(self, p):
        if p is None:
            return
        leftNodeCount = self.__getNodeCount(p.left)
        rightNodeCount = self.__getNodeCount(p.right)
        p.nodeCount = leftNodeCount + rightNodeCount + 1


    def __search(self, v, x):
        if v is None:
            return None
        if v.key == x:
            return v
        elif x < v.key:
            return self.__search(v.left, x)
        else:
            return self.__search(v.right, x)


    def __insert(self, v, x):
        if v is None:
            return BST.Node(x)
        elif x < v.key:
            v.left = self.__insert(v.left, x)
        elif x > v.key:
            v.right = self.__insert(v.right, x)
        return self.__balance(v)


    def __balance(self, p):
        self.__fixHeight(p)
        self.__fixNodeCount(p)
        if self.__balanceFactor(p) == 2:
            if self.__balanceFactor(p.right) < 0:
                p.right = self.__smallRotateRight(p.right)
            return self.__smallRotateLeft(p)
        
        if self.__balanceFactor(p) == -2:
            if self.__balanceFactor(p.left) > 0:
                p.left = self.__smallRotateLeft(p.left)
            return self.__smallRotateRight(p)
        
        return p


    def __smallRotateRight(self, p):
        q = p.left
        p.left = q.right
        q.right = p
        self.__fixHeight(p)
        self.__fixHeight(q)
        self.__fixNodeCount(p)
        self.__fixNodeCount(q)
        return q


    def __smallRotateLeft(self, q):
        p = q.right
        q.right = p.left
        p.left = q
        self.__fixHeight(q)
        self.__fixHeight(p)
        self.__fixNodeCount(q)
        self.__fixNodeCount(p)
        return p


    def __delete(self, v, x):
        if v is None:
            return None
        elif x < v.key:
            v.left = self.__delete(v.left, x)
        elif x > v.key:
            v.right = self.__delete(v.right, x)
        else:
            if v.left is None and v.right is None:
                v = None
            elif v.left is None:
                v = v.right
            elif v.right is None:
                v = v.left
            else:
                v.key = self.__findMax(v.left).key
                v.left = self.__delete(v.left, v.key)
        return self.__balance(v)


    def __findMax(self, v):
        while v.right is not None:
            v = v.right
        return v
            

class Solver:
    def getCommands(self, text):
        splittedCommands = text.split("\n")
        for c in list(filter(lambda x: x != '', splittedCommands)):
            yield c

    def solveByCommands(self, commands):
        result = []
        tree = BST()
        for c in commands:
            command, value = c.split()
            value = int(value)
            if command == '1' or command == "+1":
                tree.insert(value)
            elif command == '-1':
                tree.delete(value)
            elif command == '0':
                res = tree.findMaximum(value)
                assert(res is not None)
                result.append(res.key)
        return result


    def solve(self):
        _ = int(input())
        commands = []
        for c in sys.stdin:
            commands.append(c)

        [print(result) for result in self.solveByCommands(commands)]


Solver().solve()