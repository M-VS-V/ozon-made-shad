from operator import sub, add, mul

operators = {
    "-": sub,
    "+": add,
    "*": mul
}

class DynamicList:

    DEFAULT_INITIAL_CAPACITY = 10
    MINIMAL_CAPACITY = 10
    GROW_COEEFICIENT = 2

    def __init__(self, initialCapacity = DEFAULT_INITIAL_CAPACITY):
        self.capacity = max(initialCapacity, self.MINIMAL_CAPACITY)
        self.storage = [None] * initialCapacity
        self.size = 0


    def append(self, element):
        if self.size == self.capacity:
            self.__ensureCapacity(True)

        self.storage[self.size] = element
        self.size += 1
        

    def pop(self):
        if self.size == 0:
            return None

        popped = self.storage[self.size - 1]
        self.size -= 1

        if self.size <= self.capacity / 4:
            self.__ensureCapacity(False)

        return popped


    def peek(self):
        if self.size == 0:
            return None

        return self.storage[self.size - 1]


    def __ensureCapacity(self, isGrow):
        newCapacity = self.capacity * self.GROW_COEEFICIENT if isGrow \
            else max(self.capacity // self.GROW_COEEFICIENT, self.MINIMAL_CAPACITY)
        
        self.capacity = newCapacity
        extendedList = [None] * self.capacity

        for index in range(self.size):
            extendedList[index] = self.storage[index]
        
        self.storage = extendedList


class ProblemSolver:
    def solve(self):
        stack = DynamicList()

        for x in input().split():
            if x in ["-", "+", "*"]:
                last = stack.pop()
                prev = stack.pop()
                stack.append(operators[x](prev, last))
            else:
                stack.append(int(x))

        print(stack.pop())


ProblemSolver().solve()