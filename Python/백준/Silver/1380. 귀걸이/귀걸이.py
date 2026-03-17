import sys
input = sys.stdin.readline
sc = 1

while True:
    n = int(input())
    if n == 0:
        break
    name = [input().strip() for _ in range(n)]
    ring = [0] * n
    for _ in range(2 * n - 1):
        idx, s = input().split()
        idx = int(idx)
        ring[idx-1] += 1
    print(sc, name[ring.index(1)])
    sc += 1
