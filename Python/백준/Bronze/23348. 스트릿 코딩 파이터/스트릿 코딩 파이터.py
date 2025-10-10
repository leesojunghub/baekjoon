import sys
A, B, C = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
l = []
for _ in range(n):
    point = 0
    for i in range(3):
        a, b, c = map(int, sys.stdin.readline().split())
        point += A * a + B * b + C * c
    l.append(point)
print(max(l))