import sys
n, m, k = map(int, sys.stdin.readline().strip().split())
print(min(m, k) + min(n - m, n - k))