import sys
s = sys.stdin.readline().strip()
l = len(s)
n = int(s)
for i in range(1, l):
    p = 10 ** i
    n = (n + p // 2) // p * p
print(n)