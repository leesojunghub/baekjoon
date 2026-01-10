import sys
n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
l.sort()
cost = 0
for i in range(n-1):
    cost += l[i] * sum(l[i+1:])
print(cost)