import sys
import math
n, k, c, r = map(int, sys.stdin.readline().strip().split())
base = list(map(int, sys.stdin.readline().strip().split()))
s = list(map(int, sys.stdin.readline().strip().split()))
p = list(map(int, sys.stdin.readline().strip().split()))
star = 0
tired = 0
combo = 0
skill = [0] * k 
for _ in range(n):
    b = int(sys.stdin.readline())
    if b == 0:
        tired -= r
        combo = 0
    else:
        star += base[b-1] * (100 + combo * c) * (100 + skill[b-1] * s[b-1]) // 10000
        combo += 1
        skill[b-1] += 1
        tired += p[b-1]
    if tired < 0:
        tired = 0
    elif tired > 100:
        print(-1)
        exit()
print(star)