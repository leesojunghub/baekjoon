import sys
t = int(sys.stdin.readline())
for j in range(1, t+1):
    n = int(sys.stdin.readline())
    l = list(map(int, sys.stdin.readline().split()))
    for i in range(1, n-1):
        if l[i-1] + l[i+1] < 2 * l[i]:
            l[i] = (l[i-1] + l[i+1]) / 2
    print("Case #%d: %.6f" %(j, l[n-2]))