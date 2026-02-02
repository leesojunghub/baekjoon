import sys
n = int(sys.stdin.readline())
ans = 0

for x in range(1, n + 1):
    t = x
    while t:
        d = t % 10
        if d == 3 or d == 6 or d == 9:
            ans += 1
        t //= 10

print(ans)
