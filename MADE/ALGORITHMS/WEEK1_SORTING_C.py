def merge(a, b):
    aIndex = 0
    bIndex = 0
    resultArray = []
    while aIndex < len(a) and bIndex < len(b):
        if a[aIndex] <= b[bIndex]:
            resultArray.append(a[aIndex])
            aIndex += 1
        else:
            resultArray.append(b[bIndex])
            bIndex += 1

    if aIndex < len(a):
        resultArray += a[aIndex:len(a)]
    
    if bIndex < len(b):
        resultArray += b[bIndex:len(b)]

    return resultArray

def mergeSort(array):
    arrayLength = len(array)
    if arrayLength < 2:
        return array
    
    midIndex = arrayLength // 2
    lefSideSortedArray = mergeSort(array[0:midIndex])
    rightSideSortedArray = mergeSort(array[midIndex:arrayLength])
    return merge(lefSideSortedArray, rightSideSortedArray)
    
def solveProblem():
    N = int(input())
    array = list(map(int, input().split()))
    sortedArray = mergeSort(array)
    [print(x, end=' ') for x in sortedArray]

solveProblem()