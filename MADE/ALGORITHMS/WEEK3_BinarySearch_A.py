def findClosestInSortedArray(sortedArray, valueForApproximation):
    left = -1
    right = len(sortedArray) - 1

    while right - left >= 2:
        m = (left + right) // 2
        if valueForApproximation <= sortedArray[m]:
            right = m
        else:
            left = m

    if left == -1:
        return sortedArray[right]
    
    leftDistance = valueForApproximation - sortedArray[left]
    rightDistance = sortedArray[right] - valueForApproximation
    return sortedArray[right] if rightDistance < leftDistance else sortedArray[left]

def solveProblem():
    _, _ = list(map(int, input().split()))
    sortedArray = list(map(int, input().split()))
    queries = list(map(int, input().split()))
    resultArray = []
   
    for query in queries:
        closestNumber = findClosestInSortedArray(sortedArray, query) 
        resultArray.append(closestNumber)
            
    [print(x) for x in resultArray]

solveProblem()