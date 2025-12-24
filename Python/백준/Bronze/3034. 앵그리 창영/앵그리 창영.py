import sys
n, w, h = map(int, sys.stdin.readline().split())
for _ in range(n):
    i = int(sys.stdin.readline())
    if i**2 <= w**2 + h**2:
        print('DA')
    else:
        print('NE')