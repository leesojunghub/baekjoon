import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    l = list(sys.stdin.readline().strip().split())
    s = l[0]
    for i in range(1, n):
        if l[i] <= s[0]:
            s = l[i] + s
        else:
            s = s + l[i]
    print(s)
