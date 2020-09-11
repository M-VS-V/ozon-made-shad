import random
import sys


class Treap:
    class Node():
        def __init__(self, x, y, left = None, right = None):
            self.x = x
            self.y = y
            self.right = right
            self.left = left
    
    
    def __init__(self):
        self.root = None


    def next(self, x):
        v, res = self.root, None
        while v is not None:
            if v.x > x:
                res = v
                v = v.left
            else:
                v = v.right
        return res


    def prev(self, x):
        v, res = self.root, None
        while v is not None:
            if v.x < x:
                res = v
                v = v.right
            else:
                v = v.left
        return res

    def search(self, x):
        return self.__search(self.root, x)


    def insert(self, x):
        if self.search(x) is None:
            self.root = self.__fastInsert(self.root, x, self.__rand())

    def delete(self, x):
        self.root = self.__delete(self.root, x)

    
    def __rand(self):
        return random.randrange(int(1e6))


    def __split(self, v, x):
        if v is None:
            return None, None
        if v.x > x:
            t1, t2 = self.__split(v.left, x)
            v.left = t2
            return t1, v
        else:
            t1, t2 = self.__split(v.right, x)
            v.right = t1
            return v, t2


    def __search(self, v, x):
        if v is None:
            return None
        if v.x == x:
            return v
        elif x < v.x:
            return self.__search(v.left, x)
        else:
            return self.__search(v.right, x)


    def __merge(self, t1, t2):
        if t1 is None:
            return t2
        
        if t2 is None:
            return t1

        if t1.y > t2.y:
            t1.right = self.__merge(t1.right, t2)
            return t1
        else:
            t2.left = self.__merge(t1, t2.left)
            return t2


    def __insert(self, t, x, y):
        t1, t2 = self.__split(t, x)
        node = Treap.Node(x, y)
        t1 = self.__merge(t1, node)
        return self.__merge(t1, t2)


    def __delete(self, t, x):
        t1, t2 = self.__split(t, x)
        t1Left, _ = self.__split(t1, x - 1)
        return self.__merge(t1Left, t2)
        

    def __fastInsert(self, t, x, y):
        node = Treap.Node(x, y)
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
        

class Solver:
    def getCommands(self, text):
        splittedCommands = text.split("\n")
        for c in list(filter(lambda x: x != '', splittedCommands)):
            yield c


    def solveByCommands(self, commands):
        result = []
        tree = Treap()
       
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
                result.append(val.x if val is not None else 'none')
            elif command == 'next':
                val = tree.next(value)
                result.append(val.x if val is not None else 'none')
        return result


    def solve(self):
        commands = []
        for c in sys.stdin:
            commands.append(c)

        [print(result) for result in self.solveByCommands(commands)]


Solver().solve()