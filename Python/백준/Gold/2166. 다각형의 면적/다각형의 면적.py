import sys
n = int(sys.stdin.readline())
l = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
s = 0
for i in range(n):
    x1, y1 = l[i]
    x2, y2 = l[(i+1) % n]
    s += x1*y2 - x2 * y1
s = abs(s) / 2
print("%.1f"%s)