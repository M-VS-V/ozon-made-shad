def getBucketIndex(string, index, minValue):
    return ord(string[len(string) - 1 - index]) - minValue


def radixSort(stringArray, indexFromRight):
    sortedArray = []
    minValue = ord('a')
    maxValue = ord('z')
    countingArrayLength = maxValue - minValue + 1
    countingArray = [0] * countingArrayLength
    sortedArray = [-1] * len(stringArray)

    for string in stringArray:
        bucketIndex = getBucketIndex(string, indexFromRight, minValue)
        countingArray[bucketIndex] += 1

    bucketInsertIndexes = [0]
    for i in range(1, countingArrayLength):
        prevBucketInsertIndex = bucketInsertIndexes[i - 1]
        prevBucketElementsCount = countingArray[i - 1]
        currentBucketInsertIndex = prevBucketInsertIndex + prevBucketElementsCount
        bucketInsertIndexes.append(currentBucketInsertIndex)

    for string in stringArray:
        bucketIndex = getBucketIndex(string, indexFromRight, minValue)
        sortedArray[bucketInsertIndexes[bucketIndex]] = string
        bucketInsertIndexes[bucketIndex] += 1

    return [x for x in sortedArray]


def solveProblem():
    n, _, k = map(int, input().split())
    strings = []

    for _ in range(n):
        strings.append(input().strip())

    for sortIndex in range(k):
        strings = radixSort(strings, sortIndex)

    [print(x) for x in strings]


solveProblem()
