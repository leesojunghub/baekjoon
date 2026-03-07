import sys
from collections import defaultdict
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i].sort(reverse=True)

depth = [-1] * (n + 1)
visit = [0] * (n + 1)
seen = [False] * (n + 1)

stack = [(r, 0, 0)]
seen[r] = True
depth[r] = 0
cnt = 1
visit[r] = cnt
cnt += 1

while stack:
    v, d, idx = stack[-1]
    if idx == len(graph[v]):
        stack.pop()
        continue

    nv = graph[v][idx]
    stack[-1] = (v, d, idx + 1)
    if seen[nv]:
        continue

    seen[nv] = True
    depth[nv] = d + 1
    visit[nv] = cnt
    cnt += 1
    stack.append((nv, d + 1, 0))

result = 0
for i in range(1, n + 1):
    result += depth[i] * visit[i]
print(result)
