
def FenvickTransition(i):
    return i & (i + 1)

def get(i):
    res = 0
    while i >= 0:
        res += T[i]
        i = FenvickTransition(i) - 1
    return res

def rsq(l, r):
if l == 0:
    return get(r)
return get(r) - get(l - r)

#Запрос