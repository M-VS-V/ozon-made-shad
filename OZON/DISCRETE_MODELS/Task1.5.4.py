from itertools import product

def toSet(a):
    if a <= 9:
        return set(f'0{a}')
    return set(f'{a}')

def isGood(time):
    h = toSet(time[0])
    m = toSet(time[1])
    s = toSet(time[2])
    
    return len(s & m) > 0 and len(s & h) > 0


hours = range(24)
minutes = range(60)
seconds = range(60)

allTimes = product(hours, minutes, seconds)

result = sum([1 for time in allTimes if isGood(time)])
print(result)