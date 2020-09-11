import sys

class BST:
    class Node:
        def __init__(self, key, left = None, right = None):
            self.key = key
            self.left = left
            self.right = right
            self.height = 0


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


    def __height(self, p):
        return p.height if p is not None else 0


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
        return q


    def __smallRotateLeft(self, q):
        p = q.right
        q.right = p.left
        p.left = q
        self.__fixHeight(q)
        self.__fixHeight(p)
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
            if command == 'insert':
                tree.insert(value)
            elif command == 'delete':
                tree.delete(value)
            elif command == 'exists':
                exists = str(tree.search(value) is not None).lower()
                result.append(exists)
            elif command == 'prev':
                val = tree.prev(value)
                val = val.key if val is not None else 'none'
                result.append(val)
            elif command == 'next':
                val = tree.next(value)
                val = val.key if val is not None else 'none'
                result.append(val)
        return result

    def solve(self):
        commands = []
        for c in sys.stdin:
            commands.append(c)

        [print(result) for result in self.solveByCommands(commands)]



text = """
exists 2
next 4
delete 3
prev 3
insert 4
prev 4
exists 3
insert 0
exists 4
insert 2
insert 3
insert 1
exists 0
insert 4
insert 0
prev 0
insert 2
exists 4
delete 2
prev 3
"""

result = Solver().solveByCommands(Solver().getCommands(text))
print("\n".join(map(lambda x: str(x), result)))