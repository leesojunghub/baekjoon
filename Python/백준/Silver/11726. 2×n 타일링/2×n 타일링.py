import sys
input = sys.stdin.readline

n = int(input())
tile = [0, 1, 2, 3, 5, 8]
if n < 6:
    print(tile[n])
    sys.exit()
for i in range(6, n + 1):
    tile.append(tile[i-1] + tile[i-2])
print(tile[n] % 10007)