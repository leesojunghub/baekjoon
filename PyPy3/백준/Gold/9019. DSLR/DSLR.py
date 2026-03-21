import sys
from collections import deque
input = sys.stdin.readline

def D(x):
    return (x * 2) % 10000

def S(x):
    return 9999 if x == 0 else x - 1

def L(x):
    return (x % 1000) * 10 + x // 1000

def R(x):
    return (x % 10) * 1000 + x // 10

t = int(input())
for _ in range(t):
    start, target = map(int, input().split())
    visit = [False] * 10000
    how = [''] * 10000
    parent = [-1] * 10000
    q = deque([start])
    visit[start] = True
    while q:
        now = q.popleft()
        if now == target:
            break
        for nxt, op in ((D(now), 'D'), (S(now), 'S'), (L(now), 'L'), (R(now), 'R')):
            if not visit[nxt]:
                visit[nxt] = True
                parent[nxt] = now
                how[nxt] = op
                q.append(nxt)
    result = []
    now = target
    while now != start:
        result.append(how[now])
        now = parent[now]
    result.reverse()
    print("".join(result))