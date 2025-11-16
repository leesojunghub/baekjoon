import sys
n, m = map(int, sys.stdin.readline().split())
map = []
for _ in range(n):
    a = list(sys.stdin.readline().strip().split())
    map.append(a)
row = -1
col = -1
distance = float('INF')
for i in range(n):
    for j in range(m):
        if map[i][j] == '0':
            a = i + 1+ abs((m + 1) / 2 - j - 1)
            if a < distance:
                distance = a
                row = i
                col = j
if row == -1 and col == -1:
    print(-1)
else:
    print(row + 1, col + 1)