import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
MAX = 100000
graph = [float('INF')] * (MAX+1)
graph[n] = 0
queue = deque()
queue.append(n)
while queue:
    node = queue.popleft()
    nx = node * 2
    if nx <= MAX and graph[nx] > graph[node] + 1:
        graph[nx] = graph[node] + 1
        queue.appendleft(nx)
    nx = node - 1
    if nx >= 0 and graph[nx] > graph[node] + 1:
        graph[nx] = graph[node] + 1
        queue.append(nx)
    nx = node + 1
    if nx <= MAX and graph[nx] > graph[node] + 1:
        graph[nx] = graph[node] + 1
        queue.append(nx)
print(graph[k])