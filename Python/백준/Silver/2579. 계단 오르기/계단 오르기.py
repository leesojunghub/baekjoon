import sys
n = int(sys.stdin.readline())
l = [int(sys.stdin.readline()) for _ in range(n)]
if n <= 1:
    print(l[0])
    sys.exit()
elif n <=2:
    print(l[0] + l[1])
    sys.exit()
dp = [0] * n
dp[0] = l[0]
dp[1] = l[0] + l[1]
dp[2] = max(l[0] + l[2], l[1] + l[2])
for i in range(3, n):
    dp[i] = max(dp[i-2] + l[i], dp[i-3] + l[i-1] + l[i])
print(dp[n-1])