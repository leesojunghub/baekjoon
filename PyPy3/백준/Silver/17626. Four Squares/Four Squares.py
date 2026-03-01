import sys
input = sys.stdin.readline

n = int(input())
dp = [0] + [10**5] * n
for i in range(1, n+1):
    j = 1
    while j ** 2 <= i:
        dp[i] = min(dp[i], dp[i - j **2] + 1)
        j += 1
print(dp[n])