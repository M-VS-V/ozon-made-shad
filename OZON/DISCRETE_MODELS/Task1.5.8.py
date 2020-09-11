from itertools import permutations

def cost(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

points = [
    (11, 27),
    (34, 4),
    (90, 63),
    (40, 80),
    (20, 20),
    (50, 60),
    (85, 69)
]

def pathCost(path):
    total = 0
    for i in range(1, len(path)):
        total += cost(path[i], path[i - 1])
    return total + cost(terminalPoint, path[0]) + cost(terminalPoint, path[-1])


terminalPoint = (20, 19)
possiblePaths = list(permutations(points))

result = round(min([pathCost(path) for path in possiblePaths]))
print(result)

