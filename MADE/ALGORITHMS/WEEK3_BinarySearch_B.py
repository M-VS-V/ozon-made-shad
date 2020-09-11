import sys


def lowerBound(sortedArray, valueForApproximation):
    left = -1
    right = len(sortedArray) - 1

    while right - left >= 2:
        m = (left + right) // 2
        if valueForApproximation <= sortedArray[m]:
            right = m
        else:
            left = m

    return right


def solveForData(sortedArray, l, r):
    if r < sortedArray[0] or l > sortedArray[-1]:
        return 0

    leftIndexIncluded = lowerBound(sortedArray, l)
    rightIndexIncluded = lowerBound(sortedArray, r + 1)
    
    if sortedArray[rightIndexIncluded] > r:
        rightIndexIncluded -= 1
        
    return rightIndexIncluded - leftIndexIncluded + 1


def solveProblem():
    n = int(input())
    sortedArray = list(sorted(map(int, input().split())))
    k = int(input())
    
    for line in sys.stdin:
        l, r = map(int, line.split())
        result = solveForData(sortedArray, l, r)
        print(result)

solveProblem()