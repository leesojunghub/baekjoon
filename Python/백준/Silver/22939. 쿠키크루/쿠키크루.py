import sys
from itertools import permutations

n = int(sys.stdin.readline().strip())
home = None
cookie = None
kinds = ['J', 'C', 'B', 'W']
fields = ['Assassin', 'Healer', 'Mage', 'Tanker']
pos = {ch: [] for ch in kinds}

def dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

board = [sys.stdin.readline().strip() for _ in range(n)]
for i in range(n):
    for j in range(n):
        ch = board[i][j]
        if ch == 'H':
            home = (i, j)
        elif ch == '#':
            cookie = (i, j)
        elif ch in pos:
            pos[ch].append((i, j))

best_cost = 10**4+1
best_field = None

for ch, name in zip(kinds, fields):
    cells = pos[ch]
    # 모든 순열(3개 방문 순서) 시도
    for p1, p2, p3 in permutations(cells, 3):
        d = dist(home, p1) + dist(p1, p2) + dist(p2, p3) + dist(p3, cookie)
        if d < best_cost:
            best_cost = d
            best_field = name

print(best_field)
