import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1) 

for _ in range(m):
    l = list(map(int, input().split()))
    for i in range(1, l[0]):
        graph[l[i]].append(l[i+1])
        indegree[l[i+1]] += 1

queue = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)

result = []
while queue:
    now = queue.popleft()
    result.append(now)
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            queue.append(i)
if set(result) == set(range(1,n+1)):
    for i in result:
        print(i)
else:
    print(0)