def solveForData(n, m, matrix):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = matrix[0][0]

    def getSafe(i,j):
        BAD_CELL_VALUE = -1000
        if i < 0 or j < 0: 
            return BAD_CELL_VALUE
        
        return dp[i][j]


    for i in range(n):
        for j in range(m):
            if i == j == 0:
                continue
            upValue = getSafe(i - 1, j)
            leftValue = getSafe(i, j - 1)
            dp[i][j] = max(upValue, leftValue) + matrix[i][j]


    (i, j) = (n - 1, m - 1)
    route = []
    while not(i == 0 and j == 0):
        left = i, j - 1
        up = i - 1, j
        if i - 1 < 0:
            i, j = left
        elif j - 1 < 0:
            i, j = up
        elif dp[left[0]][left[1]] > dp[up[0]][up[1]]:
            i, j = left
        else:
            i, j = up
        
        if (i, j) == left:
            route.append("R")
        else:
            route.append("D")

    return (dp[n - 1][m - 1], ''.join(reversed(route)))


def solve():
    n, m = map(int, input().split())
    matrix = [None for _ in range(n)]
    for i in range(n):
        row = list(map(int, input().split()))
        matrix[i] = row

    result = solveForData(n, m, matrix)
    print(result[0])
    print(result[1])

solve()