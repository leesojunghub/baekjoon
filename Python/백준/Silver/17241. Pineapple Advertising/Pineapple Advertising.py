import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())

adj = [set() for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    if a == b:
        continue
    adj[a].add(b)
    adj[b].add(a)
served = [False]*(N+1)
cnt = [0]*(N+1)
for u in range(1, N+1):
    cnt[u] = len(adj[u]) + 1
out = []
for _ in range(Q):
    i = int(input())
    out.append(str(cnt[i]))
    if cnt[i] == 0:
        continue
    new_served = []
    if not served[i]:
        served[i] = True
        new_served.append(i)
    for v in adj[i]:
        if not served[v]:
            served[v] = True
            new_served.append(v)
    for v in new_served:
        if cnt[v] > 0:
            cnt[v] -= 1
        for u in adj[v]:
            if cnt[u] > 0:
                cnt[u] -= 1 
print("\n".join(out))
