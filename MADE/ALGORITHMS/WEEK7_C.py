import sys

class FenvickTree:

    def __init__(self, a):
        self.a = a
        self.fenvickSums = [None] * len(a)
        for i in range(0, len(a)):
            sum = 0
            for j in range(self.__fenvickAnd(i), i + 1):
                sum += a[j]
            self.fenvickSums[i] = sum
    

    def set(self, i, x):
        diff = x - self.a[i]
        self.a[i] = x
        while i < len(self.a):
            self.fenvickSums[i] += diff
            i = self.__fenvickOr(i)



    def sum(self, i, j):
        if i == 0:
            return self.__prefix(j)
        return self.__prefix(j) - self.__prefix(i - 1)


    def __prefix(self, i):
        sum = 0
        while True:
            sum += self.fenvickSums[i]
            i = self.__fenvickAnd(i) - 1
            if i < 0:
                return sum


    def __fenvickAnd(self, i):
        return i & (i + 1)


    def __fenvickOr(self, i):
        return i | (i + 1)



class Solver:
    def solve(self):
        _ = int(input())
        a = list(map(int, input().split()))
        tree = FenvickTree(a)
        answers = []
        for line in sys.stdin.buffer:
            command, a, b = line.split()
            a = int(a)
            b = int(b)
            if command == "set":
                tree.set(a - 1, b)
            elif command == "sum":
                answers.append(str(tree.sum(a - 1, b - 1)))
                
        sys.stdout.write("\n".join(answers))
        sys.stdout.write("\n")


Solver().solve()