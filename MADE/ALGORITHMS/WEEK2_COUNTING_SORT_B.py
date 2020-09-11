def sortByCount(array, minValue, maxValue):
    sortedArray = []
    countingArrayLength = maxValue - minValue + 1
    countingArray = [0] * countingArrayLength

    for value in array:
        index = value - minValue
        countingArray[index] += 1

    for value in range(countingArrayLength):
        valueCount = countingArray[value]
        if valueCount > 0:
            sortedArray += [value] * valueCount

    return sortedArray


def solveProblem():
    array = list(map(int, input().split()))
    minValue, maxValue = 0, 100
    sortedArray = sortByCount(array, minValue, maxValue)
    [print(x, end = ' ') for x in sortedArray]


solveProblem()
