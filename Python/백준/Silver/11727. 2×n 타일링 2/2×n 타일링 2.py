import sys
input = sys.stdin.readline

n = int(input())
tile = [0] * (n+1)
tile[1] = 1
if n == 1:
    print(tile[n])
    sys.exit()
tile[2] = 3
for i in range(3, n + 1):
    tile[i] = tile[i-1] + tile[i-2] * 2
print(tile[n] % 10007)
