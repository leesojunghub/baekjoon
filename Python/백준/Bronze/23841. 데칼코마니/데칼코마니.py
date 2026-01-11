import sys
n, m = map(int, sys.stdin.readline().split())
l = []
for _ in range(n):
    a = list(sys.stdin.readline().strip())
    l.append(a)
for i in range(n):
    for j in range(m):
        if l[i][j] != '.':
            l[i][m-1-j] = l[i][j]
for i in l:
    print(''.join(i))