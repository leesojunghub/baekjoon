import sys
from collections import defaultdict
n, m = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)
x = int(sys.stdin.readline())
visit = set()
stack = [x]
while stack:
    a = stack.pop()
    if a in visit:
        pass
    else:
        visit.add(a)
        for i in graph[a]:
            if i not in visit:
                stack.append(i)
print(len(visit) - 1)
