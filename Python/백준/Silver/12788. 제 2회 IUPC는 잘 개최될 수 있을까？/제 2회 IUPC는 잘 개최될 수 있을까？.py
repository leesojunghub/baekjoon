import sys

n = int(sys.stdin.readline())
m, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
a.sort(reverse=True)
c = 0
s = 0
for i in a:
    s += i
    c += 1
    if s >= m * k:
        print(c)
        exit()
print('STRESS')