import sys

class CyclicArrayBasedQueue:

    DEFAULT_INITIAL_CAPACITY = 3
    MINIMAL_CAPACITY = 3
    GROW_COEEFICIENT = 2

    def __init__(self, initialCapacity = DEFAULT_INITIAL_CAPACITY):
        self.capacity = max(initialCapacity, self.MINIMAL_CAPACITY)
        self.storage = [None] * initialCapacity
        self.size = 0
        self.head = None
        self.tail = None

    def appendTail(self, element):
        if self.size == self.capacity:
            self.__ensureCapacity(True)

        if self.isEmpty():
            self.head = 0
            self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.capacity
            
        self.storage[self.tail] = element
        self.size += 1
        

    def popHead(self):
        if self.isEmpty():
            return None

        if self.size <= self.capacity / 4:
            self.__ensureCapacity(False)

        popped = self.storage[self.head]
        self.storage[self.head] = None
        self.size -= 1

        if self.isEmpty():
            head = None
            tail = None
        else:
            self.head = (self.head + 1) % self.capacity

        return popped


    def isEmpty(self):
        return self.size == 0

    def __ensureCapacity(self, isGrow):
        newCapacity = self.capacity * self.GROW_COEEFICIENT if isGrow \
            else max(self.capacity // self.GROW_COEEFICIENT, self.MINIMAL_CAPACITY)
        
        if newCapacity == self.capacity:
            return

        extendedList = [None] * newCapacity

        if self.tail == self.head:
            extendedList[0] = self.storage[self.head]
        else:
            index = self.head
            newIndex = 0
            
            while index != self.tail:
                extendedList[newIndex] = self.storage[index]
                newIndex += 1
                index = (index + 1) % self.capacity

            extendedList[newIndex] = self.storage[index]

        self.capacity = newCapacity
        self.storage = extendedList
        self.head = 0
        self.tail = self.size - 1


m = int(input())
q = CyclicArrayBasedQueue()
for line in sys.stdin:
    commands = line.split()
    if commands[0] == "+":
        q.appendTail(commands[1])
    else:
        print(q.popHead())