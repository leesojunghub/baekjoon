import sys
from collections import Counter

m, n = map(int, sys.stdin.readline().strip().split())
c = [0] * 10
for i in range(m, n + 1):
    x = i
    while x > 0:
        c[x%10] += 1
        x = x // 10
print(" ".join(map(str, c)))