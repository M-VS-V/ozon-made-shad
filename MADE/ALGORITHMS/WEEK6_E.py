
def solve():
    THRESHOLD = 100
    DUMMY = int(1e9)
    n = int(input())
    if n == 0:
        print(0)
        print("0 0")
        return


    costs = []
    
    for _ in range(n):
        costs.append(int(input()))

    if costs[0] > THRESHOLD:
        dp = [ [DUMMY, costs[0]] ]
    else:
        dp = [[costs[0]]]

    def getSafe(i, k):
        if k >= len(dp[i]) or k < 0: 
            return DUMMY

        return dp[i][k]

    def getPrevIndexiesAndValue(i, k1, k2):
        usedCouponValue = getSafe(i - 1, k1)
        unusedCouponValue = getSafe(i - 1, k2) + costs[i]
        if usedCouponValue < unusedCouponValue:
            return (usedCouponValue, k1)
        else:
            return (unusedCouponValue, k2)

    prev = {}

    for i in range(1, n):
        dp.append([DUMMY] * len(dp[i - 1]))
        for k in range(0, len(dp[i - 1])):
            if costs[i] > THRESHOLD:
                (value, kPrev) = getPrevIndexiesAndValue(i, k + 1, k - 1)
            else:
                (value, kPrev) = getPrevIndexiesAndValue(i, k + 1, k)

            dp[i][k] = value
            prev[(i, k)] = (i - 1, kPrev)

        if costs[i] > THRESHOLD:
            dp[i].append(dp[i - 1][k] + costs[i])
            prev[(i, k + 1)] = (i - 1, k)

    kOpt = 0

    for k in range(len(dp[n - 1])): 
        if dp[n - 1][k] <= dp[n - 1][kOpt]:
            kOpt = k

    current = (n - 1, kOpt)
    totalCoupons = 0
    days = []
    while current[0] > 0:
        prevState = prev[current]
        if prevState[1] == current[1] + 1:
            totalCoupons += 1
            days.append(current[0])
        current = prevState


    print(dp[n - 1][kOpt])
    print(f'{kOpt} {totalCoupons}')
    for d in reversed(days):
        print(d + 1)

solve()