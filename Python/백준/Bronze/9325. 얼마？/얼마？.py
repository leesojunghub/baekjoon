import sys
t = int(sys.stdin.readline().strip())
for _ in range(t):
    s = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        q, p = map(int, sys.stdin.readline().strip().split())
        s += q * p
    print(s)