import sys
n, m, x = map(int, sys.stdin.readline().split())
mountain = list(map(int, sys.stdin.readline().split()))
img = [['.'] * m for _ in range(n)]
img[n - x] = ['-'] * m
for i in range(m):
    h = mountain[i]
    for j in range(n-1, n-h-1, -1):
        if img[j][i] == '.':
            img[j][i] = '#'
        elif img[j][i] == '-':
            img[j][i] = '*'
for i in range(2, m, 3):
    for j in range(n - x + 1, n):
        if img[j][i] == '.':
            img[j][i] = '|'
        else:
            continue
for i in img:
    print("".join(i))