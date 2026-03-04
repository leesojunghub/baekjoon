import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
l = []
for _ in range(n):
    s = input().strip()
    if len(s) == 3:
        l.append(s)
l.sort()
print(l[0])