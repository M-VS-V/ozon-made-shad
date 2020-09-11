def solve():
    n = int(input())
    seq = list(map(int, input().split()))
    dp = [1] * n

    prevIndicies = [None] * n

    def findIndex(i):
        previousOptimalIndex = None
        for endSeqIndex in range(0, i):
            if seq[endSeqIndex] >= seq[i]:
                continue

            if previousOptimalIndex is None or dp[endSeqIndex] > dp[previousOptimalIndex]:
                previousOptimalIndex = endSeqIndex

        return previousOptimalIndex
    
    optIndex = 0
    for i in range(1, n):
        prevIndex = findIndex(i)
        if prevIndex is not None:
            dp[i] = dp[prevIndex] + 1
            prevIndicies[i] = prevIndex
        
        if dp[i] > dp[optIndex]:
            optIndex = i

    result = []
    seqElementIndex = optIndex
    while seqElementIndex is not None:
        result.append(seq[seqElementIndex])
        seqElementIndex = prevIndicies[seqElementIndex]

    print(len(result))
    [print(x, end = ' ') for x in reversed(result)]

solve()