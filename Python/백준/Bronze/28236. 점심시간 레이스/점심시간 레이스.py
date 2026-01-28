import sys
n, m, k = map(int, sys.stdin.readline().split())
win = k + 1
dist = n + m + 1
for i in range(1, k+1):
    f, d = map(int, sys.stdin.readline().split())
    if f - 1 + m - d < dist:
        dist = f - 1 + m - d
        win = i
print(win)