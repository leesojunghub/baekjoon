import sys

n = int(sys.stdin.readline())
l = [int(sys.stdin.readline()) for _ in range(n)]
L = int(sys.stdin.readline())
Q = int(sys.stdin.readline())
s = [0]
for i in l:
    s.append(s[-1] + i)
center = [0.0] * n
for i in range(n):
    center[i] = s[i+1] - l[i] / 2.0
mid = L / 2

for _ in range(Q):
    q = int(sys.stdin.readline()) - 1
    if s[-1] <= L:
        print("0.00")
    else:
        c = center[q] - mid
        if c < 0.0:
            print("0.00")
        elif c > max(0.0, s[-1]-L):
            print("%.2f"%max(0.0, s[-1]-L))
        else:
            print("%.2f"%c)