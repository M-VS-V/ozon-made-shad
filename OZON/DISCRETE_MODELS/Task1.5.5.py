from itertools import combinations

def digits(x):
    digits = []
    while x > 0:
        r = x % 10
        digits.append(r)
        x //= 10
    return digits

def isGood(x):
    digitsOfX = digits(x)
    pairsSum = sum((a[0] * a[1] for a in combinations(digitsOfX, 2)))
    return pairsSum == 100
    
print(sum((1 for x in range(10000, 100000) if isGood(x))))