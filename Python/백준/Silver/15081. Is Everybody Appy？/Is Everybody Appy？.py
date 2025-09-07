import sys
n = int(sys.stdin.readline())
l = []
for _ in range(n):
    m = list(sys.stdin.readline().strip().split())
    for i in range(1, int(m[0])+1):
        if m[i] not in l:
            l.append(m[i])
            break
print(" ".join(l))