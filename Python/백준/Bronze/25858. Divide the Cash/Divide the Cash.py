import sys

n, total = map(int, sys.stdin.readline().strip().split())
l = []
for _ in range(n):
    l.append(int(sys.stdin.readline().strip()))
s = sum(l)
for i in l:
    print(int(total/s*i))