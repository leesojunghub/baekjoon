import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
l = [input().strip() for _ in range(n)]
cnt = Counter(l)
cnt = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))
print(cnt[0][0])