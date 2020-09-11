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



class OpenAddressingMap:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            
    DEFAULT_CAPACITY = int(1e7)
    DUMMY_NODE = Node(int(1e9) + 1, int(1e9) + 1)
<<<<<<< HEAD
    BIG_PRIME_NUMBER = 1_000_000_007
    STRING_HASH_MULTIPLIER = 31
=======

>>>>>>> fb57725... Add algorithms solutions WEEK5

    def __init__(self):
        self.capacity = self.DEFAULT_CAPACITY
        self.storage = [None] * self.capacity


    def getIndex(self, key):
<<<<<<< HEAD
        return self.__getHash(key) % self.capacity


    def __getHash(self, string):
        hashResult = 0

        for x in string:
            hashResult = (hashResult * self.STRING_HASH_MULTIPLIER + ord(x)) % self.BIG_PRIME_NUMBER

        return hashResult   

    def insertNode(self, key, value):
        node = OpenAddressingMap.Node(key, value)
=======
        result = abs(key)
        result *= 31
        return result % self.capacity



    def insertNode(self, key, value):
        node = Node(key, value)
>>>>>>> fb57725... Add algorithms solutions WEEK5
        index = self.getIndex(key)

        while self.storage[index] is not None  \
            and self.storage[index] != key \
            and self.storage[index] is not self.DUMMY_NODE:

            index += 1
            index %= self.capacity

<<<<<<< HEAD
        self.storage[index] = node


    def remove(self, key):
=======
            self.storage[index] = node


    def deleteNode(self, key):
>>>>>>> fb57725... Add algorithms solutions WEEK5
        index = self.getIndex(key)

        while self.storage[index] is not None:
            if self.storage[index].key == key:
                self.storage[index] = self.DUMMY_NODE

            index += 1
            index %= self.capacity



<<<<<<< HEAD
    def __contains__(self, key): 
=======
    def contains(self, key): 
>>>>>>> fb57725... Add algorithms solutions WEEK5
        return self[key] is not None

    
    def __getitem__(self, key):
        index = self.getIndex(key)

        while self.storage[index] is not None:
            if self.storage[index].key == key:
                return self.storage[index]

            index += 1
            index %= self.capacity

        return None


class ProblemSolver:
<<<<<<< HEAD
    DUMMY_VALUE = -1

    def solve(self):
        storage = OpenAddressingMap()
        for line in stdin:
            command, value = line.split()
            if command == "insert":
                storage.insertNode(value, self.DUMMY_VALUE)
=======

    def solve(self):
        storage = set()
        for line in stdin:
            command, value = line.split()
            if command == "insert":
                storage.add(value)
>>>>>>> fb57725... Add algorithms solutions WEEK5
            elif command == "exists":
                result = "true" if value in storage else "false"
                print(result)
            elif command == "delete":
                if value in storage:
                    storage.remove(value)


ProblemSolver().solve()