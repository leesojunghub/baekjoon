import sys
from collections import defaultdict
import heapq
n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
graph = defaultdict(list)
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().strip().split())
    graph[u].append((v, w))
start, end = map(int, sys.stdin.readline().strip().split())
distance = [float('inf')] * (n + 1)
distance[start] = 0
heap = [(0, start)]
while heap:
    dist, now = heapq.heappop(heap)
    if dist>distance[now]:
        continue
    for neighbor, weight in graph[now]:
        cost = dist + weight
        if cost < distance[neighbor]:
            distance[neighbor] = cost
            heapq.heappush(heap, (cost, neighbor))
print(distance[end])