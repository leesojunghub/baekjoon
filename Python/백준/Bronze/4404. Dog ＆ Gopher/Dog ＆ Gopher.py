import sys, math
x, y, x1, y1 = map(float, sys.stdin.readline().split())
l = []
for line in sys.stdin:
    a, b = map(float, line.split())
    l.append((a, b))
for a, b in l:
    if ((a - x)**2 + (b - y) ** 2) ** 0.5 <= ((a - x1)**2 + (b - y1) ** 2) ** 0.5 / 2:
        print('The gopher can escape through the hole at (%.3f,%.3f).'%(a, b))
        exit()
print('The gopher cannot escape.')