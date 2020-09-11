class Counter:
    def __init__(self, count):
        self.count = count

def merge(a, b, inversionCounter):
    aIndex = 0
    bIndex = 0
    resultArray = []
    while aIndex < len(a) and bIndex < len(b):
        if a[aIndex] <= b[bIndex]:
            resultArray.append(a[aIndex])
            aIndex += 1
        else:
            inversionCounter.count += len(a) - aIndex
            resultArray.append(b[bIndex])
            bIndex += 1

    if aIndex < len(a):
        resultArray += a[aIndex:len(a)]
    
    if bIndex < len(b):
        resultArray += b[bIndex:len(b)]

    return resultArray

def mergeSort(array, inversionCounter):
    arrayLength = len(array)
    if arrayLength < 2:
        return array
    
    midIndex = arrayLength // 2
    lefSideSortedArray = mergeSort(array[0:midIndex], inversionCounter)
    rightSideSortedArray = mergeSort(array[midIndex:arrayLength], inversionCounter)

    return merge(lefSideSortedArray, rightSideSortedArray, inversionCounter)
    
def solveProblem():
    N = int(input())
    inversionCounter = Counter(0)
    array = list(map(int, input().split()))
    mergeSort(array, inversionCounter)
    print(inversionCounter.count)

solveProblem()