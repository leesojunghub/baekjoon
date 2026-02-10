import sys
N, L = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
cow = list(range(1, N + 1))
l_idx = 0
c_idx = 0
while N != 1:
    c_idx = (c_idx + l[l_idx] - 1) % N
    l_idx = (l_idx + 1) % L
    cow.pop(c_idx)
    N -= 1
print(cow[0])