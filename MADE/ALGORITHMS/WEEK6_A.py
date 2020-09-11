n, k = map(int, input().split())
costs = list(map(int, input().split()))
costs.append(0)

#Столбик с номером i имеет costs[i - 2] монеток

dp = [None] * (n + 1)
prev = [None] * (n + 1)
dp[1] = 0 

def findMaxIndex(currentPillarNumber, k):
    currentPillarNumber -= 1
    optIndex = currentPillarNumber
    while currentPillarNumber >= 1 and k > 0:
        if dp[currentPillarNumber] >= dp[optIndex]:
            optIndex = currentPillarNumber
        k -= 1
        currentPillarNumber -= 1

    return optIndex
        
def solve():
    for i in range(2, n + 1):
        optIndex = findMaxIndex(i, k)
        dp[i] = dp[optIndex] + costs[i - 2]
        prev[i] = optIndex

    route = [n]
    i = n
    while prev[i] is not None:
        route.append(prev[i])
        i = prev[i]

    print(dp[n])
    print(len(route) - 1)
    [print(x, end=' ') for x in reversed(route)]

solve()