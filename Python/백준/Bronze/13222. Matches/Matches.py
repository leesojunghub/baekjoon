import sys
n, w, h = map(int, sys.stdin.readline().split())
for _ in range(n):
    i = int(sys.stdin.readline())
    if i > (w**2 + h**2) ** 0.5:
        print('NO')
    else:
        print('YES')