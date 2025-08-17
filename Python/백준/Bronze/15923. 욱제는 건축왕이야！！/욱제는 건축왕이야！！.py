import sys

n = int(sys.stdin.readline().strip())
xy = [tuple(map(int, input().split())) for _ in range(n)]
s = 0
for i in range(n):
    x1, y1 = xy[i]
    x2, y2 = xy[(i + 1) % n]
    s += abs(x1 - x2) + abs(y1 - y2)

print(s)