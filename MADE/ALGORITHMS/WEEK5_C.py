import sys

class ChainsDictionary:
    INITIAL_CAPACITY = 1_000_000
    MINIMAL_CAPACITY = 10
    BIG_PRIME_NUMBER = 1_000_000_007
    STRING_HASH_MULTIPLIER = 31

    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None


    def __init__(self, capacity = INITIAL_CAPACITY):
        self.capacity = max(capacity, self.MINIMAL_CAPACITY) 
        self.storage = [None] * capacity
        self.lastAddedNode = None


    def prev(self, key):
        node = self[key]

        if node is not None and node.prev is not None:
            return node.prev

        return None
        

    def next(self, key):
        node = self[key]

        if node is not None and node.next is not None:
            return node.next
            
        return None


    def removeKey(self, key):
        index = self.__index(key)
        chain = self.storage[index] 
        indexForRemove = None
       
        if chain is not None:
            for i, node in enumerate(chain):
                if node.key == key:
                    indexForRemove = i

        if indexForRemove is not None:
            deletedNode = chain[indexForRemove]
            if deletedNode.next is not None:
                deletedNode.next.prev = deletedNode.prev
            
            if deletedNode.prev is not None:
                deletedNode.prev.next = deletedNode.next
        
            if self.lastAddedNode is deletedNode:
                self.lastAddedNode = deletedNode.prev

            chain = list(filter(lambda node: node.key != key, chain))
            self.storage[index] = None if len(chain) == 0 else chain
    

    def __getHash(self, string):
        hashResult = 0

        for x in string:
            hashResult = (hashResult * self.STRING_HASH_MULTIPLIER + ord(x)) % self.BIG_PRIME_NUMBER

        return hashResult     


    def __getitem__(self, key):
        index = self.__index(key)
        if self.storage[index] is not None:
            for element in self.storage[index]:
                if element.key == key:
                    return element
            return None
        else:
            return None
            

    def __contains__(self, key):
        return self[key] is not None

    
    def __setitem__(self, key, value):
        index = self.__index(key)
        item = ChainsDictionary.Node(key, value)
        chain = self.storage[index]

        isNewNode = False
        if chain is not None:
            indexInChain = None

            for index, node in enumerate(chain):
                if node.key == key:
                    indexInChain = index
                    break

            if indexInChain is None:
                chain.append(item)
                isNewNode = True
            else:
                chain[indexInChain].value = value
        else:
            isNewNode = True
            self.storage[index] = [item]

        if not isNewNode:
            return
        
        if self.lastAddedNode is not None:
            self.lastAddedNode.next = item
                
        item.prev = self.lastAddedNode
        self.lastAddedNode = item


    def __index(self, element):
        return self.__getHash(element) % len(self.storage)
        


class ProblemSolver:

    def fastPrint(self, node):
        result = "none" if node is None else node.value
        sys.stdout.write(result + "\n")

    def solve(self):
        storage = ChainsDictionary()

        for line in sys.stdin:
            commands = line.split()
            command = commands[0]
            key = commands[1]
            if command == "put":
                storage[key] = commands[2]
            elif command == "get":
                result = storage[key]
                self.fastPrint(result)
            elif command == "delete":
                storage.removeKey(key)
            elif command == "prev":
                self.fastPrint(storage.prev(key))
            elif command == "next":
                self.fastPrint(storage.next(key))


ProblemSolver().solve()