import sys
a, b, c = map(int, sys.stdin.readline().strip().split())
if c >= 2:
    print(a * 2 + b * 2 + (c//2) * 3)
else:
    print(a * 2)