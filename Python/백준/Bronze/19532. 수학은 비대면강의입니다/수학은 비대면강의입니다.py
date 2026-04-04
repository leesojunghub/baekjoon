import sys
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())
den = b * d - a * e
y = (c * d - a * f) // den
if a != 0:
    x = (c - b * y) // a
else:
    x = (f - e * y) // d
print(x, y)