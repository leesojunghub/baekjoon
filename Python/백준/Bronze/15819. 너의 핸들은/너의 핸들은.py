import sys
n, i = map(int, sys.stdin.readline().split())
handle = [sys.stdin.readline().strip() for _ in range(n)]
handle.sort()
print(handle[i-1])