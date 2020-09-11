# def isPossibleToCut(ropeLength, ropes, housesCount):
#     return sum([length // ropeLength for length in ropes]) >= housesCount

# def getOptimalRopeLength(ropes, housesCount):
#     if not isPossibleToCut(1, ropes, housesCount):
#         return 0

#     left = 1
#     right = max(ropes) + 1

#     while right - left >= 2:
#         ropeLength = left + (right - left) // 2

#         if isPossibleToCut(ropeLength, ropes, housesCount):
#             left = ropeLength
#         else:
#             right = ropeLength

#     return left


# def solveProblem():
#     ropesNumber, housesCount = map(int, input().split())
#     ropes = []

#     for _ in range(ropesNumber):
#         ropes.append(int(input()))

#     optimalLength = getOptimalRopeLength(ropes, ropes)
#     print(optimalLength)
    

# assert(getOptimalRopeLength([802, 743, 457, 539], 11) == 200)
# assert(getOptimalRopeLength([3, 3, 3, 3], 13) == 0)
# assert(getOptimalRopeLength([15, 14, 13, 12, 11], 15) == 3)
# assert(getOptimalRopeLength([234, 23, 143, 12, 11], 1) == 234)
