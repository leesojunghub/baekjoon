import sys, math
t = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
result = []
for i in l:
    r = math.isqrt(i)
    if r * r == i:
        result.append('1')
    else:
        result.append('0')
print(' '.join(result))