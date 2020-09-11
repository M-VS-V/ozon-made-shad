import sys

class ChainsDictionary:
    INITIAL_CAPACITY = 100_000
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
    

    def allElements(self):
        for chain in self.storage:
            if chain is None:
                continue
            for keyValuePair in chain:
                yield (keyValuePair[0], keyValuePair[1])


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
        

class ChainsSet:
    DEFAULT_CAPACITY = 1000

    def __init__(self, capacity = DEFAULT_CAPACITY):
        self.dic = ChainsDictionary(capacity = capacity)

    def allElements(self):
        return map(lambda keyValuePair: keyValuePair[0], self.dic.allElements())

    def add(self, key):
        self.dic[key] = True


    def removeKey(self, key):
        self.dic.removeKey(key)


    def __contains__(self, key):
        return self.dic[key] is not None

def solve():
    dic = ChainsDictionary()
    for line in sys.stdin:
        commands = line.split()
        command = commands[0] 
        key = commands[1]
        if command == "put":
            value = commands[2]
            if dic[key] is None:
                dic[key] = ChainsSet()
                dic[key].add(value)
            else:
                dic[key].add(value)
        elif command == "delete":
            value = commands[2]
            if key in dic and value in dic[key]:
                dic[key].removeKey(value)
        elif command == "deleteall":
            dic.removeKey(key)
        elif command == "get":
            if dic[key] is None:
                print(0)
            else:
                sequence = list(dic[key].allElements())
                print(f"{len(sequence)} {' '.join(sequence)}")


solve()
