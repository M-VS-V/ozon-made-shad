n, x, y, a0 = map(int, input().split())
m, z, t, b0 = map(int, input().split())
bLen = 2 * m + 2
MOD_A = 1 << 16
MOD_B = 1 << 30

a = [None] * n; a[0] = a0
prefixSums = [None] * n; prefixSums[0] = a0

def rqs(l, r):
    if l == 0:
        return prefixSums[r]
    return prefixSums[r] - prefixSums[l - 1]

for i in range(1, n):
    a[i] = (x * a[i - 1] + y) % MOD_A
    prefixSums[i]  = prefixSums[i - 1] + a[i]


b = [None] * bLen; b[0] = b0
for i in range(1, bLen):
    b[i] = (z * b[i - 1] + t) % MOD_B

totalSum = 0
for i in range(0, m):
    c1 = b[2 * i] % n
    c2 = b[2 * i + 1] % n
    left = min(c1, c2)
    right = max(c1, c2)
    totalSum += rqs(left, right)

print(totalSum)



