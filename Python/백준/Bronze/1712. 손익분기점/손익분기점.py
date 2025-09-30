import sys
a, b, c = map(int, sys.stdin.readline().strip().split())
if c - b <= 0:
    print(-1)
else:
    print(a // (c - b) + 1)