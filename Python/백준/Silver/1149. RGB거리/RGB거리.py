import sys
n = int(sys.stdin.readline())
dp = [0,0,0]
for i in range(n):
    r, g, b = map(int, sys.stdin.readline().split())
    if i == 0:
        dp = [r, g, b]
    else:
        pre = dp
        dp = [
            r + min(pre[1], pre[2]),
            g + min(pre[0], pre[2]),
            b + min(pre[0], pre[1])
        ]
print(min(dp))