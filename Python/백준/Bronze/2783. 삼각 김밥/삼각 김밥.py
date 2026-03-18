import sys
input = sys.stdin.readline

x, y = map(int, input().split())
best = x / y * 1000
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    i = x / y * 1000
    if i < best:
        best = i
print("%.2f"%best)