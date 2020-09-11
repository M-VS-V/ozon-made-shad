def isPossiblePrint(copiesNumber, time, x, y):
    timeForFirstCopy = min(x, y)
    if time < timeForFirstCopy:
        return False

    time -= timeForFirstCopy
    
    firstPrinterCopies = time // x
    secondPrinterCopies = time // y
    return firstPrinterCopies + secondPrinterCopies >= copiesNumber - 1


def getMinimalNumberOfSeconds(n, x, y):
    left = -1
    right = n * min(x, y)

    while right - left >= 2:
        time = (left + right) // 2
        if isPossiblePrint(n, time, x, y):
            right = time
        else:
            left = time

    return right

def solveProblem():
    n, x, y = map(int, input().split())
    seconds = getMinimalNumberOfSeconds(n, x, y)
   
    print(seconds)


solveProblem()

