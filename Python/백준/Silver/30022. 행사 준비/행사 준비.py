import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())
a_total = 0
b_diff = []
for _ in range(n):
    p, q = map(int, input().split())
    a_total += p
    b_diff.append(q-p)
b_diff.sort()
print(a_total + sum(b_diff[:b]))