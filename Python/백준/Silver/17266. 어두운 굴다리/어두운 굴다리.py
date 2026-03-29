import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
x = list(map(int, input().split()))
best = x[0]
for i in range(1, m):
    best = max(best, (x[i] - x[i-1] + 1) // 2)
best = max(best, n - x[-1])
print(best)