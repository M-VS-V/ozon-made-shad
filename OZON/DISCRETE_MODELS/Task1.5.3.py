from itertools import product

def isGood(time):
    h = time[0]
    m = time[1]
    s = time[2]
    return m != 0 and h % m == 0 and s != 0 and m % s == 0


hours = range(24)
minutes = range(60)
seconds = range(60)

allTimes = product(hours, minutes, seconds)

result = sum([1 for time in allTimes if isGood(time)])
print(result)