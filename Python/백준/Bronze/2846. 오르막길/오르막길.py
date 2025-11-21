import sys
input = sys.stdin.readline
n = int(input())
l = list(map(int, input().split()))
best = 0
start = l[0]
for i in range(1, n):
    if l[i] > l[i-1]:
        continue
    else:
        best = max(best, l[i-1] - start)
        start = l[i]
best = max(best, l[-1] - start)
print(best)
