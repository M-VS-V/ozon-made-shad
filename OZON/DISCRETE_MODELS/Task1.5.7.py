from itertools import product

allSums = set()
for element in product(range(16), range(11), range(9)):
    allSums.add(element[0] * 1 + element[1] * 5 + element[2] * 10)

print(len(allSums) - 1)