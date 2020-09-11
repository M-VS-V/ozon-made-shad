import random
def partition3(a, l, r):
   k = random.randint(l, r)
   x, j, t = a[k], l, r
   i = j

   while i <= t :
      if a[i] < x:
         a[j], a[i] = a[i], a[j]
         j += 1

      elif a[i] > x:
         a[t], a[i] = a[i], a[t]
         t -= 1
         i -= 1 # remain in the same i in this case
      i += 1   
   return j, t


def quickSelect(array, i, j, k):
    if i == j:
        return array[i]
  
    left, right = partition3(array, i, j)
    if i + k < left:
        return quickSelect(array, i, left - 1, k)
    elif k >= right - i + 1:
        return quickSelect(array, right + 1, j, i + k - right - 1)
    else:
        return array[left]


def solveProblem():
    _ = int(input())
    clones = list(map(int, input().split()))
    queriesNumber = int(input())

    for _ in range(queriesNumber):
        i, j, k = map(int, input().split())
        leftIndex = i - 1
        rightIndex = j - 1
        result = quickSelect(clones[leftIndex:rightIndex + 1], 0, j - i, k - 1)

        print(result)

solveProblem()


#print(quickSelect([4,3,2,1], 0, 3, 3))
assert(quickSelect([1,2,3], 0,2,0) == 1)
assert(quickSelect([1,2,3], 0,2,1) == 2)
assert(quickSelect([1,2,3], 0,2,2) == 3)
assert(quickSelect([4,3,2,1],0,3, 0) == 1)
assert(quickSelect([4,3,2,1],0,3, 1) == 2)
assert(quickSelect([4,3,2,1],0,3, 2) == 3)
assert(quickSelect([4,3,2,1],0,3, 3) == 4)
assert(quickSelect([3,3,1,1,2,2],0,5, 0) == 1)
assert(quickSelect([3,3,1,1,2,2],0,5, 1) == 1)
assert(quickSelect([3,3,1,1,2,2],0,5, 2) == 2)
assert(quickSelect([3,3,1,1,2,2],0,5, 3) == 2)
assert(quickSelect([3,3,1,1,2,2],0,5, 3) == 2)
assert(quickSelect([3,3,1,1,2,2], 1, 1,0) == 3)
assert(quickSelect([3,3,1,1,2,2], 2, 3, 0) == 1)
assert(quickSelect([3,3,1,1,2,2], 2, 3, 1) == 1)
assert(quickSelect([3,3,1,1,2,2], 1, 4, 0) == 1)
assert(quickSelect([3,3,1,1,2,2], 1, 4, 1) == 1)
assert(quickSelect([3,3,1,1,2,2], 1, 4, 2) == 2)
assert(quickSelect([3,3,1,1,2,2], 1, 4, 3) == 3)
assert(quickSelect([4,3,2,1], 0, 3, 0) == 1)
assert(quickSelect([4,3,2,1], 0, 3, 1) == 2)
assert(quickSelect([4,3,2,1], 0, 3, 2) == 3)
assert(quickSelect([4,3,2,1], 0, 3, 3) == 4)
assert(quickSelect([1],0,0, 1) == 1)
assert(quickSelect([1,1,1,1],2,3,1) == 1)
assert(quickSelect([12,2,3,7,4,56,2,2],1,6,0) == 2)
assert(quickSelect([12,2,3,7,4,56,2,2],1,6,1) == 2)
assert(quickSelect([12,2,3,7,4,56,2,2],1,6,2) == 3)
assert(quickSelect([12,2,3,7,4,56,2,2],1,6,3) == 4)
assert(quickSelect([12,2,3,7,4,56,2,2],1,6,4) == 7)
assert(quickSelect([12,2,3,7,4,56,2,2],1,6,5) == 56)
assert(quickSelect([12,2,3,7,4,56,2,2],7,7,0) == 2)
assert(quickSelect([12,2,3,7,4,56,2,2],5,5,0) == 56)
assert(quickSelect([12,2,3,7,4,56,2,2],1,7,0) == 2)
assert(quickSelect([12,2,3,7,4,56,2,2],1,7,1) == 2)
assert(quickSelect([12,2,3,7,4,56,2,2],1,7,2) == 2)
assert(quickSelect([12,2,3,7,4,56,2,2],1,7,3) == 3)
assert(quickSelect([12,2,3,3,7,4,56,2,2],2,4,0) == 3)
assert(quickSelect([12,2,3,3,7,4,56,2,2],2,4,1) == 3)
assert(quickSelect([12,2,3,3,7,4,56,2,2],2,4,2) == 7)