import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
l = [int(input()) for _ in range(n)]
l = Counter(l)
l = sorted(l.items(), key=lambda x: (-x[1], x[0]))
print(l[0][0])