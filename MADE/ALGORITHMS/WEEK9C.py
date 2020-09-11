import random
import sys

class Treap:
    class Node():
        def __init__(self, value, y, left = None, right = None):
            self.y = y
            self.value = value
            self.right = right
            self.left = left
            self.size = 1
    
    
    def __init__(self):
        self.root = None


    def insert(self, key, value):
        self.root = self.__insert(self.root, key, value, self.__rand())


    def delete(self, x):
        self.root = self.__delete(self.root, x)


    def getArray(self):
        array = []
        def dfs(v):
            if v is None:
                return
            dfs(v.left)
            array.append(v.value)
            dfs(v.right)

        dfs(self.root)
        return array

    def print(self):
        [print(x, end = ' ') for x in self.getArray()]
        print()


    def insertAtStart(self, l, r):
        beforeLeft, afterLeft = self.__split(self.root, l - 1)
        target, afterRight = self.__split(afterLeft, r - self.__getSize(beforeLeft))
        result = self.__merge(target, beforeLeft)
        result = self.__merge(result, afterRight)
        self.root = result 


    def __rand(self):
        return random.randrange(int(1e6))


    def __split(self, v, x):
        if v is None:
            return None, None
        if self.__implicitKey(v) > x:
            t1, t2 = self.__split(v.left, x)
            v.left = t2
            self.__fix(v)
            return t1, v
        else:
            t1, t2 = self.__split(v.right, x - self.__getSize(v.left) - 1)
            v.right = t1
            self.__fix(v)
            return v, t2


    def __implicitKey(self, v):
        return self.__getSize(v.left)


    def __merge(self, t1, t2):
        if t1 is None:
            return t2
        
        if t2 is None:
            return t1

        if t1.y > t2.y:
            t1.right = self.__merge(t1.right, t2)
            self.__fix(t1)
            return t1
        else:
            t2.left = self.__merge(t1, t2.left)
            self.__fix(t2)
            return t2


    def __insert(self, t, x, value, y):
        t1, t2 = self.__split(t, x)
        node = Treap.Node(value, y)
        t1 = self.__merge(t1, node)
        return self.__merge(t1, t2)


    def __delete(self, t, x):
        t1, t2 = self.__split(t, x)
        t1Left, _ = self.__split(t1, x - 1)
        return self.__merge(t1Left, t2)
        

    def __fastInsert(self, t, x, value, y):
        node = Treap.Node(value, y)
        if t is None:
            return node

        current = t
        parent = None
        while current is not None and current.y > y:
            parent = current
            if x > current.x:
                current = current.right
            else:
                current = current.left
        
        t1, t2 = self.__split(current, x)
        node.left = t1
        node.right = t2
        
        if parent is None:
            return node
        else:
            if x < parent.x:
                parent.left = node
            else:
                parent.right = node
            return t

    def __fix(self, v):
        v.size = self.__getSize(v.left) + self.__getSize(v.right) + 1

    def __getSize(self, v):
        return 0 if v is None else v.size
        

class Solver:
    def solve(self):
        random.seed(1)
        n, m = map(int, input().split())
        array = range(1, n + 1)
        tree = Treap()

        for i in array:
            tree.insert(i - 1, i)
        
        for _ in range(m):
            l, r = map(int, input().split())
            tree.insertAtStart(l - 1, r - 1)
            
        [print(x, end = ' ') for x in tree.getArray()]


Solver().solve()