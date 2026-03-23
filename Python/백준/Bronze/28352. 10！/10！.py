import sys
input = sys.stdin.readline

n = int(input())
sec = 1
for i in range(2, n + 1):
    sec *= i
print(int(sec / (7 * 24 * 60 * 60)))