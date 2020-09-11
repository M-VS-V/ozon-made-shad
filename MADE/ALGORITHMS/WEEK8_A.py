import sys

class BST:
    class Node:
        def __init__(self, key, left = None, right = None):
            self.key = key
            self.left = left
            self.right = right


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
        return v


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
        return v


    def __findMax(self, v):
        assert(v is not None)
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
            if command == 'insert':
                tree.insert(value)
            elif command == 'delete':
                tree.delete(value)
            elif command == 'exists':
                exists = str(tree.search(value) is not None).lower()
                result.append(exists)
            elif command == 'prev':
                val = tree.prev(value)
                result.append(val.key if val is not None else 'none')
            elif command == 'next':
                val = tree.next(value)
                result.append(val.key if val is not None else 'none')
        return result


    def solve(self):
        commands = []
        for c in sys.stdin:
            commands.append(c)

        [print(result) for result in self.solveByCommands(commands)]


Solver().solve()