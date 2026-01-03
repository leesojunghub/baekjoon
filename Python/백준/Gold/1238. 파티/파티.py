import sys
import heapq

def dijkstra(start, g):
    dist = [INF] * (N + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        cur, u = heapq.heappop(pq)
        if cur > dist[u]:
            continue
        for v, w in g[u]:
            if dist[v] > cur + w:
                dist[v] = cur + w
                heapq.heappush(pq, (dist[v], v))
    return dist

INF = 10**18
N, M, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
rev_graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, t = map(int, sys.stdin.readline().split())
    graph[a].append((b, t))
    rev_graph[b].append((a, t))

back = dijkstra(X, graph)
go = dijkstra(X, rev_graph)
result = 0
for i in range(1, N+1):
    result = max(result, back[i]+go[i])
print(result)