

def getBits(x):
    array = [0,0,0,0]
    i = 0
    while i < 4:
      isBitOne = ((1 << i) & x) >> i  == 1
      result = 1 if isBitOne else 0
      array[3 - i] = result
      i += 1
    return array

def f(arr):
    x1,x2,x3,x4 = arr
    cond = (x3 and (x2 or x4)) or not(x1 and x2 or x3 or x4)
    return 1 if cond else 0

result = [0] * 16
for i in range(0,  16):
    result[i] = f(getBits(i))
    print(f'i:{i} {getBits(i)}  {result[i]}')

assert(result == [1,0,0,1,1,0,1,1,1,0,0,1,0,0,1,1])
    
