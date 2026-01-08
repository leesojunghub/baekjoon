import sys
b, n, m = map(int, sys.stdin.readline().split())
dic = {}
for _ in range(n):
    i, p = sys.stdin.readline().strip().split()
    dic[i] = int(p)
cost = 0
for _ in range(m):
    j = sys.stdin.readline().strip()
    cost += dic[j]
if cost <= b:
    print('acceptable')
else:
    print('unacceptable')