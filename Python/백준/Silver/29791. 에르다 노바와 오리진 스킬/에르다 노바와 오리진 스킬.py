import sys
from bisect import bisect_left
n, m = map(int, sys.stdin.readline().strip().split())
a = list(map(int, sys.stdin.readline().strip().split()))
b = list(map(int, sys.stdin.readline().strip().split()))
a.sort()
b.sort()
ac = 0
bc = 0
i = 0
while i < n:
    ac += 1
    i = bisect_left(a, a[i] + 100, i+1)
i = 0
while i < m:
    bc += 1
    i = bisect_left(b, b[i] + 360, i+1)
print(ac, bc)