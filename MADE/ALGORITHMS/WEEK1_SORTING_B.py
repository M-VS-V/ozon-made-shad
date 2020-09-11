def bubbleSortInPlace(array):
    arrayLength = len(array)
    if arrayLength < 2:
        return

    for _ in range(arrayLength):
        for second in range(1, arrayLength):
            first = second - 1
            if array[second] < array[first]:
                array[first], array[second] = array[second], array[first]
    return array

def solveProblem():
    N = int(input())
    array = list(map(int, input().split()))
    bubbleSortInPlace(array)
    [print(x, end=' ') for x in array]

solveProblem()