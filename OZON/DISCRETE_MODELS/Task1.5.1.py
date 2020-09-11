def isGood(x):
    xStr = set(str(x))
    return ('4' in xStr or '5' in xStr) and not (('6' in xStr) and ('7' in xStr))

answer = sum(1 for x in range(123456, 7891012) if isGood(x))
print(answer)
