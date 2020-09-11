from math import sqrt
from math import log2

def f(x):
    return x * x + sqrt(x)
    
def solve(rightPartOfEquationConstant):
    PRECISION = 1e-7
    left = 1.0
    right = rightPartOfEquationConstant
    iterationsCount = int(log2((right - left) / PRECISION))

    for i in range(iterationsCount):

        if (right - left) < PRECISION:
            return right
        
        m = (left + right) / 2.0
        if f(m) < rightPartOfEquationConstant:
            left = m
        else:
            right = m
            
    return (left + right) / 2.0
 
def solveProblem():
    rightPartOfEquationConstant = float(input())
    result = solve(rightPartOfEquationConstant)
    print('{:.6f}'.format(result))
 
solveProblem()