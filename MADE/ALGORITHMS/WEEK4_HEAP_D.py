import sys

class Heap:

    def __init__(self):
        self.storage = []
        self.storageIndexies = [None]
        self.operationNumber = 0


    def decreaseKey(self, addOperationNumber, newValue):
        self.operationNumber += 1
        self.storageIndexies.append(None)
        if self.storageIndexies[addOperationNumber] is not None:
            indexInStorage = self.storageIndexies[addOperationNumber]
            self.storage[indexInStorage] = (newValue, self.__operationNumberAtIndex(indexInStorage))
            if indexInStorage == 0:
                changedStorageIndicies = self.__siftDown(indexInStorage)
            else:
                changedStorageIndicies = self.__siftUp(indexInStorage)
            
            self.__updateStorageIndicies(changedStorageIndicies)


    def extractMin(self):
        self.operationNumber += 1
        self.storageIndexies.append(None)
        if len(self.storage) == 0:
            return None

        popped = self.storage[0]
        lastElement = self.storage.pop()
        if len(self.storage) >= 1:
            self.storage[0] = lastElement
            changedStorageIndicies = self.__siftDown(0)
            self.__updateStorageIndicies(changedStorageIndicies)

        pushIndex = popped[1]
        self.storageIndexies[pushIndex] = None

        return popped


    def push(self, element):
        self.operationNumber += 1
        self.storage.append((element, self.operationNumber))

        storageIndex = len(self.storage) - 1
        self.storageIndexies.append(len(self.storage) - 1)

        changedStorageIndicies = self.__siftUp(storageIndex)
        self.__updateStorageIndicies(changedStorageIndicies)


    def __updateStorageIndicies(self, changedStorageIndicies):
        for indicies in changedStorageIndicies:
            pushIndex = indicies[0]
            newStorageIndex = indicies[1]
            self.storageIndexies[pushIndex] = newStorageIndex


    def __siftDown(self, index):
        changedIndecies = []
        pushIndexOfSiftedNode = self.__operationNumberAtIndex(index)
        while (True):
            currentIndex = index
            leftChildIndex = self.__leftChildIndex(index)
            rightChildIndex = self.__rightChildIndex(index)
            if self.__exists(leftChildIndex) and self.__exists(rightChildIndex):
                if self.__valueAtIndex(currentIndex) > self.__valueAtIndex(leftChildIndex) \
                    or self.__valueAtIndex(currentIndex) > self.__valueAtIndex(rightChildIndex):
                    if self.__valueAtIndex(leftChildIndex) < self.__valueAtIndex(rightChildIndex):
                        changedIndecies.append((self.__operationNumberAtIndex(leftChildIndex), index))
                        self.__swap(index, leftChildIndex)
                        index = leftChildIndex
                    else:
                        changedIndecies.append((self.__operationNumberAtIndex(rightChildIndex), index))
                        self.__swap(index, rightChildIndex)
                        index = rightChildIndex
                else:
                    changedIndecies.append((pushIndexOfSiftedNode, index))
                    break
            elif self.__exists(leftChildIndex) and self.__valueAtIndex(index) > self.__valueAtIndex(leftChildIndex):
                changedIndecies.append((self.__operationNumberAtIndex(leftChildIndex), index))
                self.__swap(index, leftChildIndex)
                index = leftChildIndex
            elif self.__exists(rightChildIndex) and self.__valueAtIndex(index) > self.__valueAtIndex(rightChildIndex):
                changedIndecies.append((self.__operationNumberAtIndex(rightChildIndex), index))
                self.__swap(index, rightChildIndex)
                index = rightChildIndex
            else:
                changedIndecies.append((pushIndexOfSiftedNode, index))
                break
        return changedIndecies
            

    def __siftUp(self, index):
        changedIndecies = []
        pushIndexOfSiftedNode = self.__operationNumberAtIndex(index)
        parentIndex = self.__parentIndex(index)
        while self.__valueAtIndex(index) < self.__valueAtIndex(parentIndex):
            pushIndex = self.__operationNumberAtIndex(parentIndex)
            newStorageIndex = index
            changedIndecies.append((pushIndex, newStorageIndex))

            self.__swap(index, parentIndex)
            index = parentIndex
            parentIndex = self.__parentIndex(index)
       
        changedIndecies.append((pushIndexOfSiftedNode, index))
        return changedIndecies


    def __valueAtIndex(self, index):
        return self.storage[index][0]


    def __operationNumberAtIndex(self, index):
        return self.storage[index][1]


    def __exists(self, index):
        return index >= 0 and index < len(self.storage)


    def __swap(self, index1, index2):
        self.storage[index1], self.storage[index2] = self.storage[index2], self.storage[index1]


    def __parentIndex(self, index):
        if index == 0:
            return 0
        return (index - 1) // 2


    def __leftChildIndex(self, index):
        return 2 * index + 1


    def __rightChildIndex(self, index):
        return 2 * index + 2



class ProblemSolver:

    def solve1(self, text):
        minHeap = Heap()
        answ = []
        splitter = list(filter(lambda x: x != '', text.split("\n")))
        for line in splitter:
            commands = line.split()
            heapCommand = commands[0] 

            if heapCommand == "push":
                value = int(commands[1])
                minHeap.push(value)
            elif heapCommand == "extract-min":
                result = minHeap.extractMin()
                if result is None:
                    answ.append("*")
                else:
                    answ.append(f'{result[0]} {result[1]}')
            elif heapCommand == "decrease-key":
                addOperationNumber = int(commands[1])
                newValue = int(commands[2])
                popped = minHeap.decreaseKey(addOperationNumber, newValue)
            else:
                assert(False)
                return
        return answ

    def solve(self):
        minHeap = Heap()

        for line in sys.stdin:
            commands = line.split()
            heapCommand = commands[0] 

            if heapCommand == "push":
                value = int(commands[1])
                minHeap.push(value)
            elif heapCommand == "extract-min":
                result = minHeap.extractMin()
                if result is None:
                    print("*")
                else:
                    print(f'{result[0]} {result[1]}')
            elif heapCommand == "decrease-key":
                addOperationNumber = int(commands[1])
                newValue = int(commands[2])
                popped = minHeap.decreaseKey(addOperationNumber, newValue)
            else:
                assert(False)
                return


# ProblemSolver().solve()   

text = """
extract-min
extract-min
push 10
push 8
push 6
push 9
decrease-key 1 4
decrease-key 2 2
decrease-key 3 -1
extract-min
decrease-key 1 1
decrease-key 1 1
extract-min
decrease-key 3 2
extract-min
extract-min
extract-min
push 1
push 2
extract-min
extract-min
push 1
push 2
decrease-key 22 1
decrease-key 23 0
extract-min
extract-min
"""
print(ProblemSolver().solve1(text))

