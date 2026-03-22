import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, d = map(int,input().split())
    cnt = 0
    for i in range(n):
        v, f, c = map(int,input().split())
        if v * f / c >= d:
            cnt += 1
    print(cnt)