def isPossible(w, h, n, possibleSize):
    inRowCount = possibleSize // w
    inColumnCount = possibleSize // h
    return inRowCount * inColumnCount >= n
 
def solveProblem():
    w, h, n = map(int, input().split())
    left = -1
    right = int(1e20)
    while left < right - 1:
        m = (left + right) // 2
        if isPossible(w, h, n, m):
            right = m
        else:
            left = m

    return right
 
print(solveProblem())