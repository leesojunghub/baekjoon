import sys
input = sys.stdin.readline

a, b, c, x, y = map(int, input().split())
case1 = a * x + b * y
case2 = min(x, y) * 2 * c + (x - min(x, y)) * a + (y - min(x, y)) * b
case3 = max(x, y) * 2 * c

print(min(case1, case2, case3))