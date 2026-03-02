import sys
from collections import deque
input = sys.stdin.readline

def bfs(start_row, start_col, grid, dist):
    queue = deque([(start_row,start_col)])
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    while queue:
        row, col = queue.popleft()
        for d in range(4):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if not (0 <= next_row < n and 0 <= next_col < m):
                continue
            if grid[next_row][next_col] == 0:
                dist[next_row][next_col] = 0
                continue
            if dist[next_row][next_col] != -1:
                continue

            dist[next_row][next_col] = dist[row][col] + 1
            queue.append((next_row, next_col))


n, m = map(int, input().split())
grid = []
for _ in range(n):
    i = list(map(int, input().split()))
    grid.append(i)
for i in range(n):
    if 2 in grid[i]:
        start_row = i
        start_col = grid[i].index(2)
dist = [[-1] * m for _ in range(n)]
dist[start_row][start_col] = 0
bfs(start_row, start_col, grid, dist)

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            dist[i][j] = 0

for i in dist:
    print(' '.join(map(str, i)))
