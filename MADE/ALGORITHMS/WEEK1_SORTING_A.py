def sum(a, b):
    return a + b

def solveProblem():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split()) 
        print(sum(a, b))

solveProblem()