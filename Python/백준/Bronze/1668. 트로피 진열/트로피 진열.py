import sys
input = sys.stdin.readline

n = int(input())
l = [int(input()) for _ in range(n)]
best = l[0]
cnt = 1
for i in range(1, n):
    if l[i] > best:
        cnt += 1
        best = l[i]
print(cnt)
l.reverse()
best = l[0]
cnt = 1
for i in range(1, n):
    if l[i] > best:
        cnt += 1
        best = l[i]
print(cnt)