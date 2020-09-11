import random

def qSort(array, begin, end):
    if begin > end:
        return
    left, right = begin, end
    pivot = array[random.randint(begin, end)]
    while left <= right:
        while array[left] < pivot: left += 1
        while array[right] > pivot: right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left = left + 1
            right = right - 1 

    qSort(array, begin, right)
    qSort(array, left, end)
    
def solveProblem():
    N = int(input())
    array = list(map(int, input().split()))
    qSort(array, 0, len(array) - 1)
    [print(x, end=' ') for x in array]

solveProblem()