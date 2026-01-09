import sys
def dfs(start):
    stack = [(start,0,0)] #node, parent, dist
    node = start
    dist = 0
    while stack:
        u, p, d = stack.pop()
        if d > dist:
            dist = d
            node = u
        for v, w in graph[u]:
            if v == p:
                continue
            stack.append((v, u, w+d))
    return node, dist
n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
far_1, dist_1 = dfs(1)
far_max, dist_max = dfs(far_1)
print(dist_max)