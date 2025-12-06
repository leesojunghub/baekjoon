import sys
n, t = map(int, sys.stdin.readline().split())
l = [int(sys.stdin.readline()) for _ in range(n)]
for _ in range(t):
    max_value = max(l)
    maxidx = l.index(max_value)
    print(maxidx + 1)
    l[maxidx] = 0
    if max_value == 0:
        continue
    same = max_value // (n-1)
    more = max_value % (n-1)
    for i in range(n):
        if i == maxidx:
            pass
        else:
            l[i] = l[i] + same
    for i in range(n):
        if i == maxidx:
            continue
        if more == 0:
            break
        l[i] += 1
        more -= 1