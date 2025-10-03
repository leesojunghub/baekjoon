import sys
l = list(map(int, sys.stdin.readline().strip().split()))
if l[-1] * 4 - sum(l[:4]) > 0:
    print(l[-1] * 4 - sum(l[:4]))
else:
    print(0)