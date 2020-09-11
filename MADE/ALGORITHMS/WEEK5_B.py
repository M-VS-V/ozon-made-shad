import sys

class ChainsDictionary:
    INITIAL_CAPACITY = 1_000_000 
    MINIMAL_CAPACITY = 10
    BIG_PRIME_NUMBER = 1_000_000_007
    STRING_HASH_MULTIPLIER = 31

    def __init__(self, capacity = INITIAL_CAPACITY):
        self.capacity = max(capacity, self.MINIMAL_CAPACITY) 
        self.storage = [None] * capacity


    def removeKey(self, key):
        index = self.__index(key)
        if self.storage[index] is not None:
            self.storage[index] = list(filter(lambda x: x[0] != key, self.storage[index]))
            if len(self.storage[index]) == 0:
                self.storage[index] = None
    

    def __getHash(self, string):
        hashResult = 0

        for x in string:
            hashResult = (hashResult * self.STRING_HASH_MULTIPLIER + ord(x)) % self.BIG_PRIME_NUMBER

        return hashResult     

    def __getitem__(self, key):
        index = self.__index(key)
        if self.storage[index] is not None:
            for element in self.storage[index]:
                if element[0] == key:
                    return element[1]
            return None
        else:
            return None
            

    def __contains__(self, key):
        return self[key] is not None

    
    def __setitem__(self, key, value):
        index = self.__index(key)
        item = (key, value)
        chain = self.storage[index]
        if chain is not None:
            indexInChain = None
            for index, element in enumerate(chain):
                if element[0] == key:
                    indexInChain = index
                    break
            if indexInChain is None:
                chain.append(item)
            else:
                chain[indexInChain] = item
        else:
             self.storage[index] = [item]


    def __index(self, element):
        return self.__getHash(element) % len(self.storage)
        


class ProblemSolver:

    def solve(self):
        storage = ChainsDictionary()

        for line in sys.stdin:
            commands = line.split()
            command = commands[0]
            key = commands[1]
            if command == "put":
                storage[key] = commands[2]
            elif command == "get":
                result = storage[key] if key in storage else "none"
                sys.stdout.write(result + "\n")
            elif command == "delete":
                storage.removeKey(key)


ProblemSolver().solve()