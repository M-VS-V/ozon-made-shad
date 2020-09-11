
def f1(a,b,c):
    return (a or (a and b)) == a

def f2(a,b,c):
    return (a and (a or b)) == a

def f3(a,b,c):
    return (a and ( (not a) or b)) == (a and b)

def f4(a,b,c):
    return a or ( (not a) and b) == a or b

def f5(a,b,c):
    return (a and b) or ((not a) and c) or (b and c) == (a and b) or ((not a) and c)


array = [(0,0,0),(0,0,1),(0,1,0),(1,0,0),(0,1,1),(1,0,1),(1,1,0),(1,1,1)]
for (a, b, c) in array:
    assert(f3(a, b, c))