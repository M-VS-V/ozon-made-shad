import sys

class BST:
    SUM_NEUTRAL_ELEMENT = 0

    class Node:
        def __init__(self, key, left = None, right = None):
            self.key = key
            self.left = left
            self.right = right
            self.height = 0
            self.sum = key


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


    def findSum(self, l, r):
        return self.__findSum(self.root, l, r, None)


    def __height(self, p):
        return p.height if p is not None else 0


    def __safeSum(self, v):
        return v.sum if v is not None else BST.SUM_NEUTRAL_ELEMENT


    def __findSum(self, v, l, r, parentValue):
        assert(l <= r)
        if v is None:
            return BST.SUM_NEUTRAL_ELEMENT
        leftChild = v.left
        rightChild = v.right
        if r <= v.key:
            return (v.key if r == v.key else BST.SUM_NEUTRAL_ELEMENT) +  self.__findSum(leftChild, l, r, v.key)
        elif l >= v.key:
            return (v.key if l == v.key else BST.SUM_NEUTRAL_ELEMENT) +  self.__findSum(rightChild, l, r, v.key)
        # l < v.key < r
        else:
            result = v.key
            
            if parentValue == r:
                result += self.__safeSum(rightChild)
                result += self.__findSum(leftChild, l, v.key, v.key)
            elif parentValue == l: 
                result += self.__safeSum(leftChild)
                result += self.__findSum(rightChild, v.key, r, v.key)  
            else:
                result += self.__findSum(leftChild, l, v.key, v.key) +  self.__findSum(rightChild, v.key, r, v.key)
            return result


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

    def __fixSum(self, p):
        if p is None:
            return
        leftNodeSum = self.__safeSum(p.left)
        rightNodeSum = self.__safeSum(p.right)
        p.sum = leftNodeSum + rightNodeSum + p.key


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
        self.__fixSum(p)
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
        self.__fixSum(p)
        self.__fixSum(q)
        return q


    def __smallRotateLeft(self, q):
        p = q.right
        q.right = p.left
        p.left = q
        self.__fixHeight(q)
        self.__fixHeight(p)
        self.__fixSum(q)
        self.__fixSum(p)
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

    def solveByCommands(self, lines):
        result = []
        tree = BST()
        prev = None
        MOD_CONSTANT = int(1e9)
        for line in lines:
            tokens = line.split()
            command = tokens[0]
            if command == '+':
                value = int(tokens[1])
                if prev is not None:
                    value = (value + prev) % MOD_CONSTANT
                    prev = None
                tree.insert(value)
            elif command == '?':
                l, r = int(tokens[1]), int(tokens[2])
                res = tree.findSum(l, r)
                prev = res
                result.append(res)
        return result 


    def solve(self):
        _ = int(input())
        commands = []
        for c in sys.stdin:
            commands.append(c)

        [print(result) for result in self.solveByCommands(commands)]


Solver().solve()